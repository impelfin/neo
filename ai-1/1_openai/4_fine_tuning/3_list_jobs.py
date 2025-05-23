from openai import OpenAI 
client = OpenAI()

response = client.fine_tuning.jobs.list()
print(response)