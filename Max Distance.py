A = [3, 5, 4, 2]
A = [5, 5, 5, 2, 4, 4, 4, 3, 6]
x = A.copy()
x.sort()
mMap = {}
print(x)

for i in range(len(A)):
    mMap.__setitem__(A[i],i)

print(mMap)

arr = []

for i in range(len(x)):
    arr.append(mMap[x[i]])

print(arr)

ans = -9999999999

for i in range(len(arr)-1):
    ans = max(ans,arr[i+1]-arr[i])
print(ans)
