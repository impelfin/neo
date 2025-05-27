from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables = ["product"],
    template = "{product}을 만드는 새로운 회사이름을 하나 제안해주세요."
)

print(prompt.format(product="컴퓨터 게임"))