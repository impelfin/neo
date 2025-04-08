#!/usr/bin/env python

numbers = [0, 1, 2, 3]
names = ['Kim', 'Lee', 'Park', 'Choi']
print(numbers[0])
print(names[2:])
print(numbers[-1])
print(numbers+names)
empty=[]
print(empty)

# append
names.append('Moon')
print(names)

# insert
names.insert(1, 'Gang')
print(names)

# delete
del names[1]
print(names)

# remove
names.remove('Moon')
print(names)

# pop
value = names.pop()
print(value)

# pop
value = names.pop(1)
print(value)

# extend
numbers.extend([4, 5, 6, 4, 4, 5, 6])
print(numbers)

# count
print(numbers.count(4))

# sort
numbers.sort()
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# clear
numbers.clear()
print(numbers)
