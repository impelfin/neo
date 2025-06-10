import lmstudio as lms

model = lms.llm()

tokens = model.tokenize('Hello World!')

print(tokens)
