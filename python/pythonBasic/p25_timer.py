#!/usr/bin/env python

def counter2():
    t = [0]
    def increment():
        t[0] += 1
        return t[0]
    return increment

timer = counter2()
print(timer())

print(timer())

