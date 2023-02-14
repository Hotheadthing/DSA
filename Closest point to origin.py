A = [
       [1, 3],
       [-2, 2]
     ]
B = 1
A = [
    [1, -1],
    [2, -1]
]
B = 1

A.sort(key=lambda Z: Z[0]**2 + Z[1]**2)
print(A)
print(A[:B])