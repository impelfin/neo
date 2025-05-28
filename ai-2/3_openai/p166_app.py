import openai 

user_input = input("AI와 채팅할 내용을 입력하세요(종료하려면 end를 입력하세요. \n[나] : ")

messages = [{"role": "user", "content": user_input}]

ai_message = "AI : "

while user_input.lower() != 'end':
    message = [
        {"role": "assistant", "content": ai_message},
        {"role": "user", "content": user_input}
    ]
    messages.extend(message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    ai_message = response.choices[0].message.content
    print(f'[AI] : {ai_message}' + '\n')

    user_input = input("[나] : ")

if(user_input.lower() == 'end'):
    print("AI와 채팅을 종료합니다.")   
