A = [0,1,2,0,1,2]
# A = [0]
mMap = {}

for i in range(len(A)):
    if A[i] not in mMap:
        mMap.__setitem__(A[i],1)
    else:
        mMap[A[i]] += 1
arr = []

x = 0
y = 0
z = 0
for d in mMap:
    if d == 0:
        x = mMap[d]
    elif d == 1:
        y = mMap[d]
    else:
        z = mMap[d]


for i in range(x):
    arr.append(0)
for j in range(y):
    arr.append(1)
for k in range(z):
    arr.append(2)

print(arr)