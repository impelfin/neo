#!/usr/bin/env python

import random

def binaryDigits(num, lists):
    q = num // 2
    r = num % 2
    lists.append(r)
    if q == 0:
        lists.reverse()
        return lists
    else:
        return binaryDigits(q, lists)

lists = []
num = random.randrange(4, 20)
print(f'{num} binary number is : {binaryDigits(num, lists)}')


