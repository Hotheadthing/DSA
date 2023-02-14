A = [1, 2, 3, 4, 5]
B = 3
A = [1, 2]
B = 2
A = [ 82, 61, 38, 88, 12, 7, 6, 12, 48, 8, 31, 90, 35, 5, 88, 2, 66, 19, 5, 96, 84, 95 ]
B = 8
A.sort()
# print(A)
n = len(A)
l = 1
r = A[n-1] - A[0]
ans = 0

def count(arr,mid,B):
    B -= 1
    in_count = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - in_count >= mid:
            B -= 1
            in_count = arr[i]
    if B <= 0:
        return True
    else:
        return False
while l <= r:
    mid = (l+r)//2
    # print(mid)
    if count(A, mid, B):
        ans = mid
        # print(f"the value of ans is {ans}")
        l = mid + 1
    else:
        r = mid - 1
print(ans)

# print(ans)
