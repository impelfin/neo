#!/bin/bash

# --- 설정 변수 ---
MODEL_DIR="finetuned-llama3.2-1b"
GGUF_MODEL_NAME="llama3.2-1b-finetuned.gguf"
GGUF_MODEL_PATH="./${MODEL_DIR}/${GGUF_MODEL_NAME}"

# Ollama에 등록할 모델의 이름
OLLAMA_MODEL_TAG="llama3.2-1b-finetuned"

# 데이터셋 파일의 경로 (참고용. Ollama 등록 시 직접 사용되지 않음)
DATASET_PATH="./sft.json"

# --- Modelfile 내용 생성 ---
MODELFILE_PATH="${MODEL_DIR}/Finetuned_ModelFile"

echo "FROM ${GGUF_MODEL_NAME}" > "${MODELFILE_PATH}"
echo "" >> "${MODELFILE_PATH}"
echo "SYSTEM \"\"\"" >> "${MODELFILE_PATH}"
echo "당신은 사용자에게 도움이 되는 친절한 AI 어시스턴트입니다." >> "${MODELFILE_PATH}"
echo "사용자의 질문에 training_data/srf.json 데이터셋에 학습된 방식으로 답변해 주세요." >> "${MODELFILE_PATH}"
echo "\"\"\"" >> "${MODELFILE_PATH}"
echo "" >> "${MODELFILE_PATH}"
echo "# 모델의 동작을 조절하는 파라미터 (선택 사항, 필요에 따라 주석 해제 및 값 조정)" >> "${MODELFILE_PATH}"
echo "# PARAMETER temperature 0.7" >> "${MODELFILE_PATH}"
echo "# PARAMETER top_k 40" >> "${MODELFILE_PATH}"
echo "# PARAMETER top_p 0.9" >> "${MODELFILE_PATH}"
echo "# PARAMETER num_gpu 1" >> "${MODELFILE_PATH}" 

echo "---"
echo "Modelfile이 ${MODELFILE_PATH} 에 생성되었습니다."
echo "내용:"
cat "${MODELFILE_PATH}"
echo "---"

# --- 모델 등록 (ollama create) ---
echo "Ollama에 모델 등록 중: ${OLLAMA_MODEL_TAG} (FROM ${GGUF_MODEL_PATH})"
(cd "${MODEL_DIR}" && ollama create "${OLLAMA_MODEL_TAG}" -f "${MODELFILE_PATH}")

if [ $? -eq 0 ]; then
    echo "---"
    echo "모델 '${OLLAMA_MODEL_TAG}'이(가) 성공적으로 Ollama에 등록되었습니다."
    echo "이제 이 모델을 실행할 수 있습니다."
    echo ""
    echo "--- 모델 실행 명령 ---"
    echo "ollama run ${OLLAMA_MODEL_TAG}"
    echo "---"
    echo "데이터셋 ${DATASET_PATH} 은(는) 이미 모델 학습에 사용되었음을 가정합니다."
    echo "Ollama는 이 GGUF 모델을 로드하여 실행만 합니다."
else
    echo "---"
    echo "오류: Ollama 모델 등록에 실패했습니다."
    echo "다음 사항을 확인하세요:"
    echo "1. Ollama가 실행 중인지 확인하세요."
    echo "2. '${GGUF_MODEL_PATH}' 경로에 GGUF 파일이 실제로 존재하는지 확인하세요."
    echo "3. Modelfile 내용에 오류가 없는지 확인하세요."
    echo "---"
    exit 1
fi

# --- 모델 실행 (ollama run) ---
echo "모델 '${OLLAMA_MODEL_TAG}' 실행 중..."
ollama run "${OLLAMA_MODEL_TAG}"
