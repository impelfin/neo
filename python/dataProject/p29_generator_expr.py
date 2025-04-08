#!/usr/bin/env python

numbers = [1, 2, 3, 4, 5]
evens = (2 * i for i in numbers)
print(evens)
print(evens.__next__())
print(evens.__next__())
print(sum(evens))
print()

print(numbers)
numbers.reverse()
print(numbers)
print()

evens = (2 * i for i in numbers)
print(evens)
print(evens.__next__())
print(evens.__next__())
print(numbers)
print(evens.__next__())