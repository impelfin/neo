import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.find_all('div', attrs={'class': 'sect-movie-chart'})
# print('-' * 50)
# print(infos)
# print('-' * 50)

mydata0 = [i for i in range(1, 20)]

result = []
title = soup.select("strong.title")
for i in title:
    result.append(i.text)
mydata1 = result
# print(mydata1)

result = []
score = soup.select("span.percent")
for i in score:
    result.append(i.text)
mydata2 = result
# print(mydata2)

result = []
reserv = soup.select("strong.percent")
for i in reserv:
    result.append(i.text.lstrip('예매율'))
mydata3 = result
# print(mydata3)

result = []
release = soup.select("span > strong")
for i in release:
    result.append(i.text.strip()[0:10])
mydata4 = result
# print(mydata4)

mycolumn = ['순위', '제목', '평점', '예매율', '개봉일']

myframe = pd.DataFrame(data = list(zip(mydata0, mydata1, mydata2, mydata3, mydata4)), columns = mycolumn)
myframe = myframe.set_index(keys=['순위'])
print(myframe)
print('-' * 40)

filename = 'quiz_02_cgvMovie.csv'
myframe.to_csv(filename, encoding='utf8', index=False)
print(filename, ' saved...', sep='')
print('finished')

dfmovie = myframe.reindex(columns=['제목', '평점', '예매율'])
print(dfmovie)

mygroup0 = dfmovie['제목']
mygroup1 = dfmovie['평점']
mygroup1 = mygroup1.str.replace('%','')
mygroup1 = mygroup1.str.replace('?','0')
mygroup2 = dfmovie['예매율']
mygroup2 = mygroup2.str.replace('%','')
mygroup2 = mygroup2.str.replace('?','0')

df = pd.concat([mygroup1, mygroup2], axis=1)
df = df.set_index(mygroup0)
df.columns = ['평점', '예매율']
print(df)

df.astype(float).plot(kind='barh', title='영화별 평점과 예매율', rot=0)
filename = 'quiz_02_cgvMovieGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()

