from collections import deque
A = [
       [0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 1, 1, 0]
     ]
A = [
       [1, 0, 0],
       [0, 0, 0],
       [0, 0, 0]
     ]
ones = []

rows = len(A)
colm = len(A[0])

for i in range(rows):
    for j in range(colm):
        if A[i][j] == 1:
            ones.append([i,j,0])

# print(ones)

def bfs(adj):
    q = deque()
    visit = {}
    for i in range(len(adj)):
        q.append(adj[i])
    while q:
        x,y,d = q.popleft()
        visit.__setitem__((x,y),d)
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        for dx,dy in directions:
            x_co = dx + x
            y_co = dy + y
            if x_co in range(rows) and y_co in range(colm):
                if A[x_co][y_co] == 0 and (x_co,y_co) not in visit:
                    dist = abs(x_co-x) + abs(y_co-y) + d
                    A[x_co][y_co] = dist
                    q.append([x_co,y_co,dist])
                    visit.__setitem__((x_co,y_co),dist)


bfs(ones)

for i in range(len(ones)):
    x = ones[i][0]
    y = ones[i][1]
    A[x][y] = 0

print(A)



