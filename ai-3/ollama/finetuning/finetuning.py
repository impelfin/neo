import os
import json
import torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, PeftModel
from trl import SFTTrainer, SFTConfig
import subprocess
import logging

# 로깅 설정: 스크립트 진행 상황을 명확하게 확인하기 위해 INFO 레벨로 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 1. 설정 변수 ---
# 파인튜닝할 원본 기본 모델의 로컬 경로.
# 위에 다운로드한 Llama 3.2-1B 모델의 경로로 설정.
base_model_local_path = "./llama-3.2-1b" # <<< 이 경로를 실제 환경에 맞게 수정.

sft_json_path = "./sft.json" # 학습 데이터셋 JSON 파일 경로
# 파인튜닝 결과 및 병합 모델이 저장될 디렉터리.
output_dir = f"./finetuned-{os.path.basename(base_model_local_path).lower()}"
os.makedirs(output_dir, exist_ok=True) # 출력 디렉터리 생성

gguf_output_name = f"{os.path.basename(base_model_local_path).lower()}-finetuned.gguf"
gguf_output_path = os.path.join(output_dir, gguf_output_name)

# llama.cpp 저장소의 루트 경로. convert_hf_to_gguf.py 스크립트가 이 경로 아래에 있어야 함.
llama_cpp_path = "llama.cpp" # <<< 이 경로를 실제 환경에 맞게 수정.

# --- 2. 모델 및 토크나이저 로드 ---
logger.info(f"모델 로드 중: {base_model_local_path}...")

# MPS (Apple Silicon GPU) 사용 가능 여부 확인
if torch.backends.mps.is_available():
    device = "mps"
    logger.info("MPS (Apple Silicon GPU)가 사용 가능합니다. 이를 사용하여 학습을 가속합니다.")
else:
    device = "cpu"
    logger.warning("MPS (Apple Silicon GPU)를 사용할 수 없습니다. CPU를 사용합니다. 학습 속도가 매우 느릴 수 있습니다.")

try:
    # 4비트 양자화 (BitsAndBytesConfig) 없이 float16 정밀도로 모델을 로드.
    # 이는 bitsandbytes 설치 문제를 우회하고, MPS 가속을 계속 활용.
    model = AutoModelForCausalLM.from_pretrained(
        base_model_local_path,
        # quantization_config=bnb_config, # <<< 이 줄은 이제 사용하지 않는다.
        device_map="auto",              # 사용 가능한 디바이스(MPS)에 모델을 효율적으로 분배
        torch_dtype=torch.float16,      # 모델 파라미터를 float16으로 로드하여 메모리 절약
        low_cpu_mem_usage=True,         # CPU 메모리 절약 모드 활성화
        trust_remote_code=True,         # 일부 모델(예: Llama 3)에 필요
        local_files_only=True           # 로컬 파일만 사용하도록 강제 (Repo id 에러 해결)
    )
    model.config.use_cache = False # 학습 중 캐시 비활성화 (메모리 절약)

    tokenizer = AutoTokenizer.from_pretrained(
        base_model_local_path,
        trust_remote_code=True,
        local_files_only=True           # 토크나이저도 로컬 파일만 사용하도록 강제
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token # 패딩 토큰 설정 (모델에 따라 필요)
    tokenizer.padding_side = "right" # 패딩 방향 설정 (오른쪽 패딩)

    logger.info("모델과 토크나이저 로드 성공.")

except Exception as e:
    logger.error(f"\n--- 오류: 모델 또는 토크나이저 로드 중 오류 발생 ---")
    logger.error(f"원인: {e}")
    logger.error(f"'{base_model_local_path}' 경로에 모델 파일이 완전히 존재하는지, PyTorch/Transformers 설치가 올바른지 확인하세요.")
    logger.error("\n--- 추가 문제 해결 팁 ---")
    logger.error("1. Mac의 다른 모든 애플리케이션을 종료하여 통합 메모리를 최대한 확보하세요.")
    logger.error("2. 모델 파일이 손상되었거나 불완전하게 다운로드되었을 수 있으니, 다시 다운로드해보세요.")
    logger.error("3. `base_model_local_path`를 `EleutherAI/gpt-neo-125M` 같은 훨씬 작은 모델로 변경하여 스크립트가 작동하는지 테스트해 보세요.")
    exit(1)

# --- 3. 데이터셋 로드 및 전처리 ---
logger.info(f"데이터셋 로드 중: {sft_json_path}...")
try:
    with open(sft_json_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    dataset = Dataset.from_list(raw_data)
    logger.info(f"데이터셋 로드 성공. 총 {len(dataset)}개의 샘플을 학습합니다.")
except FileNotFoundError:
    logger.error(f"오류: {sft_json_path} 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
    exit(1)
except json.JSONDecodeError:
    logger.error(f"오류: {sft_json_path} 파일이 유효한 JSON 형식이 아닙니다. JSON 포맷을 확인해주세요.")
    exit(1)
except Exception as e:
    logger.error(f"데이터셋 로드 중 오류 발생: {e}")
    exit(1)

# --- 4. LoRA 설정 ---
# LoRA는 적은 수의 파라미터만 학습하여 메모리 사용량을 최소화하면서 파인튜닝을 가능하게 한다.
peft_config = LoraConfig(
    lora_alpha=16,          # LoRA 스케일링 팩터 (높을수록 학습 가중치가 원본 모델에 더 많이 적용)
    lora_dropout=0.1,       # LoRA 레이어에 적용할 드롭아웃 비율
    r=64,                   # LoRA 행렬의 랭크 (낮을수록 메모리 절약, 높을수록 표현력 증가)
    bias="none",            # 바이어스 학습 여부
    task_type="CAUSAL_LM",  # 모델의 태스크 유형: 인과적 언어 모델링 (GPT 계열)
    # LoRA를 적용할 모델의 특정 모듈 지정 (일반적으로 q, k, v 프로젝션은 필수, 다른 모듈 추가 시 성능 향상 가능성)
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
)

# --- 5. 모델 준비 (LoRA 적용) ---
model = get_peft_model(model, peft_config)
model.print_trainable_parameters() # 학습 가능한 파라미터 수 확인
logger.info("LoRA 어댑터가 모델에 성공적으로 적용되었습니다.")

# --- 6. 학습 인자 설정 ---
# M2 Pro 16GB 램 환경에 최적화된 학습 파라미터 설정
sft_training_args = SFTConfig(
    output_dir=output_dir,                  # 파인튜닝 결과 저장 경로
    num_train_epochs=1,                     # 총 학습 에포크 수 (1 에포크로 시작)
    per_device_train_batch_size=1,          # 디바이스당 학습 배치 사이즈 (메모리 절약을 위해 최소값 1로 설정)
    gradient_accumulation_steps=4,          # 그래디언트 누적 스텝 (실제 배치 사이즈 = per_device_train_batch_size * gradient_accumulation_steps = 1 * 4 = 4 효과)
    optim="adamw_torch",                    # 옵티마이저 (AdamW는 일반적으로 좋은 성능을 보여줌)
    learning_rate=2e-4,                     # 학습률
    lr_scheduler_type="cosine",             # 학습률 스케줄러 (cosine은 안정적인 학습에 도움)
    save_steps=50,                          # 50 스텝마다 체크포인트 저장
    logging_steps=10,                       # 10 스텝마다 로그 출력
    push_to_hub=False,                      # 학습 완료 후 Hugging Face Hub에 푸시 안 함
    report_to="none",                       # 학습 진행 상황 리포트 기능 사용 안 함
    fp16=False,                             # 학습도 float16 정밀도로 진행하여 메모리 절약
    bf16=False,                             # bfloat16은 대부분의 Mac에서 지원하지 않음
    max_grad_norm=0.3,                      # 그래디언트 클리핑 (그래디언트 폭발 방지)
    warmup_ratio=0.03,                      # 웜업 비율 (학습 초기 안정화에 도움)
    group_by_length=True,                   # 비슷한 길이의 시퀀스를 묶어 패딩을 최소화 (메모리 및 속도 개선)
    disable_tqdm=False,                     # tqdm 진행바 사용 활성화
    max_seq_length=256,                     # 시퀀스 길이를 256 토큰으로 제한하여 메모리 사용량 낮춤 (필요시 128로 더 줄일 수 있음)
    dataset_text_field="text",              # 데이터셋에서 텍스트 데이터가 있는 필드 이름
    packing=False,                          # 데이터셋 패킹 비활성화 (간단한 데이터셋에 적합)
)

# --- 7. SFTTrainer 설정 및 학습 시작 ---
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    args=sft_training_args,
    # tokenizer=tokenizer, # 토크나이저를 명시적으로 전달.
)

logger.info("\n--- 파인튜닝 시작 ---")
try:
    trainer.train()
    logger.info("\n--- 파인튜닝 완료 ---")
except Exception as e:
    logger.error(f"\n--- 오류: 파인튜닝 중 오류 발생 ---")
    logger.error(f"원인: {e}")
    logger.error("메모리 부족, 학습 인자 설정 오류 등을 확인하세요. `gradient_accumulation_steps`를 늘리거나 `max_seq_length`를 줄여보세요.")
    exit(1)


# --- 8. 파인튜닝된 LoRA 어댑터와 토크나이저 저장 ---
# SFTTrainer는 학습이 끝나면 자동으로 output_dir에 저장하지만, 명시적으로 다시 저장하는 것은 안전하다.
trainer.model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
logger.info(f"\n파인튜닝된 LoRA 어댑터와 토크나이저가 '{output_dir}'에 저장되었습니다.")


# --- 9. LoRA 어댑터를 기본 모델에 병합 및 전체 모델 저장 (GGUF 변환을 위해) ---
logger.info("\nLoRA 어댑터를 기본 모델에 병합 중 (GGUF 변환 준비)...")

try:
    # 병합할 때도 기본 모델을 로드할 때 `torch_dtype`을 `float16`으로 일치시킴.
    base_model_full = AutoModelForCausalLM.from_pretrained(
        base_model_local_path,
        return_dict=True,
        torch_dtype=torch.float16, # float16으로 통일하여 메모리 절약
        device_map="auto",
        low_cpu_mem_usage=True, # 병합 시에도 CPU 메모리 절약 활성화
        local_files_only=True   # 로컬 파일만 사용하도록 강제합니다!
    )

    # 파인튜닝된 LoRA 어댑터를 기본 모델에 로드
    model_to_merge = PeftModel.from_pretrained(base_model_full, output_dir)
    merged_model = model_to_merge.merge_and_unload() # LoRA 가중치를 기본 모델에 병합하여 하나의 완전한 모델 생성

    merged_model_save_path = os.path.join(output_dir, "merged_model")
    merged_model.save_pretrained(merged_model_save_path, safe_serialization=True)
    tokenizer.save_pretrained(merged_model_save_path) # 병합된 모델과 토크나이저 함께 저장

    logger.info(f"\n병합된 모델이 '{merged_model_save_path}'에 저장되었습니다. 이제 GGUF로 변환할 수 있습니다.")

except Exception as e:
    logger.error(f"\n--- 오류: LoRA 어댑터 병합 중 오류 발생 ---")
    logger.error(f"원인: {e}")
    logger.error(f"'{base_model_local_path}' 경로의 기본 모델 파일이 온전한지, 그리고 Mac에 충분한 메모리가 있는지 확인하세요.")
    exit(1)


# --- 10. GGUF 변환 (llama.cpp의 convert_hf_to_gguf.py 사용) ---
convert_py_path = os.path.join(llama_cpp_path, "convert_hf_to_gguf.py")

if not os.path.exists(convert_py_path):
    logger.warning(f"\n경고: '{convert_py_path}'를 찾을 수 없습니다.")
    logger.warning("GGUF 변환을 위해서는 llama.cpp 레포지토리와 해당 스크립트가 필요합니다. 위의 '스크립트 실행 전 필수 확인 사항'을 다시 확인하세요.")
    exit(1)
else:
    logger.info(f"\nGGUF 변환 시작: {gguf_output_path}...")
    # GGUF 변환 시에도 메모리 절약을 위해 `--outtype F16`을 권장.
    # F32는 파일 크기가 매우 크고 추론 시 더 많은 메모리를 요구함.
    convert_command = [
        "python", convert_py_path,
        merged_model_save_path, # 병합된 모델 경로 사용
        "--outfile", gguf_output_path,
        "--outtype", "f16" # GGUF 파일도 F16 정밀도로 변환 (메모리 절약)
    ]
    logger.info(f"실행 명령: {' '.join(convert_command)}")

    try:
        # subprocess.run을 shell=True 없이 리스트 형태로 사용 (더 안전함)
        process = subprocess.run(convert_command, check=True, capture_output=True, text=True)
        logger.info("GGUF 변환 출력:")
        logger.info(process.stdout)
        if process.stderr:
            logger.warning("GGUF 변환 경고/오류 (있는 경우):")
            logger.warning(process.stderr)

    except subprocess.CalledProcessError as e:
        logger.error(f"\n--- 오류: GGUF 변환 중 오류 발생 ---")
        logger.error(f"명령어: {' '.join(e.cmd)}")
        logger.error(f"반환 코드: {e.returncode}")
        logger.error(f"stdout: {e.stdout}")
        logger.error(f"stderr: {e.stderr}")
        logger.error("llama.cpp가 빌드되었고, 변환 스크립트 경로가 올바른지 확인하세요.")
        exit(1)
    except FileNotFoundError:
        logger.error(f"\n--- 오류: 'python' 명령어를 찾을 수 없습니다. Python이 PATH에 추가되었는지 확인하세요. ---")
        exit(1)
    except Exception as e:
        logger.error(f"\n--- 예상치 못한 오류: {e} ---")
        exit(1)

    if os.path.exists(gguf_output_path):
        logger.info(f"\n--- 성공: 파인튜닝된 GGUF 모델이 '{gguf_output_path}'에 생성되었습니다. ---")
        logger.info("이제 이 GGUF 파일을 사용하여 Ollama에 모델을 등록하고 실행할 수 있습니다.")
        logger.info("\n--- 다음 단계 ---")
        logger.info(f"1. Ollama bash 스크립트 또는 Modelfile에서 `GGUF_MODEL_PATH`가 '{gguf_output_path}'를 정확히 가리키는지 확인하세요.")
        logger.info("2. Ollama bash 스크립트를 다시 실행하거나 `ollama create` 명령어를 사용하여 모델을 등록하고 실행하세요.")
    else:
        logger.error("\n--- 오류: GGUF 모델 생성에 실패했습니다. llama.cpp 변환 과정을 다시 확인해주세요. ---")
        exit(1)
