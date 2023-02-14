A = 2
B = "abab"
mMap = {}
for i in range(len(B)):
    if B[i] not in mMap:
        mMap.__setitem__(B[i], 1)
    else:
        mMap[B[i]] += 1

print(mMap)
flag = True
for d in mMap:
    if mMap[d] % A != 0:
        flag = False
        break

if flag == True:
    print(1)
else:
    print(-1)
