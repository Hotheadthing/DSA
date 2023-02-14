A = [1, 2, 3]

arr = []


def dfs(A):
    if len(A) == 1:
        return [A.copy()]

    for i in range(len(A)):
        val = A.pop(0)
        permutation = dfs(A)
        for x in permutation:
            x.append(val)
        arr.extend(permutation)
        A.append(val)


dfs(A)
print(arr)

