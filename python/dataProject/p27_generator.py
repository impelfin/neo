#!/usr/bin/env python

def counter3(max):
    t = 0
    while t < max:
        yield t
        t += 1
    return

timer = counter3(5)
print(timer.__next__())
print(timer.__next__())
print(timer.__next__())
print(next(timer))
print(next(timer))
