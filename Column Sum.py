A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 2, 3, 4]]
length = len(A)
C = []
D = []
for j in A:
    C.append(j)
for i in range(len(A[0])):
    X = 0
    for j in range(length):
        X += A[j][i]
    D.append(X)
print(D)