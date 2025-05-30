import deepl
from pathlib import Path
import os

def translate_text_file(input_path, target_lang="KO"):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    auth_key = os.environ["DEEPL_AUTH_KEY"]
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=target_lang)

    path = Path(input_path)
    output_file = f"{path.parent}/{path.stem}_번역_{target_lang}{path.suffix}"

    output_path = Path(output_file)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.text)

    return output_path

input_file = "./data/youtube_download.srt"

translated_file = translate_text_file(input_file)
print(f"- [번역 파일] : {translated_file}\n")
