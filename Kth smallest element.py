A = [1, 2]
B = 2
arr = []

n = len(A)
count = 0
for i in range(n):
    x = A[i]
    temp = 0
    if count == B:
        break
    for j in range(i+1,n):
        if A[j] < x:
            x = A[j]
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    arr.append(x)
    count += 1

print(arr[-1])