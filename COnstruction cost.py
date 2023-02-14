import heapq

A = 3
B = [[1, 2, 14],
     [2, 3, 7],
     [3, 1, 2]]
A = 3
B = [   [1, 2, 20],
        [2, 3, 17]  ]

mod = 1000000007
adj = {c: [] for c in range(A + 1)}
# print(adj)

for src, des, weight in B:
    adj[des].append([weight, src])
    adj[src].append([weight, des])

# print(adj)

cost = [[] for i in range(A + 1)]

q = []
heapq.heapify(q)
visit = set()
for i in range(len(adj[1])):
    heapq.heappush(q, adj[1][i])

visit.add(1)
cum_weight = 0
while q:
    wt, dest = heapq.heappop(q)
    if dest not in visit:
        cum_weight += wt
        for i in range(len(adj[dest])):
            heapq.heappush(q, adj[dest][i])
        visit.add(dest)

print(cum_weight % mod)
