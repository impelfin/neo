#!/usr/bin/env python

import prime_func

while True:
    n = int(input("Input number(0 : Quit) : "))

    if (n == 0):
        break
    if (n < 2) :
        print("re-enter number~!!")
        continue
    print(f"{n} is prime number") if prime_func.prime(n) == 1 else print(f"{n} is not prime number")
