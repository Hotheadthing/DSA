# A = [ -50, -41, -40, -19, 5, 21, 28 ]
# B = [ -50, -21, -10 ]
A = [0, 23]
B = []
# A = [1, 4, 5]
# B = [2, 3]
# A = [1, 2, 3]
# B = [4]
a = 0
b = 0
n = len(A)
m = len(B)
z = n + m
ans = []
if z % 2 != 0:
    x = (z+1) // 2
    ans.append(x)
else:
    x = z//2
    y = x-1
    ans.append(y)
    ans.append(x)
# print(ans)
p = ans[-1]
arr = []
count = 0
while a < n and b < m:
    if A[a] <= B[b]:
        if count == p+1:
            break
        else:
            arr.append(A[a])
            # print(f"the value of a is {A[a]}")
            a += 1
            count += 1
    else:
        if count == p+1:
            break
        else:
            arr.append(B[b])
            # print(B[b])
            b += 1
            count += 1
while a < n:
    if count == p+1:
        break
    else:
        arr.append(A[a])
        # print(f"the value of a is {A[a]}")
        a += 1
        count += 1

while b < m:
    if count == p+1:
        break
    else:
        arr.append(B[b])
        b += 1
        count += 1
print(ans)
print(arr)
if len(ans) == 1:
    print(arr[ans[0]-1])
else:
    d = (arr[ans[-1]] + arr[ans[-2]]) / 2
    print(d)

