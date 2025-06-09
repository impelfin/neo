import lmstudio as lms

model = lms.llm()

response = model.respond(
    'What is LM Studio',
    on_prompt_processing_progress = (lambda progress: print(f'{progress * 100}% complete')),
)

print(response)