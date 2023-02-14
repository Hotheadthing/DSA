A = [1, 5, 3, 4, 2]
B = 3
A = [8, 12, 16, 4, 0, 20]
B = 4
A = [1, 1, 1, 2, 2]
B = 0
A = [1,2]
B = 0
A.sort()
# print(A)
i = 0
n = len(A)
j = 1
arr = []
while j < n:
    if A[j] - A[i] == B:
        if j != i:
            x = [A[j],A[i]]
            if x not in arr:
                arr.append(x)
        i += 1
        j += 1
    elif A[j] - A[i] < B:
        j += 1
    else:
        i += 1

print(len(arr))