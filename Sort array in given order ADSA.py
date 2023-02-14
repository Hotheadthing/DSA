A = [1, 2, 3, 4, 5]
B = [5, 4, 2]
A = [5, 17, 100, 11]
B = [1, 100]
A = [ 10, 2, 18, 16, 16, 16 ]
B = [ 3, 13, 2, 16, 4, 19 ]
A = [ 20, 14, 8, 18, 6 ]
B = [ 1, 16, 7, 6, 17, 3, 13, 8, 19, 20 ]

arr = []
mMap = {}
A.sort()
n = len(A)
for i in range(n):
    if A[i] not in mMap:
        mMap.__setitem__(A[i], 1)
    else:
        mMap[A[i]] += 1

# print(mMap)
bMap = {}
for i in range(len(B)):
    bMap.__setitem__(B[i],1)

# print(bMap)

for d in bMap:
    if d in mMap:
        for i in range(mMap[d]):
            arr.append(d)
            mMap[d] -= 1

# print(arr)
# print(mMap)

for d in mMap:
    if mMap[d] != 0:
        for i in range(mMap[d]):
            arr.append(d)
            mMap[d] -= 1
print(arr)
# print(mMap)
