A = "abc"
A = "bbcd"
# A = "hqghumeaylnlfdxfi"
n = len(A)
r = n-1
l = 0
count = 0

while l <= r:
    if A[l] == A[r]:
        l += 1
        r -= 1
    else:
        l = 0
        count = n - r
        while A[l] == A[r]:
            l += 1
        r -= 1
print(count)