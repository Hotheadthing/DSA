from collections import deque

A = 7
B = [0, 1, 6, 7, 2, 9, 4, 5]
C = [[1, 2],
     [2, 3],
     [5, 6],
     [5, 7]]
D = 12
A = 5
B = [1, 2, 3, 4, 5]
C = [[1, 5],
     [2, 3]]
D = 6
A = 9
B = [3, 4, 8, 4, 10, 6, 7, 6, 2]
C = [
    [4, 8],
    [4, 9],
    [5, 6]
]
D = 17  # 0
# A = 14
# B = [7, 5, 7, 3, 9, 4, 4, 6, 3, 1, 4, 8, 7, 6]
# C = [
#     [1, 2],
#     [2, 6],
#     [2, 7],
#     [4, 13],
#     [5, 8],
#     [5, 13],
#     [6, 12],
#     [7, 10],
#     [10, 14],
#     [13, 14]
# ]
# D = 2  # 4
adj = {c: [] for c in range(A + 1)}
B.insert(0, 0)
for src, des in C:
    adj[src].append(des)
    adj[des].append(src)

print(adj)

visit = set()


def bfs(ind, sm):
    q = deque()
    q.append(ind)
    visit.add(ind)
    sm += B[ind]
    while q:
        v = q.popleft()
        for val in adj[v]:
            if val not in visit:
                q.append(val)
                sm += B[val]
                visit.add(val)
    return sm


count = 0
for i in range(1, (A + 1)):
    if i not in visit:
        ans = bfs(i, 0)
        if ans >= D:
            count += 1
print(count)

# def bfs(ind, sum):
#     visit.add(ind)
#     sum = B[ind]
#     for val in adj[ind]:
#         if val not in visit:
#             visit.add(val)
#             sum += bfs(val, sum)
#     return sum
#
#
# count = 0
# lvs = 0
# for i in range(1, (A + 1)):
#     if i not in visit:
#         ts = bfs(i, 0)
#         print(ts, i)
#         if ts >= D:
#             count += 1
#
# print(count)
