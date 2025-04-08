#!/usr/bin/env python

sum = 0
for i in range(10):
    if i % 2 == 0:
        pass
    sum += i
    print(f'sum += {i}')
print()
print(f'sum = {sum}')