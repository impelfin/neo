from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

template = """ 
    Q : {question}    
    A :
"""

prompt = PromptTemplate(
    input_variables = ["question"],
    template = template,
)

llm_chain = LLMChain(
    llm = OpenAI(
        model = 'gpt-3.5-turbo-instruct', 
        temperature = 0,
    ),
    prompt = prompt,
    verbose = True
)

question = "기타를 잘 치는 방법은?"
print(llm_chain.predict(question=question))