A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]
A = [   [5, 17, 100, 11],
         [0, 0,  2,   8]    ]
B = [1, 1]
C = [1, 4]
D = [2, 2]
E = [2, 4]

n = len(A[0])
m = len(A)
x = []
j = []
for i in range(n+1):
    if i != n-1:
        j.append(0)
    else:
        j.append(0)
        x.append(j)

for j in range(m):
    A[j].insert(0,0)

A.insert(0,x[0])
print(A)

for i in range(m):
    for j in range(n):
        A[i+1][j+1] = (A[i][j+1] + A[i+1][j] + A[i+1][j+1]) - A[i][j]
print(A)

ans = []
for i in range(len(B)):
    rbi = D[i]
    rbj = E[i]
    tli = B[i]
    tlj = C[i]
    res = A[rbi][rbj]
    res = res + A[tli - 1][tlj - 1] - A[tli - 1][rbj] - A[rbi][tlj - 1]
    print(f"previous {res}")
    res = (res % 1000000007)
    print(f"after {res}")
    ans.append(res)

# print(ans)
# if (tli > 0):
#     res = res - A[tli - 1][rbj]
#
#     # Remove elements between (0, 0)
#     # and (rbi, tlj-1)
# if (tlj > 0):
#     res = res - A[rbi][tlj - 1]
#
#     # Add aux[tli-1][tlj-1] as elements
#     # between (0, 0) and (tli-1, tlj-1)
#     # are subtracted twice
# if (tli > 0 and tlj > 0):