A = [1, 2, 3, 4, 5]
B = 10
A = [5, 17, 100, 11]
B = 130
n = len(A)
l = 0
r = n
def subarray(arr,k,x):
    sum = 0
    a = 0
    b = k - 1
    flag = True
    for i in range(n):
        sum += arr[i]
        if i > b:
            b = b+1
            sum -= arr[a]
            a += 1
        if sum > x:
            flag = False
            break
    return flag

ans = 9999999999999999
while l <= r:
    mid = (l+r)//2
    x = subarray(A,mid,B)
    if x:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)






