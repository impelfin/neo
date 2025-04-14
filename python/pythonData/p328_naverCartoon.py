import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)

weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일',
                'thu': '목요일', 'fri': '금요일', 'sat': '토요일',
                'sun': '일요일'}
myfolder = './imsi'

try:
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)
    for mydir in weekday_dict.values():
        mypath = myfolder + mydir
        if os.path.exists(mypath):
            pass
        else:
            os.mkdir(mypath)
except FileExistsError as err:
    pass

def saveFile(mysrc, myweekday, mytitle):
    image_file = urlopen(mysrc)
    filename = myfolder + myweekday + '\\' + mytitle + '.jpg'
    myfile = open(filename, mode='wb')
    myfile.write(image_file.read())

mylist = []

mytarget = soup.find_all('div', attrs={'class': 'thumb'})
print('만화 총 개수 : %d' % (len(mytarget)))

for abcd in mytarget:
    myhref = abcd.find('a').attrs['href']
    myhref = myhref.replace('./webtoon/list.nhn?', '')
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    myweekday = weekday_dict[myweekday]

    imgtag = abcd.find('img')
    mysrc = imgtag.attrs['src']
    mytitle = imgtag.attrs['title'].strip()
    mytitle = mytitle.replace('?', '').replace(':', '')

    mytuple = tuple([mytitleid, myweekday, mytitle, mysrc])
    mylist.append(mytuple)

    saveFile(mysrc, myweekday, mytitle)

print(mylist)

myframe = DataFrame(mylist, columns=['타이틀 번호', '요일', '제목', '링크'])
filename = 'cartoon.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print(filename, ' saved....')
print('\n# finished.')
