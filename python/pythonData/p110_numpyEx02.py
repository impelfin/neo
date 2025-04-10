import numpy as np

a = np.array([-1, 3, 2, -6])
b = np.array([3, 6, 1, 2])

print("\nsol1")
A = np.reshape(a, (2, 2))
print(A)

print("\nsol2")
B = np.reshape(b, (2, 2))
print(B)

print("\nsol3-1")
result3_1 = np.matmul(A, B)
print(result3_1)

print("\nsol3-2")
result3_2 = np.matmul(B, A)
print(result3_2)

print("\nsol4-1")
a = np.reshape(a, (1, 4))
print(a)

a2 = np.transpose(a)
print(a2)
print()

b = np.reshape(b, (1, 4))
print(b)

b2 = np.transpose(b)
print(b2)
print()

print("\nsol4-2")
result4 = np.matmul(a, b2)
print(result4)