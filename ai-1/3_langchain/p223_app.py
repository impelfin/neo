from langchain.prompts import PromptTemplate

no_input_prompt = PromptTemplate(
    input_variables = ["content"],
    template = "멋진 {content}이라고 하면?"
)

print(no_input_prompt.format(content="동물"))