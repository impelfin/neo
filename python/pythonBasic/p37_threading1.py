#!/usr/bin/env python

import threading

def sum(low, high):
    total = 0
    for i in range(low, high + 1):
        total += i
    print("Sub Thread : ", total)

t = threading.Thread(target=sum, args=(1,100000))
t.start()

print("Main Thread")