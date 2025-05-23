from openai import OpenAI 
client = OpenAI()

training_file = client.files.create(file=open("tsukuyomi_new.jsonl", "rb"),
    purpose='fine-tune')

print("Uploaded file ID:", training_file.id)

response = client.fine_tuning.jobs.create(training_file=training_file.id,
    model='gpt-3.5-turbo')

print(response)