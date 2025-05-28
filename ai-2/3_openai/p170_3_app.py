import openai 
import json

def get_price_info_temp(product_name):
    price_info = {
        "product_name": product_name,
        "price": "10,000"
    }

    return json.dumps(price_info)

def run_conversation_temp(user_query):
    messages = [{"role": "user", "content": user_query}]

    functions = [
        {
            "name": "get_price_info",
            "description": "제품 이름에 따른 가격 가져오기",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "제품 이름. 예를 들면, 키보드, 마우스",
                    },
                },
                "required": ["product_name"],
            }
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call="auto",
    )

    response_message = response.choices[0].message

    return response_message

user_query = "마우스의 가격은 얼마인가요?"
response_message = run_conversation_temp(user_query)
print(json.dumps(response_message, ensure_ascii=False))
print('-' * 50)
print(response_message['function_call']['name'])
print(json.loads(response_message['function_call']['arguments']))
print(json.loads(response_message['function_call']['arguments'])['product_name'])
