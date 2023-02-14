import math
A = "a"
arr = []

for i in range(len(A)):
    arr.append(ord(A[i]))

#print(arr)
arr.sort()
#print(arr)

def count(n):
    count = 0
    for i in range(len(arr)):
        if arr[i] < n:
            count += 1
    return count

n = len(arr)
ans = 1
for i in range(len(A)):
    j = 0
    mark = 0
    if ord(A[i]) == arr[j]:
        arr.remove(arr[j])

    else:
        x = count(ord(A[i]))
        y = n
        z = y - i - 1
        ans += (x * math.factorial(z))
        arr.remove(ord(A[i]))


print(ans % 1000003)
