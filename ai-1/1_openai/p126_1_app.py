import openai

prompt = '''아래 문장을 짧은 한 문장으로 요약해주세요.
    OpenAI는 영리법인 OpenAI LP와 그 모회사인 비영리법인 OpenAI Inc.로 구성된 인공지능 연구소입니다. 2015년 말에 샘 알트만과 일론 머스크 등이 샌프란시스코에서 설립했습니다. 인류 전체에 도움이 되는 방식으로 친근한 인공지능을 보급하고 발전시키는 것을 목표로 삼고 있습니다.
'''

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0,
    max_tokens=150
)
print(response.choices[0].text)
