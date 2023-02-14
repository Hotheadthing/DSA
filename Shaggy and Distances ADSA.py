A = [7, 1, 3, 4, 1, 7]
A = [1, 1]
hmap = {}
n = len(A)
diff = 99999999999999999
for i in range(n):
    if A[i] not in hmap:
        hmap.__setitem__(A[i], i)
    else:
        diff = min(diff, i - hmap[A[i]])
        hmap[A[i]] = i
print(diff)
