from openai import OpenAI
client = OpenAI()

fine_tunes = client.fine_tuning.jobs.list()

for fine_tune in fine_tunes.data:
    if fine_tune.status == "running" or fine_tune.status == "succeeded":
        print(f'running or succeeded fine-tuning job: {fine_tune.id}')
        fine_tuning_retrieve_job_id = fine_tune.id

response = client.fine_tuning.jobs.retrieve(fine_tuning_retrieve_job_id)

print(response)