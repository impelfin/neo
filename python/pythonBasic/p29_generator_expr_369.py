#!/usr/bin/env python

numbers = (i for i in range(1, 101))

data = list(numbers)

item = [3, 6, 9]

for i in data:
    if i % 10 in item:
        if i // 10 in item:
            print(f"%s" % ("👏👏") , end=" ")
        else:
            print(f"%2s" % ("👏") , end=" ")
    elif i // 10 in item:
        print(f"%2s" % ("👏") , end=" ")
    else:
        print(f"%4d" % (i), end=" ")
    if i % 10 == 0:
        print("\n")
