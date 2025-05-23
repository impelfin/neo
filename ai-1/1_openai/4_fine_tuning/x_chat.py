from openai import OpenAI
client = OpenAI()

while(1):
    prompt = input("Moon : ")
    if prompt == 'quit' or prompt == 'q' or prompt == 'exit' or prompt == 'ㅂ':
        break
    else:
        response = client.chat.completions.create(
            model = 'ft:gpt-3.5-turbo-0125:personal::BaH5ssr3',
            messages = [
            {'role': 'user', 'content': prompt}
        ]
    )

    print("Javis : " + response.choices[0].message.content.strip())
    print()