from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

mylist = [30, 20, 40, 30, 60]
myindex = ['강감찬', '김유신', '이순신', '안익태', '운동주']
myseries = Series(data=mylist, index=myindex)
myseries.plot(kind='bar', rot=0, use_index=True, grid=False, table=False, color=['r', 'g', 'b', 'y', 'c'])

plt.xlabel('학생이름')
plt.ylabel('점수')
plt.title('학생별 시험 점수')

ratio = 100 * myseries / myseries.sum()
print(round(ratio, 1))
print('-' * 50)

for idx in range(myseries.size):
    value = str(myseries.iloc[idx]) + '건'
    ratioval = '%.1f' % ratio.iloc[idx]

    plt.text(x=idx, y=myseries.iloc[idx] + 1, s=value, ha='center', va='bottom')
    plt.text(x=idx, y=myseries.iloc[idx] / 2, s=ratioval, ha='center', va='bottom')

meanval = myseries.mean()
print(meanval)
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linestyle='--', linewidth=1)
plt.text(x=0, y=meanval + 1, s=average, ha='center', va='bottom')

filename = 'Ex_p239_06_Graph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()  
