#!/usr/bin/env python

import calc_func

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f'{a} + {b} = {calc_func.add(a, b)}')
print(f'{a} - {b} = {calc_func.sub(a, b)}')