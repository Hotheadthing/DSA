from collections import deque
A = 5
B = [  [1, 2],
        [1, 3],
        [2, 3],
        [1, 4],
        [4, 5]
     ]
# A = 3
# B = [  [1, 2],
#         [1, 3]
#      ]
# A = 3
# B = [
#   [1, 2],
#   [1, 3],
#   [2, 3]
# ]

# A = 4
# B = [
#   [1, 2],
#   [2, 3],
#   [3, 4]
# ]

arr = [[] for i in range(A+1)]

for i in range(len(B)):
    arr[B[i][0]].append(B[i][1])
    arr[B[i][1]].append(B[i][0])
print(arr)


def bfs(ind,check,adj):
    q = deque()
    q.append((ind,-1))
    visit.add(ind)

    while q:
        cur,prev = q.popleft()
        for val in adj[cur]:
            if val not in check:
                check.add(val)
                q.append((val,cur))
            elif prev != val:
                return True
    return False


visit = set()
for i in range(1,A+1):
    if i not in visit:
        if bfs(i,visit,arr) == True:
            print(1)
            break






