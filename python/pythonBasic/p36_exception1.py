#!/usr/bin/env python

try:
    f = open('test.txt', 'r')
except IOError as e:
    print(e)
finally:
    data = f.readline()
    print(data)
    f.close()