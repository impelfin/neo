import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

# print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])
# font_location = '/root/.virtualenvs/neo/lib/python3.12/site-packages/matplotlib/mpl-data//fonts/ttf/NanumBarunGothic.ttf'
# font_name = font_manager.FontProperties(fname=font_location).get_name()
# matplotlib.rc('font', family=font_name)
# print(font_name)

plt.rcParams['font.family'] = 'NanumBarunGothic'

theaterfile = 'theater.csv'
colname = ['id', 'theater', 'region', 'bindo']
dftheater = pd.read_csv(theaterfile, names=colname, encoding='utf-8', header=None)
dftheater = dftheater.rename(index=dftheater.id)
dftheater = dftheater.reindex(columns=['theater', 'region', 'bindo'])
dftheater.index.name = 'id'
print('전체 조회')
print(dftheater)
print('-' * 50)

print('극장별 상영 횟수 집계')
mygrouping = dftheater.groupby('theater')['bindo']
sumSeries = mygrouping.sum()
meanSeries = mygrouping.mean()
sizeSeries = mygrouping.size()

print('시리즈 3개를 이용하여 데이터 프레임 생성')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1)
df.columns = ['합계', '평균', '개수']
print(df)
print('-' * 50)

mysize = len(mygrouping.groups)

df.plot(kind='bar', rot=0)
plt.title(str(mysize) + '개 매장 집계 데이터')
filename = 'p280_DataframeGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
# plt.show()

print('집계 함수를 dict에 담아 전달')
print('지역의 개수와 상영 횟수의 총합')
mydict = {'bindo': 'sum', 'region': 'size'}
result = dftheater.groupby('region').agg(mydict)
print(result)
print('-' * 50)

print('print using numpy')
result = mygrouping.agg([np.count_nonzero, np.mean, np.std])
print(result)
print('-' * 50)

def myroot(values):
    mysum = sum(values)
    return sqrt(mysum)

def plus_add(values, somevalue):
    result = myroot(values)
    return result + somevalue

mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용')
result = mygrouping.agg(myroot)
print(result)
print('-' * 50)

print('groupby와 사용자 정의 함수 사용(매개변수 2개 사용)')
result = mygrouping.agg(plus_add, somevalue=3)
print(result)
print('-' * 50)

print('columns 2개 이상을 그룹핑하기')
newgrouping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgrouping.count()
print(result)
print('-' * 50)

newDf = df.loc[:, ['평균','개수']]
newDf.plot(kind='bar', rot=0)
plt.title('3개 극장의 평균과 상영관 수')
filename = 'p280_DataframeGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
# plt.show()

labels = []
explode = (0, 0.03, 0.06)

for key in sumSeries.index:
    mydata = key + ' ( ' + str(sumSeries[key]) + ' )'
    labels.append(mydata)

fig, ax1 = plt.subplots()
mytuple = tuple(labels)
ax1.pie(sumSeries, labels=mytuple, explode=explode, shadow=True, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

filename = 'p280_DataframeGraph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()