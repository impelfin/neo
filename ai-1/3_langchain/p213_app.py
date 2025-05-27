from langchain.llms import OpenAI

llm=OpenAI(
    model = 'gpt-3.5-turbo-instruct', 
    temperature = 0.9,
)

result = llm("고양이의 울음소리는?")
print('-' * 50)
print(result)

result = llm.generate(["고양이의 울음소리는?", "까마귀 울음소리는?"]) 
print('-' * 50)
print("resutl 0 : ", result.generations[0][0].text)
print("resutl 1 : ", result.generations[1][0].text)
print("llm output : ", result.llm_output)