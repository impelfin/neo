import pandas as pd
import json
import os

directory_path = './archive'

messages = []

def read_json_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    utterances = data['utterances']
                    for i in range(0, len(utterances) - 1, 2):
                        if utterances[i]['role'] == 'speaker' and utterances[i + 1]['role'] == 'listener':
                            messages.append({
                                'messages': [
                                    {'role': 'user', 'content': utterances[i]['text']},
                                    {'role': 'assistant', 'content': utterances[i + 1]['text']}
                                ]
                            })

read_json_files(directory_path)

df = pd.DataFrame(messages)

output_path = 'output_1.jsonl'
df.to_json(output_path, orient='records', lines=True, force_ascii=False)

print(f"save {output_path}")
