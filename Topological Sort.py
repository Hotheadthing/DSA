from collections import deque
import heapq

A = 6
B = [[6, 3],
     [6, 1],
     [5, 1],
     [5, 2],
     [3, 4],
     [4, 2]]
A = 3
B = [[1, 2],
     [2, 3],
     [3, 1]]
A = 8
B = [
    [1, 4],
    [1, 2],
    [4, 2],
    [4, 3],
    [3, 2],
    [5, 2],
    [3, 5],
    [8, 2],
    [8, 6]
]  # 1 4 3 5 7 8 2 6
# B.sort(key=lambda x: x[1])
# A = 3
# B = [1, 2]
# C = [2, 3]
adj = [[] for i in range(A + 1)]
for i in range(len(B)):
    adj[B[i][0]].append(B[i][1])

print(adj)

indgree = [0 for i in range(A + 1)]

for node, dir in B:
    indgree[dir] += 1

print(indgree)

count = 0
q = []

for i in range(1, len(indgree)):
    if indgree[i] == 0:
        q.append(i)
        count += 1

print(q)
# print(count)

ans = []
while q:
    heapq.heapify(q)
    val = heapq.heappop(q)
    print(val)
    ans.append(val)
    for i in range(len(adj[val])):
        v = adj[val][i]
        indgree[v] -= 1
        if indgree[v] == 0:
            heapq.heappush(q,v)
            count += 1

if count != A:
    print([])
else:
    print(ans)