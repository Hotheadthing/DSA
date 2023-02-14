A = [1,2,-2,4,-4]
A.insert(0,0)
B = A.copy()
n = len(A)

for i in range(1,n):
    B[i] = B[i] + B[i-1]

print(A,B)
hmap = {}
curr_distance = 0
max_distance = 0
arr = [0,0]
for i in range(n):
    if B[i] not in hmap:
        hmap.__setitem__(B[i],i)
    else:
        curr_distance = i - hmap[B[i]]
        if curr_distance > max_distance:
            max_distance = curr_distance
            arr[1] = i
            arr[0] = hmap[B[i]]
print(A[arr[0]+1:arr[1]+1])

