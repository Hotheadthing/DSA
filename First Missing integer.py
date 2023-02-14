A = [1, 2, 0]
# A = [3, 4, -1, 1]
# A = [-8, -7, -6]
# A = [1]
nMap = {}

for i in range(len(A)):
    nMap.__setitem__(i+1,0)
# print(nMap)

for j in range(len(A)):
    if A[j] in nMap:
        nMap[A[j]] += 1

# print(nMap)
arr = -1
for d in nMap:
    if nMap[d] == 0:
        arr = d
        break
if arr == -1:
    print(max(A)+1)
else:
    print(arr)
