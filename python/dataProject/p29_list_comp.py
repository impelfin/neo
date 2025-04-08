#!/usr/bin/env python

numbers = [1, 2, 3, 4, 5]
evens = [2 * i for i in numbers]

print(evens)
print(sum(evens))

squares = [i ** i for i in numbers]
print(squares)
