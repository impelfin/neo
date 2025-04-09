#!/usr/bin/env python

from logging import raiseExceptions

list = []

try:
    while True:
        print('Item amount : ', len(list))
        print('Inventory : ', list)

        if len(list) >= 4:
            raise Exception("Inventory is Lock")
        item = 'Item' + str(len(list))
        list.append(item)
except Exception as e:
    print("Inventory is Full")
    print(e)