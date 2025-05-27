from langchain.chains import OpenAIModerationChain

chain = OpenAIModerationChain()

text = "This is OK!"
print('User : ' + text)
print('Result : ' + chain.run(text))
print('-' * 50)

text = "I'll kill you"
print('User : ' + text)
print('Result : ' + chain.run(text))
print('-' * 50)

chain = OpenAIModerationChain(
    error = True
)

try:
    text = "I'll kill you"
    print('User : ' + text)
    print('Result : ' + chain.run(text))
except ValueError as err:
    print('문제 발언입니다!!')
    print(err)