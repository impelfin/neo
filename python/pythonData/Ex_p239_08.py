import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'tips.csv'

myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

mycolors = ['r', 'b']
labels = myframe['sex'].unique()
cnt = 0  # 카운터 변수

for finditem in labels:
    xdata = myframe.loc[myframe['sex'] == finditem, 'total_bill']
    ydata = myframe.loc[myframe['sex'] == finditem, 'tip']
    plt.plot(xdata, ydata, color=mycolors[cnt], marker='o', linestyle='None', label=finditem)
    cnt += 1

plt.legend()
plt.xlabel("결제 총액")
plt.ylabel("팁 비용")
plt.title("결제 총액과 팁 비용의 산점도")
plt.grid(True)

filename = 'Ex_p239_08.png'
plt.savefig (filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()