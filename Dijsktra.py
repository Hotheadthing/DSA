import heapq
A = 6
B = [   [0, 4, 9],
        [3, 4, 6] ,
        [1, 2, 1] ,
        [2, 5, 1] ,
        [2, 4, 5] ,
        [0, 3, 7] ,
        [0, 1, 1] ,
        [4, 5, 7] ,
        [0, 5, 1] ]
C = 4
A = 5
B = [   [0, 3, 4],
        [2, 3, 3] ,
        [0, 1, 9] ,
        [3, 4, 10],
        [1, 3, 8]  ]
C = 4
A = 7
B = [
  [2, 4, 10],
  [3, 4, 1],
  [3, 6, 1],
  [1, 2, 4],
  [4, 5, 6]
]
C = 2
adj = [[] for i in range(A+1)]

for j in range(len(B)):
    adj[B[j][0]].append((B[j][1],B[j][2]))
    adj[B[j][1]].append((B[j][0],B[j][2]))

print(adj)

q = []
heapq.heapify(q)
ans = [[] for i in range(A)]

ans[C] = 0

# print(adj[4][0][0],adj[4][0][1])

for i in range(len(adj[C])):
    heapq.heappush(q,[adj[C][i][1],adj[C][i][0]])

# print(q)

# wt = 0
visit = set()
visit.add(C)
while q:
    val = heapq.heappop(q)
    wt = val[0]
    if ans[val[1]] == []:
        ans[val[1]] = wt
    # else:
    #     wt = min(wt,ans[val[1]])
    if val[1] not in visit:
        for i in range(len(adj[val[1]])):
            des = adj[val[1]][i][0]
            weight = adj[val[1]][i][1] + wt
            heapq.heappush(q,[weight,des])
        visit.add(val[1])

print(ans)

