A = [   [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]   ]

A = [   [0, 1],
        [2, 0]    ]

rows = len(A)
colum = len(A[0])
start = [0,0]
zero_count = 0
for i in range(rows):
    for j in range(colum):
        if A[i][j] == 1:
            start[0] = i
            start[1] = j
        if A[i][j] == 0:
            zero_count += 1


print(start)
# print(zero_count)

arr = []
def path(i,j,count):
    if (i >= rows) or (i < 0) or (j >= colum) or (j < 0):
        return

    if A[i][j] == 2:
        if count == 0:
            arr.append(1)
        return

    if A[i][j] == -1:
        return
    A[i][j] = -1
    path(i+1, j, count-1)
    path(i-1, j, count-1)
    path(i, j+1, count-1)
    path(i, j-1, count-1)
    A[i][j] = 0



path(start[0],start[1],zero_count+1)

print(len(arr))



