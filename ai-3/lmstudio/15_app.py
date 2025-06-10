import lmstudio as lms

def does_chat_fit_in_context(model: lms.LLM, chat: lms.Chat) -> bool:
    formatted = model.apply_prompt_template(chat)
    token_count = len(model.tokenize(formatted))
    context_length = model.get_context_length()
    print(f'Token Count : {token_count}, Context Length : {context_length}')
    return token_count < context_length

model = lms.llm()

chat = lms.Chat_from_history({
    "messages" : [
        {"role": "system", "content": "You are a resident AI philosopher."},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
})

print("Fit in Context : ", does_chat_fit_in_context(model, chat))
