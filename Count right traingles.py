A = [1, 1, 2]
B = [1, 2, 1]
A = [1, 1, 2, 3, 3]
B = [1, 2, 1, 2, 1]
xMap = {}
ymap = {}

for i in range(len(A)):
    if A[i] not in xMap:
        xMap.__setitem__(A[i],1)
    else:
        xMap[A[i]] += 1

for j in range(len(B)):
    if B[j] not in ymap:
        ymap.__setitem__(B[j],1)
    else:
        ymap[B[j]] += 1

ans = 0
for i in range(len(A)):
    x = A[i]
    y = B[i]
    count1 = xMap[A[i]] - 1
    count2 = ymap[B[i]] - 1
    ans += count2 * count1
print(ans)