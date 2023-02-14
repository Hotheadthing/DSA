from collections import deque

A = [
       [0, 1, 0],
       [0, 0, 1],
       [1, 0, 0]
     ]

# A = [
#        [1, 1, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [1, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0],
#        [1, 0, 1, 0, 1]
#      ]

row = len(A)
col = len(A[0])
visit = set()
islands = 0

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visit.add((r,c))
    while q:
        ro,co = q.popleft()
        directions = [[-1,0],[0,-1],[1,0],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]
        for dr,dc in directions:
            r = ro + dr
            c = co + dc
            if r in range(row) and c in range(col) and A[r][c] == 1 and (r,c) not in visit:
                q.append((r,c))
                visit.add((r,c))


for i in range(row):
    for j in range(col):
        if A[i][j] == 1 and (i,j) not in visit:
            bfs(i,j)
            islands += 1

print(islands)












