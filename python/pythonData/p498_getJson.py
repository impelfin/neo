import json

def get_Json_data():
    filename = 'jumsu.json'
    myfile = open(filename, 'r', encoding='utf-8')
    print(type(myfile))
    print(myfile)
    print('-' * 50)
    
    myfile = myfile.read()
    print(type(myfile))
    print(myfile)
    print('-' * 50)
    
    jsondata = json.loads(myfile)
    print(type(jsondata))
    print(jsondata)
    print('-' * 50)

    for oneitem in jsondata:
        print(oneitem.keys())
        print(oneitem.values())
        print('-' * 50)
        kor = float(oneitem['kor']) 
        eng = float(oneitem['eng']) 
        math = float(oneitem['math'])
        total = kor + eng + math
        print('국어 : ', kor)
        print('영어 : ', eng)
        print('수학 : ', math)
        print('총점 : ', total)
        print('-' * 50)

        if 'hello' in oneitem.keys():
            message = oneitem['hello']
            print('message : ', message)

        _gender = oneitem['gender'].upper()

        if _gender == 'M':
            print('성별 : ', _gender)
        elif _gender == 'F':
            print('성별 : ', _gender)
        else:
            print('성별 정보가 없습니다.')
    print('-' * 50)
    
if __name__ == '__main__':
    get_Json_data()