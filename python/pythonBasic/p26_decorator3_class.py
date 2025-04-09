#!/usr/bin/env python

import datetime

class DatetimeDecorator:
    def __init__(self, f):
        self.func = f
    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())
        print()

class MainClass:
    @DatetimeDecorator
    def func1():
        print("Main Function1 start")

    @DatetimeDecorator
    def func2():
        print("Main Function2 start")

    @DatetimeDecorator
    def func3():
        print("Main Function3 start")

my = MainClass()
my.func1()
my.func2()
my.func3()