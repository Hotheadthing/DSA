A = [[1, -2, -3],
     [-4, 5, -6],
     [-7, -8, 9]]
Sum = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        if i == j:
            Sum += A[i][j]
print(Sum)
