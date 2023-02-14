from collections import deque
import sys
sys.setrecursionlimit(10**6)
x = 2
y = 3
N = 1
R = 1
A = [2]
B = [3]
x = 1
y = 1
N = 1
R = 1
A = [1]
B = [1]
x = 61
y = 91
N = 6
R = 2
A = [ 53, 42, 27, 34, 58, 29 ]
B = [ 16, 54, 33, 40, 30, 23 ]  #YES
x = 7
y = 91
N = 8
R = 7
A = [ 1, 7, 1, 7, 1, 5, 1, 6 ]
B = [ 25, 4, 74, 14, 90, 58, 37, 4 ] #NO
# directions = [[1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,0],[-1,1],[-1,-1]]
visited = [[0 for i in range(y+1)] for j in range(x+1)]
# print(visited)
for i in range(N):
    x1 = A[i]
    y1 = B[i]
    # print(x,y)
    directions = [[R, 0], [R, R], [R, -R], [0, R], [0, -R], [-R, 0], [-R, R], [-R, -R]]
    for dx, dy in directions:
        x_co = dx + x1
        y_co = dy + y1
        if x_co in range(len(visited)) and y_co in range(len(visited[0])) and visited[x_co][y_co] != 1:
            visited[x_co][y_co] = 1

# print(visited)
if visited[0][0] == 1 or visited[x][y] == 1:
    print("NO")

def bfs(adj,a,b):
    q = deque()
    q.append((0,0))
    if adj[0][0] == 1:
        return "NO"
    adj[0][0] = 1
    while q:
        x1,y1 = q.popleft()
        if x1 == a and y1 == b:
            print(adj)
            return "YES"
        directions = [[1, 0], [1, 1], [0, 1], [1, -1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]
        for dx,dy in directions:
            x_co = dx+x1
            y_co = dy+y1
            if x_co in range(len(adj)) and y_co in range(len(adj[0])) and adj[x_co][y_co] != 1:
                q.append((x_co,y_co))
                adj[x_co][y_co] = 1
    return "NO"

print(bfs(visited,x,y))


