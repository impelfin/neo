import openai

prompt = '인공지능에 대해 알려주세요.'

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0.7,
    max_tokens=100
)
print(response.choices[0].text)
