A = [
       [-2, -3, 3],
       [-5, -10, 1],
       [10, 30, -5]
     ]

A = [
       [1, -1, 0],
       [-1, 1, -1],
       [1, 0, -1]
     ]
val = A[len(A)-1][len(A[0])-1]

if val < 0:
    A[len(A) - 1][len(A[0]) - 1] = -1 * val + 1
elif val >= 0:
    A[len(A) - 1][len(A[0]) - 1] = 1

for i in range(len(A)-2,-1,-1):
    v = A[i][len(A[0])-1]
    v_or = A[i+1][len(A[0])-1]
    res = v_or - v
    if res > 0:
        A[i][len(A[0])-1] = res
    else:
        A[i][len(A[0]) - 1] = 1

for j in range(len(A[0])-2,-1,-1):
    v = A[len(A)-1][j]
    v_or = A[len(A)-1][j+1]
    res = v_or - v
    if res > 0:
        A[len(A)-1][j] = res
    else:
        A[len(A)-1][j] = 1


for i in range(len(A)-2,-1,-1):
    for j in range(len(A[0])-2,-1,-1):
        # print(A[i][j],A[i+1][j],A[i][j+1])
        minimum = min(A[i+1][j],A[i][j+1])
        res = minimum - A[i][j]
        if res > 0:
            A[i][j] = res
        else:
            A[i][j] = 1

print(A[0][0])


