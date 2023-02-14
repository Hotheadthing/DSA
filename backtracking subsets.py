A = [1, 2, 3]
A = [1, 2, 2]
arr = []
ans = []
hmap = {}
for i in range(len(A)):
    if A[i] not in hmap:
        hmap.__setitem__(A[i],1)
    else:
        hmap[A[i]] += 1


def dfs(i):
    if i >= len(A):
        if ans.copy() not in arr:
            arr.append(ans.copy())
        return

    ans.append(A[i])
    dfs(i+1)
    ans.pop()
    dfs(i+1)


dfs(0)

print(arr)

arr.sort()
print(arr)

