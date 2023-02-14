A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
     ]

A = [
    [-6, -6],
    [-29, -8],
    [3, -8],
    [-15, 2],
    [25, 25],
    [20, -5]
    ]
A = [
    [-17, -2],
     [20, 10]
    ]
#
A =[
  [-6, -21, 27, 19, 19],
  [0, 0, 5, -21, 19],
  [18, -27, -2, -7, 13],
  [-21, -17, -25, -1, 3],
  [0, -9, -6, -16, -5],
  [29, 9, -25, -7, -25]
  ]

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

for i in range(m):
    for j in range(n):
        A[i+1][j+1] = (A[i][j+1] + A[i+1][j] + A[i+1][j+1]) - A[i][j]
print(A)
ans = -9999999
for i in range(m):
    for j in range(n):
        rbi = 3 #len(A)-1
        rbj = 5  #len(A[0])-1
        tli = i+1
        tlj = j+1
        res = A[2][5]
        res = res + A[tli - 1][tlj - 1] - A[tli - 1][rbj] - A[rbi][tlj - 1]
        ans = max(ans,res)

print(ans)

X =[
    [0,0,0,0],
    [0,1,3,6],
    [0,5,12,21],
    [0,12,27,45]
    ]




# for i in range(len(B)):
#     rbi = D[i]
#     rbj = E[i]
#     tli = B[i]
#     tlj = C[i]
#     res = A[rbi][rbj]
#     res = res + A[tli - 1][tlj - 1] - A[tli - 1][rbj] - A[rbi][tlj - 1]
#     print(f"previous {res}")
#     res = (res % 1000000007)
#     print(f"after {res}")
#     ans.append(res)
