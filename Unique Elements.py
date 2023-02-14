A = [1, 1, 1, 3]
#A = [ 51, 6, 10, 8, 22, 61, 56, 48, 88, 85, 21, 98, 81, 76, 71, 68, 18, 6, 14, 23, 72, 18, 56, 30, 97, 100, 81, 5, 99, 2, 85, 67, 46, 32, 66, 51, 76, 53, 36, 31, 81, 56, 26, 75, 69, 54, 54, 54, 83, 41, 86, 48, 7, 32, 85, 23, 47, 23, 18, 45, 79, 95, 73, 15, 55, 16, 66, 73, 13, 85, 14, 80, 39, 92, 66, 20, 22, 25, 34, 14, 51, 14, 17, 10, 100, 35, 9, 83, 31, 60, 24, 37, 69, 62 ]
A.sort()
print(A)
mMap = {}

for i in range(len(A)):
    if A[i] not in mMap:
        mMap.__setitem__(A[i],1)
    else:
        mMap[A[i]] += 1

print(mMap)
count = 0
for i in range(len(A)-1):
    if A[i+1] == A[i]:
        A[i+1] += 1
    if mMap[A[i]] > 1:
        mMap[A[i]] -= 1
        x = A[i]+1
        count += 1
        if x not in mMap:
            mMap.__setitem__(x,1)
        else:
            mMap[x] += 1
print(count)
print(mMap)

