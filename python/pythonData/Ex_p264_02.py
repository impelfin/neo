import re

mylist = ['ab123', 'cd4#6', 'cf79a', 'abc1']

regex = '^[a,c]\w{4}'
pattern = re.compile(regex)

print('# 문자 a, c로 시작하고, 이후에 숫자나 알파벳이 4개로 끝나는 패턴')
totallist = []
for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
    else:
        print(item, '은(는) 조건에 부적합')

print('\n# 조건에 적합한 항목들')
print(totallist)