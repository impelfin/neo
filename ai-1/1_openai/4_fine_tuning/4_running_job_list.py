from openai import OpenAI 
client = OpenAI()

fine_tunes = client.fine_tuning.jobs.list()

for fine_tune in fine_tunes.data:
    if fine_tune.status == 'running':
        print(f'running fine-tuning job: {fine_tune.id}')
        print(f'fine-tuning training_file : {fine_tune.training_file}')
