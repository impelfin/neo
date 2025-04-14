import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'ScoreData.csv'
myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print(myframe['jumsu'].unique())
print('-' * 50)

frame01 = myframe.loc[myframe['jumsu'] == 'lower', 'length']
frame01.index.name = 'lower'
print(frame01.head())
print('-' * 50)

frame02 = myframe.loc[myframe['jumsu'] == 'upper', 'length']
frame02.index.name = 'upper'
print(frame02.head())
print('-' * 50)

totalframe = pd.concat([frame01, frame02], axis=1, ignore_index=True)
totalframe.columns = ['lower', 'upper']
print(totalframe.head())
print('-' * 50)

totalframe.plot(kind='box')
plt.xlabel('점수 구분')
plt.ylabel('길이')
plt.grid(False)
plt.title('점수에 따른 길이의 상자 수염 그래프')

filename = 'p274_boxPlot.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()  