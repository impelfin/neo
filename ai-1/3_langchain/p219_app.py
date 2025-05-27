import time
from langchain.llms import OpenAI

def generate_serially():
    llm = OpenAI(
        model = 'gpt-3.5-turbo-instruct', 
        temperature = 0.9,
    )
    for _ in range(10):
        res = llm.generate(["안녕하세요!"])
        print(res.generations[0][0].text)

s = time.perf_counter()

generate_serially()

elapsed = time.perf_counter() - s
print(f"Generated in {elapsed:0.2f} seconds")