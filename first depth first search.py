from collections import deque
# A = [1, 1, 2]
# B = 1
# C = 2
# A = [1, 1, 2]
# B = 2
# C = 1
A = [ 1, 1, 1, 3, 3, 2, 2, 7, 6 ]
B = 9
C = 1   #1

adjacent = [[] for i in range(len(A)+1)]
# print(adjacent)

for i in range(len(A)):
    adjacent[A[i]].append(i+1)

print(adjacent)

def bfs(strt,des,arr):
    q = deque()
    visit = set()
    q.append(arr[strt])
    visit.add(strt)

    while q:
        val = q.popleft()
        for i in range(len(val)):
            if val[i] not in visit:
                q.append(arr[val[i]])
                visit.add(val[i])
                # print(q)
                # print(visit)
            if val[i] == des:
                return True
    return False

print(bfs(C,B,adjacent))



