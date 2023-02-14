from collections import deque
import heapq

A = 8
B = 8
C = 1
D = 1
E = 8
F = 8
# A = 2
# B = 4
# C = 2
# D = 1
# E = 4
# F = 4
# A = 4
# B = 7
# C = 2
# D = 6
# E = 2
# F = 4 # 2
# A = 7
# B = 13
# C = 2
# D = 8
# E = 3
# F = 4 # 3
# A = 2
# B = 20
# C = 1
# D = 18
# E = 1
# F = 5
matrix = [[0 for i in range(B+1)] for j in range(A+1)]

matrix[C][D] = 1

q = []
visit = set()
heapq.heapify(q)
heapq.heappush(q,(0,C,D))
count = 0
distance = []
def search():
    while q:
        d, x, y = heapq.heappop(q)
        visit.add((x, y))
        d += 1
        directions = [[-2, 1], [-2, -1], [-1, -2], [-1, 2], [1, 2], [1, -2], [2, -1], [2, 1]]
        for dx, dy in directions:
            x_co = x + dx
            y_co = y + dy
            if x_co in range(A+1) and y_co in range(B+1) and (x_co, y_co) not in visit:
                if x_co != 0 and y_co != 0:
                    if x_co == E and y_co == F:
                        distance.append(d)
                        return 1
                    heapq.heappush(q,(d,x_co,y_co))
                    visit.add((x_co, y_co))
    return 0


found = (search())
print(found)
if found == 0:
    print(-1)
else:
    print(distance[0])

