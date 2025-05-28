import json

python_dict = {
    "이름" : "홍길동",
    "나이" : 25,
    "지역" : "서울",
    "신체정보" : {
        "키" : 180,
        "몸무게" : 72
    },
    "취미":[
        "등산",
        "자건거 타기",
        "독서"
    ]
}

print('-' * 50)
json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(type(json_data))

dict_data = json.loads(json_data)
print(type(dict_data))
print(dict_data['신체정보']['키'])
