A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
C = []

for i in range(A):
    C.append(0)

for j in range(len(B)):
    x = B[j][0] - 1
    C[x] += B[j][2]
print(C)
length = len(C) -1
for j in range(len(B)):
    y = B[j][1] - 1
    if y != length:
        y = y+1
        C[y] -= B[j][2]
print(C)

for j in range(len(C)):
    if j != 0:
        C[j] = C[j] + C[j-1]
print(C)