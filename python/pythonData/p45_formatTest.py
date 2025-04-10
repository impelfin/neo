#!/usr/bin/env python

salary = int(input("월 급여 입력 : "))
income = 0
tax = 0

if salary > 500:
    income = 12 * salary
else:
    income = 13 * salary

if income > 10000:
    tax = 0.2 * income
elif income > 7000:
    tax = 0.15 * income
elif income > 5000:
    tax = 0.12 * income
elif income > 1000:
    tax = 0.1 * income
else:
    tax = 0

print("월급 : %d" % salary)
print("연봉 : %d" % income)
print("세금 : %d" % tax)
print("실수령액 : %d" % (income - tax))