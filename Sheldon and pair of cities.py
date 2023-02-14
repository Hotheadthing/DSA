import heapq
A = 4
B = 6
C = 2
D = [1, 2, 3, 2, 4, 3]
E = [2, 3, 4, 4, 1, 1]
F = [4, 1, 1, 1, 1, 1]
G = [1, 1]
H = [2, 3]
# A = 3
# B = 3
# C = 2
# D = [1, 2, 1]
# E = [2, 3, 3]
# F = [3, 1, 1]
# G = [2, 1]
# H = [3, 2]
A = 15
B = 18
C = 29
D = [ 11, 2, 2, 6, 2, 8, 9, 3, 14, 15, 4, 14, 8, 7, 8, 6, 2, 12 ]
E = [ 2, 1, 1, 2, 1, 1, 7, 3, 2, 13, 2, 1, 6, 1, 7, 1, 2, 10 ]
F = [ 8337, 6651, 29, 7765, 3428, 5213, 6431, 2864, 3137, 4024, 8169, 5013, 7375, 3786, 4326, 6415, 8982, 6864 ]
G = [ 6, 2, 1, 15, 12, 2, 14, 10, 13, 15, 15, 4, 8, 7, 9, 4, 15, 13, 12, 5, 2, 10, 1, 11, 14, 7, 3, 13, 12 ]
H = [ 5, 2, 15, 13, 6, 2, 8, 6, 3, 13, 15, 3, 1, 1, 4, 4, 5, 8, 1, 3, 1, 10, 15, 9, 2, 1, 1, 10, 2 ]
#-1 0 -1 4024 -1 0 8379 -1 -1 4024 0 -1 5213 3786 18415 0 -1 -1 -1 -1 29 0 -1 18583 3137 3786 -1 -1 -1
A = 4
B = 6
C = 2
D = [ 1, 2, 3, 2, 4, 3 ]
E = [ 2, 3, 4, 4, 1, 1 ]
F = [ 4, 1, 1, 1, 1, 1 ]
G = [ 1, 1 ]
H = [ 2, 3 ]
A = 15
B = 18
C = 29
D = [ 11, 2, 2, 6, 2, 8, 9, 3, 14, 15, 4, 14, 8, 7, 8, 6, 2, 12 ]
E = [ 2, 1, 1, 2, 1, 1, 7, 3, 2, 13, 2, 1, 6, 1, 7, 1, 2, 10 ]
F = [ 8337, 6651, 29, 7765, 3428, 5213, 6431, 2864, 3137, 4024, 8169, 5013, 7375, 3786, 4326, 6415, 8982, 6864 ]
G = [ 6, 2, 1, 15, 12, 2, 14, 10, 13, 15, 15, 4, 8, 7, 9, 4, 15, 13, 12, 5, 2, 10, 1, 11, 14, 7, 3, 13, 12 ]
H = [ 5, 2, 15, 13, 6, 2, 8, 6, 3, 13, 15, 3, 1, 1, 4, 4, 5, 8, 1, 3, 1, 10, 15, 9, 2, 1, 1, 10, 2 ]
# -1 0 -1 4024 -1 0 8379 -1 -1 4024 0 -1 5213 3786 18415 0 -1 -1 -1 -1 29 0 -1 18583 3137 3786 -1 -1 -1
adj = {c:[] for c in range(A+1)}
distane = [0 for j in range(A+1)]
con_road = {}
for roads in range(B):
    if (D[roads],E[roads]) not in con_road:
        con_road.__setitem__((D[roads],E[roads]),F[roads])
    else:
        val = con_road[(D[roads],E[roads])]
        if val > F[roads]:
            con_road[(D[roads],E[roads])] = F[roads]
# print(con_road)
for data in con_road:
    adj[data[0]].append((con_road[data],data[1]))
    adj[data[1]].append((con_road[data],data[0]))



def find(src,des,cos):
    visit = set()
    q = []
    heapq.heapify(q)
    heapq.heappush(q,(0,src))
    flag = False
    while q:
        c, node = heapq.heappop(q)
        if node == des:
            cos = c
            flag = True
            break
        if node not in visit:
            for cost,desti in adj[node]:
                heapq.heappush(q,(cost+c,desti))
            visit.add(node)

    if flag:
        return cos
    else:
        return -1


result = []
for quer in range(C):
    val = find(G[quer],H[quer],0)
    result.append(val)

print(result)

