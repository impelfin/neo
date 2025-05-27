import langchain
from langchain.llms import OpenAI

llm = OpenAI(
    model = 'gpt-3.5-turbo-instruct', 
    temperature = 0,
)

langchain.llm_cache = None

print('-' * 50)
print(llm.generate(["오늘 너의 마음을 색깔로 표현해줘."]))
print('-' * 50)
print(llm.generate(["오늘 너의 마음을 색깔로 표현해줘."]))
