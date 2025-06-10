import lmstudio as lms

model = lms.llm()

print(model.get_info())
print('-' * 50)

print(model.get_context_length())
print('-' * 50)

print(model.get_load_config())
print('-' * 50)