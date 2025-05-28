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
print(type(python_dict))
print(python_dict)