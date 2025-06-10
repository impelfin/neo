import math
import lmstudio as lms

def add(a: int, b: int) -> int:
    """ Given two numbers a and b, return the sum of them. """
    return a + b

def is_prime(n: int) -> bool:
    """ Given a number n, return True if it is prime, False otherwise. """
    if n < 2:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True

model = lms.llm()
model.act(
    "Is the result of 12345 + 45678 a prime? Think step by step.",
    [add, is_prime],
    on_message = print
)
