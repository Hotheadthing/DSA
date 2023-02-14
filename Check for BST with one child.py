A = [4, 10, 5, 8]
n = len(A)
arr = []
A = [4, 10, 5, 8]
A = [1, 5, 6, 4]
size = len(A)
min_A = 0
max_A = 0
if A[size-1] > A[size-2]:
    max_A = A[size-1]
    min_A = A[size-2]
else:
    max_A = A[size-2]
    min_A = A[size-1]

for i in range(size-3, -1, -1):
    if A[i] < min_A:
        min_A = A[i]
    elif A[i] > max_A:
        max_A = A[i]
    else:
        print(False)
        break