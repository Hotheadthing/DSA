import math
A = [1, 2, 3, 4]
# A = [ 96, 98, 5, 41, 80 ]
val = max(A)
arr = []
for i in range(val+1):
    if i == 0 or i == 1:
        arr.append(0)
    else:
        arr.append(i)

qMap = {}
for d in A:
    if d not in qMap:
        qMap.__setitem__(d,1)
aMap = {}
ans = []
for i in range(2,len(arr)):
    if arr[i] == i:
        ans.append(i)
        for j in range(2*i,len(arr),i):
            arr[j] = 0
            if j in qMap:
                if i not in aMap:
                    aMap.__setitem__(i,1)


# print(qMap)
# print(aMap)

for d in ans:
    if d in qMap:
        if d not in aMap:
            aMap.__setitem__(d,1)

print(aMap)
# mMap = {}
# print(ans)
# for i in range(len(A)):
#     for d in ans:
#         if d > A[i]:
#             break
#         elif A[i] % d == 0:
#             if d not in mMap:
#                 mMap.__setitem__(d,1)
#
# print(len(mMap))



