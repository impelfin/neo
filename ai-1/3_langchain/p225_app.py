from langchain.prompts import PromptTemplate

jinja2_prompt = PromptTemplate(
    input_variables = ["items"],
    template_format = "jinja2",
    template = """
    {% for item in items %}
    Q : {{ item.qestion }}
    A : {{ item.answer }}
    {% endfor %}
    """
)

items = [
    {"qestion" : "foo", "answer" : "bar"},
    {"qestion" : "1", "answer" : "2"},
]

print(jinja2_prompt.format(items=items))