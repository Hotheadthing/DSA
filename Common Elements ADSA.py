A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]
A_map = {}
arr = []

for i in range(len(A)):
    if A[i] not in A_map:
        A_map.__setitem__(A[i],1)
    else:
        A_map[A[i]] += 1

for j in range(len(B)):
    if B[j] in A_map:
        arr.append(B[j])
        A_map[B[j]] -= 1
        if A_map[B[j]] == 0:
            del A_map[B[j]]

print(arr)