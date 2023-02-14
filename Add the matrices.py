A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
length = len(A)
C= []
for j in A:
    C.append(j)
for i in range(length):
    for j in range(len(A[0])):
        C[i][j] = A[i][j]+B[i][j]
print(C)
# C = [[A[i][j] + B[i]B[j] for j in range(len(A[0]))] for i in range(length)]

# result = [[A[i][j] + B[i][j] for j in range
# (len(A[0]))] for i in range(len(A))]
