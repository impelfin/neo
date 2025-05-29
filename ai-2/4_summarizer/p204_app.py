import requests
import os

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

contents_url = "https://www.youtube.com/watch?v=BmYv8XGl-YU"
url = f'https://kagi.com/api/v0/summarize?url={contents_url}'
headers = {"Authorization": "Bot " + KAGI_API_KEY}

response = requests.get(url, headers=headers)

summary = response.json()['data']['output']
print(summary)