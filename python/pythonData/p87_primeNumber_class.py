import random

class Prime(object):
    def __init__(self, num):
        self.num = num

    def isPrime(self):
        for k in range(2, self.num + 1):
            if self.num % k == 0:
                break
        if k == self.num:
            return 1
        else:
            return 0

prime = Prime(random.randint(2, 10))
print(f'{prime.num} is prime number') if prime.isPrime() else print(f'{prime.num} is not prime number')    