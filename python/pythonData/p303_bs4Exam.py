from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('body')
ptag = body.find('p')
print('1번째 p 태그 : ', ptag['class'])
ptag['class'][1] = 'white'
print('1번째 p 태그 : ', ptag['class'])
ptag['id'] = 'apple'
print('-' * 50) 

print('1번째 p 태그의 id 속성 : ', ptag['id'])
print('-' * 50)

body_tag = soup.find('body')
print(body_tag)
print('-' * 50)

idx = 0
print('child 속성으로 하위 항목 보기')
for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 : ', child)
print('-' * 50)

mydiv = soup.find('div')
print(mydiv)
print('-' * 50)

print('div의 부모 태그')
print(mydiv.parent)
print('-' * 50)

mytag = soup.find('p', attrs={'class': 'hard'})
print(mytag)
print('-' * 50)

print('mytag의 부모 태그')
print(mytag.parent)
print('-' * 50)

print('mytag의 모든 상위 부모 태그의 이름은?')
parents = mytag.find_parents()
for p in parents:
    print(p.name)
print('-' * 50)
