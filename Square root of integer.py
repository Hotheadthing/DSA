A = 5
l = 1
r = A
x = 999999999999999
flag = False
while l <= r:
    mid = (l+r) // 2
    if mid * mid == A:
        print(mid)
        flag = True
        break
    elif mid * mid < A:
        l = mid + 1
        x = mid
    else:
        r = mid -1
if flag == False:
    print(x)