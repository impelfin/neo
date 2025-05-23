import openai 

prefix_prompt = """def helloworld():
    '''
    설명: """
suffix_prompt = """
    '''

    print("Hello World!")

helloworld()
"""

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prefix_prompt,
    suffix=suffix_prompt,
    temperature=0.7,
    max_tokens=200
)

print(response.choices[0].text)