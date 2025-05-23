import openai

messages = [
    {"role":"system", "content":"오타를 수정해주세요."},
    {"role":"user", "content":"오늘은 정말로 즐거워따."},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0
)

print('-' * 50)
print(response['choices'][0]['message']['content'])
