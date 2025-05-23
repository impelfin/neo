from openai import OpenAI 
client = OpenAI()

fine_tunes = client.fine_tuning.jobs.list()

for fine_tune in fine_tunes.data:
    if fine_tune.status == 'failed':
        print(f'running fine-tuning job: {fine_tune.id}')
