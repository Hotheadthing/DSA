A = [12, 34, 67, 90]
B = 2
A.sort()
# print(A)
n = len(A)
l = A[-1]
r = 0
for d in A:
    r += d

# print(f"the value of r is {r}")


def count(arr,mid,B):
    pages = 0
    students = 1
    for i in range(len(arr)):
        if pages + arr[i] <= mid:
            pages += arr[i]
        else:
            pages = arr[i]
            students += 1
    if students > B:
        return False
    else:
        return True
ans = -1
while l <= r:
    mid = (l+r)//2
    # print(mid,(l,r))
    if count(A, mid, B):
        ans = mid
        # print(f"the value of ans is {ans}")
        r = mid - 1
    else:
        l = mid + 1
print(ans)