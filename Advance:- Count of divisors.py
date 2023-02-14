import math
A = [2, 3, 4, 5]
A = [8, 9, 10]
A = [ 20, 39, 29, 51, 96, 32, 35, 50, 57, 7, 59, 51, 85, 55, 8, 26, 15, 4, 4, 18, 32, 49, 40, 46, 83, 77, 100, 92 ]
arr = []
z = max(A)
for i in range(z+1):
    if i == 0:
        arr.append(0)
    elif i == 1:
        arr.append(1)
    else:
        arr.append(i)
# print(arr)
val = math.floor(math.sqrt(z)+1)
for i in range(2,len(arr)):
    if arr[i] == i:
        for j in range(2*i,len(arr),i):
            if arr[j] == j:
                arr[j] = i

print(arr)

ans = []

for i in range(len(A)):
    count = 2
    x = arr[A[i]]
    print(x,A[i])
    while A[i] % x == 0:
        count += 2
        A[i] = A[i] // arr[A[i]]
    ans.append(count)
print(ans)

