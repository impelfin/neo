#!/usr/bin/env python

tuple01 = (10, 20, 30)
tuple02 = tuple01 + (40,)

print('print Tuple01 : ', tuple01)
print('print Tuple02 : ', tuple02)

tuple02 = (10, 20, 30, 40)

mylist = [10, 20, 30, 40]

tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print('Components are same')
else:
    print('Components are not same')

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
tuple06 = tuple04 + tuple05
print(tuple06)

tuple07 = (tuple01 * 3)
print(tuple07)

a, b = (11, 22)
a, b = b, a
print(f'a : {a}, b : {b}')

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3])
print(tuple08[3:])
