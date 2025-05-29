import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

text_file_name = "./스티브_잡스_2005_스탠포드_연설.txt"

with open(text_file_name, "r", encoding="utf-8") as f:
    text_data = f.read()

print("[원본 텍스트 파일의 내용 앞부분만 출력]")
print(text_data[:290], end="\n\n")

api_url = "https://kagi.com/api/v0/summarize"
headers = {"Authorization": "Bot " + KAGI_API_KEY}
data = {"text": text_data, "target_language": "KO"}

response = requests.post(api_url, headers=headers, data=data)

summary = response.json()['data']['output']
short_summary = textwrap.shorten(summary, width=250, placeholder=' [...이하 생략...]')
print("- 요약 내용(축약) : ", short_summary)

