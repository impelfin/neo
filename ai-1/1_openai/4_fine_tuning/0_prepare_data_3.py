import json
import os

dir_path = "./archive"

file_paths=[]
jsonl_data = []

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    
print(file_paths)

for file_path in file_paths:

    print(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    messages = data['utterances']

    for i in range(0, len(messages), 2):
        user_message = messages[i]

        assistant_message = messages[i + 1] if i + 1 < len(messages) else {"role": "assistant", "text": ""}

        jsonl_data.append({
            "messages": [
                {"role": "user", "content": user_message['text']},
                {"role": "assistant", "content": assistant_message['text']}
            ]
        })

output_path = 'output_3.jsonl'
with open(output_path, 'w', encoding='utf-8') as output_file:
    for entry in jsonl_data:
        output_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Conversion complete. Output saved to {output_path}")
