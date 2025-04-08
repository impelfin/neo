#!/usr/bin/env python

m = 0
n = 1

def func():
    m = 0
    global n
    m += 1
    n += 1
    print(f'{m} vs {n}')
func()
print(m, n)