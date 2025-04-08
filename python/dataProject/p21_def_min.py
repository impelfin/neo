#!/usr/bin/env python

def min(a, b):
    if a < b:
        return a
    else:
        return b

a = int(input("input first number: "))
b = int(input("input second number: "))

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))