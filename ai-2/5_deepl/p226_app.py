import deepl
import os

auth_key = os.environ["DEEPL_AUTH_KEY"]
translator = deepl.Translator(auth_key)

input_path = './data/President_Obamas_Farewell_Address_영어_원본.pdf'
output_path = './data/President_Obamas_Farewell_Address_한국어_번역.pdf'

result = translator.translate_document_from_filepath(
    input_path,
    output_path,
    target_lang="KO"
)

print(result.done)