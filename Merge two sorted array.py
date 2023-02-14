A = [4, 7, 9 ]
B = [2, 11, 19 ]
arr = []
p1 = 0
p2 = 0
n = len(A)
m = len(B)

while p1 < n and p2 < m:
    if A[p1] <= B[p2]:
        arr.append(A[p1])
        p1 += 1
    else:
        arr.append(B[p2])
        p2 += 1

while p1 < n:
    arr.append(A[p1])
    p1 += 1

while p2 < m:
    arr.append(B[p2])
    p2 += 1

print(arr)


