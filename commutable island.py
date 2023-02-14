import heapq

A = 4
B = [[1, 2, 1],
     [2, 3, 4],
     [1, 4, 3],
     [4, 3, 2],
     [1, 3, 10]]
A = 4
B = [  [1, 2, 1],
        [2, 3, 2],
        [3, 4, 4],
        [1, 4, 3]   ]
adj = {c: [] for c in range(A + 1)}
# print(adj)

for src, des, cost in B:
    adj[src].append([cost, des])
    adj[des].append([cost, src])

# print(adj)

visit = set()
q = []
heapq.heapify(q)

for i in range(len(adj[1])):
    heapq.heappush(q, adj[1][i])

visit.add(1)

total_cost = 0

while q:
    cst, dest = heapq.heappop(q)
    if dest not in visit:
        total_cost += cst
        for i in range(len(adj[dest])):
            heapq.heappush(q, adj[dest][i])
        visit.add(dest)

print(total_cost)
