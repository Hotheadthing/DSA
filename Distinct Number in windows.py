A = [1, 2, 1, 3, 4, 3]
B = 3
A = [1, 1, 2, 2]
B = 1
n = len(A)
arr = []
if B > n:
    print([])
else:
    mMap = {}
    for i in range(B):
        if A[i] not in mMap:
            mMap.__setitem__(A[i],1)
        else:
            mMap[A[i]] += 1
    arr.append(len(mMap))
    j = 0
    for i in range(B,n):
        mMap[A[j]] -= 1
        if mMap[A[j]] == 0:
            del mMap[A[j]]
        if A[i] not in mMap:
            mMap.__setitem__(A[i],1)
        else:
            mMap[A[i]] += 1
        j += 1
        arr.append(len(mMap))
print(arr)

