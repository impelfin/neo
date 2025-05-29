import deepl
import os

auth_key = os.environ["DEEPL_AUTH_KEY"]
translator = deepl.Translator(auth_key)

text = "But"
result = translator.translate_text(
    text,
    target_lang="KO"
)

print("- 감지된 언어 코드 : ", result.detected_source_lang)
print("- 번역 결과 : ", result.text)