from collections import deque
A = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
     ]
A = [[2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]]
hmap = {}
rows = len(A)
cols = len(A[0])
for i in range(rows):
    for j in range(cols):
        if A[i][j] == 2:
            hmap.__setitem__((i,j),0)

q = deque()
for x in hmap:
    q.append(x)

def time_elapsed(Que,te):
    while Que:
        r,c = Que.popleft()
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        for dr,dc in directions:
            ro = r + dr
            co = c + dc
            if ro in range(rows) and co in range(cols) and (ro,co) not in hmap and A[ro][co] == 1:
                time = hmap[(r,c)] + 1
                te = time
                hmap.__setitem__((ro,co),time)
                Que.append((ro,co))
                A[ro][co] = 2
    return te


ans = time_elapsed(q,0)

for i in range(rows):
    for j in range(cols):
        if A[i][j] == 1:
            print(-1)
            break

