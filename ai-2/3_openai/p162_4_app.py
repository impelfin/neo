import openai 
import json

messages = [
    {"role": "user", "content": "한글은 언제 만들어졌나요?"},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=100,
    temperature=0.7,
    n = 2
)

print("응답 개수 : ", len(response['choices']))
print("-" * 50)
for c in response['choices']:
    print("응답 : ", c['message']['content'])
    print("-" * 50)