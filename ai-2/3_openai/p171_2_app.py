import openai 
import json

def get_price_info(product_name):
    product_price = {"키보드" : "3만원", "마우스" : "2만원", "모니터" : "30만원"}

    price = product_price.get(product_name)
    if price is None:
        price = "해당 상품은 가격 정보가 없습니다."

    price_info = {
        "product_name": product_name,
        "price": price
    }

    return json.dumps(price_info)

def run_conversation(user_query):
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

    ## Step 1
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call="auto",
    )

    response_message = response.choices[0].message

    ## Step 2
    response_message = response.choices[0].message

    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]
        
        function_args = json.loads(response_message["function_call"]["arguments"])
        
        function_response = get_price_info(
            product_name=function_args.get("product_name")
        )

        messages.append(response_message)

        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )

        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        return second_response

    return response

user_query = "마우스의 가격은 얼마인가요?"
response = run_conversation(user_query)
print(json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False))
print('-' * 50)

user_query = "HDD의 가격은 얼마인가요?"
response = run_conversation(user_query)
print(json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False))
print('-' * 50)
