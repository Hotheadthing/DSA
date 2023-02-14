import math
A = [10000, 20000, 30000]
B = 6
A = [1, 1, 1]
B = 4
# A = [ 8, 7, 1, 5, 5, 10, 10, 1, 5, 3 ]
# B = 17
# A = [ 9, 8, 9 ]
# B = 4
# A.sort()
# print(A)
l = 1
r = min(A)
for d in A:
    r += d
# print(r)
def count(arr,mid,B):
    if mid == 0:
        return False
    offices = 0
    for d in arr:
        offices += d // mid
        if offices >= B:
            return True
    return False
ans = 0
while l <= r:
    mid = (l+r)//2
    print(mid)
    if count(A, mid,B):
        ans = mid
        l = mid + 1
        # times += 1
    else:
        r = mid - 1
        # times += 1
print(ans)

