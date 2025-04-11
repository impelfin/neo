from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

myindex = ['강감찬', '홍길동', '이순신', '최영']
member = Series(data=[20, 60, 80, 40], index=myindex)
print(member)
print('-' * 50)

print('# values 속성을 이용한 요소들의 값 확인')
print(member.values)
print('-' * 50)

print('# index 속성을 이용한 색인 객체 확인')
print(member.index)
print('-' * 50)

member.plot(kind='bar', rot=40, ylim=[0, member.max() + 10], use_index=True, grid=False, table=False, color=['r', 'b', 'g', 'y'])
plt.xlabel('학생이름')
plt.ylabel('점수')
plt.title('학생별 시험 점수')

ratio = 100 * member / member.sum()
print(ratio)
print('-' * 50)

for idx in range(member.size):
    value = str(member.iloc[idx]) + '건'
    ratioval = '%.1f' % ratio.iloc[idx]

    plt.text(x=idx, y=member.iloc[idx], s=value, horizontalalignment='center')
    plt.text(x=idx, y=member.iloc[idx] / 2, s=ratioval, horizontalalignment='center')

meanval = member.mean()
print(meanval)
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linestyle='dashed', linewidth=1)
plt.text(x=0, y=meanval + 1, s=average, horizontalalignment='center')

filename = 'p255_seriesExam.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()