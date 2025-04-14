import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'Baseball_2021.csv'

myframe = pd.read_csv(filename, encoding='utf-8')
print('head() 메소드 결과')
print(myframe.head())
print('-' * 50)

print('info() 메소드 결과')
print(myframe.info())
print('-' * 50)

mycolor = ['r', 'g', 'b']
labels = ['두산', 'LG', '키움']

cnt = 0

for finditem in labels:
    xdata = myframe.loc[myframe['팀명'] == finditem, '안타']
    ydata = myframe.loc[myframe['팀명'] == finditem, '타점']
    plt.plot(xdata, ydata, label=finditem, color=mycolor[cnt], marker='o', linestyle='None')
    cnt += 1

plt.legend(loc=4)
plt.xlabel('안타')
plt.ylabel('타점')
plt.title('안타와 타점에 의한 산점도')
plt.grid(True)

filename = 'p266_scatterPlot.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()