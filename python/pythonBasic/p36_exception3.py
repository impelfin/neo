#!/usr/bin/env python

def division_function(a, b):
    try:
        print(a/b)
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

division_function("a", 1)
division_function(1, 0)
division_function(4, 2)