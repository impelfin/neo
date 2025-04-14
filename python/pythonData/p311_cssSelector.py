import re
from bs4 import BeautifulSoup

myencodig = 'utf-8'
myparser = 'html.parser'
filename = 'css01.html'

html = open(filename, encoding=myencodig)
soup = BeautifulSoup(html, myparser)

h1 = soup.select_one('div#cartoon > h1').string
print("h1 = ", h1)
print("-" * 50)

li_list = soup.select('div#cartoon > ul.elements > li')
for li in li_list:
    print(li.string)
print("-" * 50)

choice =  lambda x : print (soup.select_one(x).string)

print('\nchice("#item5) : ', end='')
choice('#item5')

print('\nchice("#item4) : ', end='')
choice('#item4')

print('\nchoice("ul > li#item3") : ', end='')
choice('ul > li#item3')

print('\nchoice("li[id=\'item1\']") : ', end='') 
choice('li[id=\'item1\']')

print('\nchoice("li:nth-of-type(4)") : ', end='')
choice('li:nth-of-type(4)')

print('\nchoice("li")[1].string : ', end='')
print(soup.select('li')[1].string)

print('\nchoice("li")[3].string : ', end='')
print(soup.select('li')[3].string)
print('-' * 50)

mytag = soup.select_one('div#cartoon > ul.elements')
mystring = mytag.select_one('li:nth-of-type(3)').string
print(mystring)
print('-' * 50)

mytag = soup.select_one('ul#itemlist')
mystring = mytag.select_one('li:nth-of-type(4)').string
print(mystring)
print('-' * 50)

print(soup.select("#vegetables > li[class='us']")[0].string)
print(soup.select("#vegetables > li.us")[1].string)
print('-' * 50)

result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])
    print(item.string)
print('-' * 50)

result = soup.select('a[href*="daum"]')
for item in result:
    print(item['href'])
    print(item.string)
print('-' * 50)

cond = {"id":"ko", "class":"cn"}
print(soup.find("li", cond).string)
print('-' * 50)

print(soup.find(id="vegetables").find("li", cond).string)
print('-' * 50)

print("# 정규 표현식으로 href에서 https인 것을 추출")
li = soup.find_all(href=re.compile(r"^https://"))

for e in li:
    print(e['href'])
print('-' * 50)

print(soup.select("#fruits > li")[0].string)
print('-' * 50)

mytag = soup.select_one('ul#fruits')
mystring = mytag.select_one("li:nth-of-type(2)").string
print(mystring)
print('-' * 50)
