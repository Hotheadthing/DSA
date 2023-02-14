from numpy import *
A = [
    [1, 2],
    [3, 4]
    ]
A = transpose(A)
print(A)
for i in range(len(A)):
    x = A[i]
    x = list(x)
    x.reverse()
    A[i] = x
print(A)
