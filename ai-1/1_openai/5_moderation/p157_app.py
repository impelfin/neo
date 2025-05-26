import openai

response = openai.Moderation.create(
    input='I want to kill you.'
)
print(response)