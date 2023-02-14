A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[1, 2, 3],
     [5, 5, 6],
     [7, 8, 9]]
count = 1
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] != B[i][j]:
            count = 0
if count == 0:
    return 0
else:
    return 1



