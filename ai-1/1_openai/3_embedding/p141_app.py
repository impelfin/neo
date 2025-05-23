import openai 

text = '이것은 테스트입니다.'

response = openai.Embedding.create(
    input=text,
    model="text-embedding-ada-002"
)

print('-' * 50)
print(len(response['data'][0]['embedding']))
print('-' * 50)
print(response['data'][0]['embedding'])
