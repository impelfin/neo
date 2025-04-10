#!/usr/bin/env python

class Factorial(object):
    def __init__(self, n):
        self.n = n
    def factorial(self):
        if self.n == 0:
            return 1
        else:
            n = self.n
            self.n -= 1
            return n * self.factorial()

input = int(input("Enter a number: "))
fact = Factorial(input)
print(f'{input}! = {fact.factorial()}')