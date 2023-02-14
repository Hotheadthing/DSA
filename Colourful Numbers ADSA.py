A = 23
mMap = {}
A = str(A)
for d in A:
    if d not in mMap:
        mMap.__setitem__(d,1)
    else:
        print(0)
        break
print(mMap)

n = len(A) - 1
j = 0

for i in range()