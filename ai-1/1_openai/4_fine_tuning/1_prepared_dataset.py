import pandas as pd
import json

df = pd.read_csv(
    'tsukuyomi.csv',
    usecols=[1,2],
    names=['prompt', 'completion'],
    skiprows=2
)
df.to_json(
    'tsukuyomi.jsonl',
    orient='records',
    lines=True,
    force_ascii=False
)

def convert_to_new_format(old_data):
    new_data = []
    for entry in old_data:
        new_entry = {
            "messages" : [
                {"role": "user", "content": entry["prompt"]},
                {"role": "assistant", "content": entry["completion"]}   
            ]
        }
        new_data.append(new_entry)
    return new_data

old_data = []
with open('tsukuyomi.jsonl', 'r') as f:
    for line in f:
        old_data.append(json.loads(line))

converted_data = convert_to_new_format(old_data)

with open('tsukuyomi_new.jsonl', 'w') as f:
    for entry in converted_data:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')