import langchain
from langchain.cache import InMemoryCache
from langchain.llms import OpenAI

llm = OpenAI(
    model = 'gpt-3.5-turbo-instruct', 
    temperature = 0,
)

langchain.llm_cache = InMemoryCache()

print(llm.generate(["하늘의 색깔은?"]))

print(llm.generate(["하늘의 색깔은?"]))