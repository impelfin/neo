import numpy as np

print("\n np.repeat function")
su1 = 2
rep_cnt1 = 5
result = np.repeat(su1, rep_cnt1)
print(type(result))
print(result)

array1 = np.array([1, 2])
array2 = np.array([3, 4])
print("\n array1")
print(array1)
print("\n array2")
print(array2)   

print("\n np.concatenate function")
result = np.concatenate((array1, array2))
print(result)

su2 = 3
rep_cnt2 = 4
print("\n np.repeat function")
abcd = np.repeat(su2, rep_cnt1)
defg = np.repeat(su2, rep_cnt2)
result = np.concatenate((abcd, defg))
print(result)

print("\n np.reshape function")
array3 = np.array([1, 2, 3, 4, 5, 6])
print(array3)

print("\n 2row 3col")
result = np.reshape(array3, (2, 3))
print(result)

print("\n 3row 2col")
result = np.reshape(array3, (3, 2))
print(result)

print("\n array4")
array4 = np.array([[3, 6, 2],[4, 1, 5]])
print(array4)

print("\n transposed array") 
result = np.transpose(array4)
print(result)