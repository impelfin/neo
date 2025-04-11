from pandas import Series
import matplotlib
import matplotlib.pyplot as plt

# print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])
plt.rcParams['font.family'] = 'NanumBarunGothic'

mylist = [30, 20, 40, 30, 60, 50]
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주', '홍길동']

print(myindex)
print(mylist)
print('-' * 50)

myseries = Series(data=mylist, index=myindex)
myylim = [0, myseries.max() + 10]
myseries.plot(title='시험점수', kind='line', ylim=myylim, grid=True, rot=10, use_index=True)

filename = 'p249_seriesGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()
