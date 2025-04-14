import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

mycolors = ['blue', '#6aff00', 'yellow', '#ff003c', 'green']
mylist = [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운', '노천명', '윤동주', '이육사']

plt.pie(x=mylist, labels=myindex, colors=mycolors, shadow=mycolors, explode=[0, 0.1, 0, 0, 0], autopct='%1.2f%%', startangle=90, counterclock=False)

plt.legend(loc=4)

filename = 'Ex_p239_09.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show() 