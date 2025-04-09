#!/usr/bin/env python

def min(a, b):
    return a if a < b else b


a = int(input("input first number: "))
b = int(input("input second number: "))

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))
