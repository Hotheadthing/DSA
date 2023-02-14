import math
A = [1, 1, 1]
B = 2
# A = [1, 1]
# B = 2
# A = [ 1, 2, 6, 6, 7, 9, 9 ]
# B = 13
# A = [ 2, 3, 5, 6, 10 ]
# B = 6
# A = [ 1, 2, 3, 3, 4, 6, 7 ]
# B = 13
# A = [ 2, 3, 3, 5, 7, 7, 8, 9, 9, 10, 10 ]
# B = 11
# A = [ 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 9, 10 ]
# B = 5
# A = [ 2, 2, 3, 4, 4, 5, 6, 7, 10 ]
# B = 8
# A = [ 1, 2, 2, 2, 2, 3, 3, 4, 8, 8, 8, 8, 10, 10 ]
# B = 5
A = [ 2, 2, 3, 4, 4, 5, 6, 7, 10 ]
B = 8
n = len(A)
i = 0
j = n-1
count = 0
mmap = {}
for d in A:
    if d not in mmap:
        mmap.__setitem__(d,1)
    else:
        mmap[d] += 1
# print(mmap)
while i < j:
    if A[i] + A[j] == B:
        mmap[A[j]] -= 1
        count += mmap[A[i]]
        print(A[i],A[j],count)
        print(mmap)
        j -= 1
    elif A[i] + A[j] < B:
        i += 1
    else:
        j -= 1
print(count)