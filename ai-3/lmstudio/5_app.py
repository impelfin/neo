import lmstudio as lms

image_path = '/Users/lune/Pictures/Lune.png'
image_handle = lms.prepare_image(image_path)

model = lms.llm('google/gemma-3-4b')
chat = lms.Chat()

chat.add_user_message("Describe this image please.", images=[image_handle])

prediction = model.respond(chat)

print(prediction)
