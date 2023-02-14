A = [1, 2, 3, 4, 5]
A = [-1, 1]
n = len(A)
for i in range(1,n):
    A[i] = A[i] + A[i-1]
print(A)

hmap = {}

for i in range(n):
    if A[i] not in hmap:
        hmap.__setitem__(A[i],1)
        if A[i] == 0:
            print(1)
            break
    else:
        print(1)
        break
