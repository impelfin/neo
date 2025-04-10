def nolambda(x, y):
    return 3 * x + 2 * y

x, y = 3, 5

yeslambda = lambda x, y: 3 * x + 2 * y

print(f'nolambda({x}, {y}) = {nolambda(x, y)}')
print(f'yeslambda({x}, {y}) = {yeslambda(x, y)}')
