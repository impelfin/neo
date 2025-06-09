import os
import json

def create_sft_json(input_directory="training_data", output_file="sft.json"):
    sft_data = []

    if not os.path.isdir(input_directory):
        print(f"오류: 입력 디렉토리 '{input_directory}'를 찾을 수 없습니다.")
        return

    for filename in os.listdir(input_directory):
        if filename.endswith(".json"):
            filepath = os.path.join(input_directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if "data_info" in data and isinstance(data["data_info"], list):
                        for item in data["data_info"]:
                            if "contents" in item:
                                sft_data.append({"text": item["contents"]})
                            else:
                                print(f"경고: {filename}의 항목에서 'contents' 키를 찾을 수 없습니다.")
                    else:
                        print(f"경고: {filename}에서 'data_info' 리스트를 찾을 수 없거나 형식이 잘못되었습니다.")
            except json.JSONDecodeError:
                print(f"오류: {filename}에서 JSON 디코딩에 실패했습니다. 건너뜁니다.")
            except Exception as e:
                print(f"{filename} 처리 중 예상치 못한 오류가 발생했습니다: {e}")

    if not sft_data:
        print(f"추출된 내용이 없습니다. 입력 디렉토리와 파일 구조를 확인해주세요.")
        return

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(sft_data, outfile, ensure_ascii=False, indent=2)

    print(f"'{output_file}' 파일이 {len(sft_data)}개의 항목으로 성공적으로 생성되었습니다.")

create_sft_json()