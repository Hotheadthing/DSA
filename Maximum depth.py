from collections import deque
import bisect
A = 5
B = [1, 4, 3, 1]
C = [5, 2, 4, 4]
D = [7, 38, 27, 37, 1]
E = [1, 1, 2]
F = [32, 18, 26]
A = 3
B = [1, 2]
C = [3, 1]
D = [7, 15, 27]
E = [1, 10, 1]
F = [29, 6, 26]
adj = {c:[] for c in range(A+1)}

for i in range(len(B)):
    adj[B[i]].append(C[i])
    adj[C[i]].append(B[i])
print(adj)

stack = deque()
visit = set()
hmap = {}

stack.append((0,1))

while stack:
    lvl,node = stack.popleft()
    if lvl not in hmap:
        if node not in visit:
            v = D[node-1]
            hmap.__setitem__(lvl,[v])
    else:
        if node not in visit:
            v = D[node-1]
            hmap[lvl].append(v)
    if node not in visit:
        for val in adj[node]:
            stack.append((lvl+1,val))
        visit.add(node)

print(hmap)

depth = len(hmap)
result = []
for i in range(len(E)):
    d = E[i] % depth
    val = F[i]
    lst = hmap[d]
    lst.sort()
    grt_ind = bisect.bisect_left(lst,val)
    if grt_ind != len(lst):
        result.append(lst[grt_ind])
    else:
        result.append(-1)





print(result)


