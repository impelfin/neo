import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'ex802.csv'
myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(City)'

myframe.plot(title='지역별 차량 등록 대수', kind='bar', rot=0, legend=True)
print(myframe)
print('-' * 50)

filename = 'p262_DataframeGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

myframeT = myframe.T
print(myframeT)
print('-' * 50)

myframeT.plot(title='지역별 차량 등록 대수', kind='bar', rot=0, legend=True)

filename = 'p262_DataframeGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

ymax = myframeT.sum(axis=1)
ymaxlimit = ymax.max() + 10

myframeT.plot(title='지역별 차량 등록 대수', kind='bar', ylim=[0, ymaxlimit], rot=0, stacked=True, legend=True)
filename = 'p262_DataframeGraph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()