import heapq
from collections import deque

# A = 5
# B = [[1, 2],
#      [4, 1],
#      [2, 4],
#      [3, 4],
#      [5, 2],
#      [1, 3]]

A = 5
B = [[1, 2],
     [2, 3],
     [3, 4],
     [4, 5]]

A = 5
B = [
    [1, 4],
    [2, 1],
    [4, 3],
    [4, 5],
    [2, 3],
    [2, 4],
    [1, 5],
    [5, 3],
    [2, 5],
    [5, 1],
    [4, 2],
    [3, 1],
    [5, 4],
    [3, 4],
    [1, 3],
    [4, 1],
    [3, 5],
    [3, 2],
    [5, 2]
]  # 1
A = 5
B = [
    [1, 2],
    [1, 3],
    [2, 3],
    [1, 4],
    [4, 3],
    [4, 5],
    [3, 5]
]  # 0
A = 3
B = [
    [1, 3],
    [2, 3],
    [3, 2]
]  # 1
A = 3
B = [
  [1, 2],
  [2, 3],
  [3, 1]
] #1
A = 2
B = [
  [1, 2]
]
indegree = [0 for i in range(A + 1)]
adj = [[] for j in range(A + 1)]

for i in range(len(B)):
    adj[B[i][0]].append(B[i][1])
    indegree[B[i][1]] += 1

print(adj)
print(indegree)

q = []
heapq.heapify(q)

count = 0
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        heapq.heappush(q,i)

print(q)


#
ans = []
while q:
    val = heapq.heappop(q)
    ans.append(val)
    for i in range(len(adj[val])):
        v = adj[val][i]
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(q, v)

print(ans)
