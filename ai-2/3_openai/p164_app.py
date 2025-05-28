import openai 
import textwrap

def response_from_ChatAI(user_content, r_num = 1):
    messages = [
        {"role": "user", "content": user_content},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.8,
        n = r_num
    )

    assistant_replies = []

    for choice in response['choices']:
        assistant_replies.append(choice['message']['content'])

    return assistant_replies

resps = response_from_ChatAI("ChatGPT는 무엇인가요?", 2)

for resp in resps:
    shorten_resp = textwrap.shorten(resp, width=100, placeholder="[...이하 생략...]")
    print(shorten_resp, end="\n\n")