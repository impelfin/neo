from langchain.prompts import PromptTemplate

no_input_prompt = PromptTemplate(
    input_variables = ["adjective", "content"],
    template = "{adjective} {content}이라고 하면?"
)

print(no_input_prompt.format(adjective="멋진", content="동물"))