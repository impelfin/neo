import readline
from pathlib import Path

import lmstudio as lms

def create_file(name:str, content:str):
    dest_path = Path(name)
    if dest_path.exists():
        return "Error : File already exists"
    try:
        dest_path.write_text(content, encoding="utf-8")
    except Exception as e:
        return f"Error : {e!r}"
    return f"File created : {name}"

def print_fragment(fragment, round_index=0):
    print(fragment, end='', flush=True)

model = lms.llm()
chat = lms.Chat("Your are a task focused AI assistant.")

while True:
    try:
        user_input = input("You (leave blank to exit) : ")
    except EOFError:
        print()
        break

    if not user_input:
        break

    chat.add_user_message(user_input)
    print("AI : ", end='', flush=True)
    model.act(
        chat, 
        [create_file],
        on_message=chat.append,
        on_prediction_fragment=print_fragment
    )
    print()
