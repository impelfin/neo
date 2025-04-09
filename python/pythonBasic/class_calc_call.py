#!/usr/bin/env python

import class_calc

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

my = class_calc.Calc(a, b)

print(f'{a} + {b} = {my.add()}')
print(f'{a} - {b} = {my.sub()}')