from collections import deque
A = [ -1, 0, 0, 0, 3 ]
# A = [-1, 0]
# A = [-1, 0, 0]
# A = [ -1, 0, 0, 1, 2, 1, 5 ]
# A = [-1,0,1,2,2,4]
A = [ -1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32, 15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20, 4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49, 90, 6, 81, 73, 10, 8, 16 ]
adj = {c:[] for c in range(len(A))}

for i in range(1,len(A)):
    adj[A[i]].append(i)
    adj[i].append(A[i])

q = deque()
q.append((0, 0))
visited = set()
arr = 0
while q:
    val, ind = q.popleft()
    if ind not in visited:
        arr = (ind,val)
        for node in adj[ind]:
            nxt = val + 1
            q.append((nxt, node))
    visited.add(ind)

visit = set()
q.append((0,arr[0]))
depth = 0
while q:
    v, index = q.popleft()
    if index not in visit:
        depth = v
        for nod in adj[index]:
            dpth = v+1
            q.append((dpth,nod))
    visit.add(index)

print(depth)


def bfs(node,v):
    visited = set()
    q = deque()
    q.append((node,v))
    visited.add(node)
    n = 0
    dis = 0
    while q:
        ind,distce = q.popleft()
        for val in adj[ind]:
            if val not in visited:
                visited.add(val)
                q.append((val,distce+1))
                n = val
                dis = distce + 1
    return n,dis

ans = (bfs(0,0))
result = (bfs(ans[0],0))
print(result[1])






