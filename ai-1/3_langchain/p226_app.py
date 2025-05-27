from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import PromptTemplate

examples = [
    {"input": "明るい", "output": "暗い"},
    {"input": "おもしろい", "output": "つまらない"},
]

example_prompt = PromptTemplate(
    input_variables = ["input", "output"],
    template = "入力: {input}\n出力: {output}",
)

prompt_from_string_examples = FewShotPromptTemplate(
    examples = examples,
    example_prompt = example_prompt,
    prefix = "모든 입력에 대한 반의어를 입력하세요.",
    suffix = "입력 : {adjective}\n출력 : ",
    input_variables = ["adjective"],
    example_separator = "\n\n",
)

print(prompt_from_string_examples.format(adjective="큰"))