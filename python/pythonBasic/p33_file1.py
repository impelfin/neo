#!/usr/bin/env python

f = open('test.txt')
line = 1
while line:
    line = f.readline()
    print(line)
f.close()