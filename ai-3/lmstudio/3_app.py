import lmstudio as lms

model = lms.llm()
chat = lms.Chat("You are a task focused AI assistant.")

while True:
    try:
        user_input = input("You (leave blank to exit) : ")
    except EOFError:
        print()
        break

    if not user_input:
        break

    chat.add_user_message(user_input)
    prediction_stream = model.respond_stream(
        chat, 
        on_message=chat.append,
    )

    print("AI : ", end='', flush=True)

    for fragment in prediction_stream:
        print(fragment.content, end='', flush=True)
    print()