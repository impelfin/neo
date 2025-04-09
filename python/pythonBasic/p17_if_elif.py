#!/usr/bin/env python

while True:
    i = input("Input the number(q:quit) : ")

    if i == 'q' or i == 'Q' or i == 'ㅂ':
        break
    elif i.isalpha():
        print('Please enter a valid input')
        continue
    else:
        if int(i) > 0:
            print("This is positive number")
        elif int(i) < 0:
            print("This is negative number")
        else:
            print("This is Zero")