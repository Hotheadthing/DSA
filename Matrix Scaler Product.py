A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2
C = []

for j in A:
    C.append(j)
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] * B
print(C)
