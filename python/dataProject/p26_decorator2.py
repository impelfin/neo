#!/usr/bin/env python

import datetime

def datetime_deco(func):
    def docorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
        print()
    return docorated

@datetime_deco
def func1():
    print('Main Function1 start')

@datetime_deco
def func2():
    print('Main Function2 start')

@datetime_deco
def func3():
    print('Main Function2 start')

func1()
func2()
func3()