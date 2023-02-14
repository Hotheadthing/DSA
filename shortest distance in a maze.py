import heapq
A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]
A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]
A = [
  [1, 1, 0, 1],
  [0, 0, 0, 1],
  [1, 0, 0, 1],
  [0, 0, 1, 0]
]
B = [ 1, 1 ]
C = [ 2, 1 ]
A = [
  [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
B = [ 7, 5 ]
C = [ 4, 2 ]

rows = len(A)
colms = len(A[0])
q = []
heapq.heapify(q)
heapq.heappush(q,(0,B[0],B[1]))
visit = set()
ans = -1
while q:
    d,x,y = heapq.heappop(q)
    visit.add((x,y))
    directions = [[0,1],[0,-1],[-1,0],[1,0]]
    for dx,dy in directions:
        x_co = x + dx
        y_co = y + dy
        # print(f"dx and dy are {dx},{dy} and x and y are {x},{y} d is {d}")
        count = 0
        while x_co in range(rows) and y_co in range(colms) and A[x_co][y_co] != 1:
            x_co += dx
            y_co += dy
            count += 1
        val = (x_co-dx,y_co-dy)
        if val[0] == C[0] and val[1] == C[1]:
            if ans == -1:
                ans = d + count
            else:
                ans = min(ans,d+count)
        if val not in visit:
            visit.add(val)
            heapq.heappush(q,(count+d,val[0],val[1]))

print(ans)


