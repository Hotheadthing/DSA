A = [[1, 2, 3],
     [4, 5, 0],
     [6, 7, 0]]
# var = []
for i in range()
B = []
C = []
D = []
for j in A:
    B.append(j)
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == 0:
            C.append(i)
            D.append(j)
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         for digit in C:
#             if i == digit:
#                 B[i][j] = 0
#         for digit in D:
#             if j == digit:
#                 B[i][j] = 0
# B[1] = [0, 0, 0]

Coloumn = B[:,2]
print(Coloumn)
