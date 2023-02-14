A = 2
B = 5
C = [1, 10]
A = 10
B = 1
C = [1, 8, 11, 3]

l = max(C)*B
r = 0
for d in C:
    r += d
r = r * B
ans = 0

def timepassed(arr,mid,A,B):
    if max(arr) > mid:
        return False
    time = 0
    for i in range(len(arr)):
        time += B*(arr[i])
        # print(f"value of time is {time}-- for mid value{mid}")
        if time > mid:
            A -= 1
            time = B*(arr[i])
            if A == 0:
                return False
    return True
while l <= r:
    mid = (l+r)//2
    if timepassed(C,mid,A,B):
        ans = mid
        # print(ans)
        r = mid - 1
    else:
        l = mid + 1
print(ans)

