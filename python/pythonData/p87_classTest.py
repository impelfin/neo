import random

class Calculate(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second
    
a = random.randint(1, 20)
b = random.randint(1, 10)

calc = Calculate(a, b)

print(f'{a} + {b} = {calc.add()}')
print(f'{a} - {b} = {calc.sub()}')
print(f'{a} * {b} = {calc.mul()}')
print(f'{a} / {b} = {round(calc.div(), 4)}')