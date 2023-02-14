A = [1,2,3,4,5]
n = len(A)
left = 0
right = n-1
ans = 0

while left <= right:
    mid = (left+right) // 2

    if A[0] > A[1]:
        ans = A[0]
        left = mid + 1
    if A[-1] > A[-2]:
        ans = A[-1]
        right = mid - 1
    if A[mid-1] <= A[mid] >= A[mid+1]:
        ans = A[mid]
        right = mid - 1
    elif A[mid+1] > A[mid]:
        left = mid + 1
    elif A[mid-1] > A[mid]:
        right = mid - 1

print(ans)
