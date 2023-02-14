A = "abcde"
A = "abbaee"
A = "yzfbzbyyrurquqf"
n = len(A)
mMap = {}
for i in range(n):
    if A[i] not in mMap:
        mMap.__setitem__(A[i], 1)
    else:
        mMap[A[i]] += 1
print(n)
print(mMap)
flag = 0
if n % 2 != 0:
    for d in mMap:
        if mMap[d] % 2 != 0:
            if flag == 0:
                flag = 1
            else:
                flag = 2
                break
    if flag == 1:
        print(1)
    else:
        print(0)
else:
    flag1 = 0
    for d in mMap:
        if mMap[d] % 2 != 0:
            flag1 = 1
            break
    if flag1 == 0:
        print(1)
    else:
        print(0)

