A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 2, 3, 4]]

Sum = []
for i in range(len(A)):
    x = 0
    for j in range(len(A[0])):
        x += A[i][j]
    Sum.append(x)
print(Sum)