import numpy as np

a = np.array([1,2,3])
b = np.array([3,6,4])

print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
# 내적
print(a.dot(b))

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2,1], [2,3,2]])

print(A)
print(B)
print(A+B)
print(A-B)
print(A*B)
# 전치
print(B.T)
# 내적
print(A.dot(B.T))