import openai

prompt = '''다음 이야기를 써주세요.
기타를 좋아하지만 컴맹인 여고생이 어떤 계기로 록 밴드에 가입하고, 
낮선 인간관계를 통해 활동하게 되는 이야기.'''

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0.7,
    max_tokens=100
)
print(response.choices[0].text)
print(response)