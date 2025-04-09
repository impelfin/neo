#!/usr/bin/env python

# f(x) = x * f(x-1), f(x) = 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

n = input("Enter a number: ")
print("{} factorial is: {}".format(n, factorial(int(n))))
