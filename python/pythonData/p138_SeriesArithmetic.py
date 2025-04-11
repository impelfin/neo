from pandas import Series

myindex1 = ['강호민', '유재준', '김제명', '신동진']
mylist1 = [30, 40, 50, 60]

myindex2 = ['강호민', '유재준', '김제명', '이수진']
mylist2 = [20, 40, 60, 70]

myseries1 = Series(data=mylist1, index=myindex1)
myseries2 = Series(data=mylist2, index=myindex2)

print('\n # data of series1')
print(myseries1)

print('\n # data of series2')
print(myseries2)

# arithmetic operation
print(myseries1 + 5)
print('-' * 50)
print(myseries1 - 10)
print('-' * 50)
print(myseries1 * 2)
print('-' * 50)
print(myseries1 / 3)
print('-' * 50)

# realation operation
print(myseries1 >= 40)
print('-' * 50)

print('\n add of series(if nodata then NaN)')
newseries = myseries1 + myseries2
print(newseries)

print('\n sub of series(operation after fill value 0)')
newseries = myseries1.sub(myseries2, fill_value=0)
print(newseries)

