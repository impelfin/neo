#!/usr/bin/env python

from class_rectangle import *

square1 = Rectangle.isSquare(5, 5)
print(square1)

rect1 = Rectangle(5, 5)
print('Area of rect1 is ', rect1.clacArea())
rect1.printCount()

rect2 = Rectangle(2, 5)
print('Area of rect2 is ', rect2.clacArea())
rect2.printCount()

rect3 = rect1 + rect2
print('Area of rect3 is ', rect3.clacArea())

rect3.width = 6
rect3.height = 6
print('Area of rect3 is ', rect3.clacArea())
rect3.printCount()

rect4 = rect2.__add__(rect1)
print('Area of rect4 is ', rect4.clacArea())
rect4.printCount()