#!/usr/bin/env python

def gcd(a, b):
    if a < b:
        a, b = b, a
    print("gcd", (a, b))
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Input First number : "))
b = int(input("Input Second number : "))

print(f'gcd({a}, {b}) of {a}, {b} = {gcd(a, b)}')
