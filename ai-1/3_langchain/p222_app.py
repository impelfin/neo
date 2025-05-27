from langchain.prompts import PromptTemplate

no_input_prompt = PromptTemplate(
    input_variables = [],
    template = "멋진 동물이라고 하면?"
)

print(no_input_prompt.format())