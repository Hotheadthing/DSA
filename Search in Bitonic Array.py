A = [3, 9, 10, 20, 17, 5, 1]
B = 20
A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12

n = len(A)
l = 0
r = n-1
val = 0
poc = 0
while l <= r:
    mid = (l+r)//2
    if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
        poc = mid
        break
    elif A[mid] < A[mid+1]:
        l = mid + 1

    elif A[mid] <= A[mid-1]:
        r = mid - 1

l = 0
r = poc - 1
while l <= r:
    mid = (l+r) // 2
    if A[mid] == B:
        print(mid)
        break
    elif A[mid] < B:
        l = mid + 1
    else:
        r = mid - 1

l = poc
r = n - 1
flag = False
while l <= r:
    mid = (l+r)//2
    if A[mid] == B:
        print(mid)
        flag = True
        break
    elif A[mid] < B:
        r = mid - 1
    else:
        l = mid + 1
if flag == False:
    print(-1)
