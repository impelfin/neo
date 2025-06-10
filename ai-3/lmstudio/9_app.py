import lmstudio as lms
from lmstudio import Chat

model = lms.llm()

chat = Chat("You are a resident AI philosopher.")
chat.add_user_message("What is the meaning of life?")

prediction = model.respond(chat)

print(prediction)
print('-' * 50)

chat = Chat.from_history({
    "messages" : [
        {"role": "system", "content": "You are a resident AI philosopher."},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
})

print(chat)
print('-' * 50)

prediction = model.respond({
    "messages" : [
        {"role": "system", "content": "You are a resident AI philosopher."},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
})

print(prediction)
