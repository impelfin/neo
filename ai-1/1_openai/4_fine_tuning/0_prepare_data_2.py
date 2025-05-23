import os
import json

input_directory = './archive'

output_file = './output_2.jsonl'

def process_json_files(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(input_dir):
            for filename in files:
                if filename.endswith('.json'):
                    filepath = os.path.join(root, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as json_file:
                            data = json.load(json_file)
                            transformed_data = transform_json(data)
                            for message_pair in transformed_data:
                                json.dump(message_pair, out_file, ensure_ascii=False)
                                out_file.write('\n')
                    except Exception as e:
                        print(f"Error processing {filepath}: {e}")

def transform_json(data):
    messages = []
    if 'utterances' in data:
        utterances = data['utterances']
        for i in range(0, len(utterances), 2):
            if i + 1 < len(utterances):
                message1 = {
                    "role": "user",
                    "content": utterances[i]['text']
                }
                message2 = {
                    "role": "assistant",
                    "content": utterances[i+1]['text']
                }
                messages.append({"messages": [message1, message2]})
        return messages
    else:
        raise ValueError("'utterances' key found in the input JSON")

process_json_files(input_directory, output_file)
