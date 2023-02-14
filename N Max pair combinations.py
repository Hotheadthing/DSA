import heapq

A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
A = [1, 2, 3, 4]
B = [1, 2, 5, 6]
A = [2, 4, 1, 1]
B = [-2, -3, 2, 4]
A = [ 3, 4 ]
B = [ 3, 4 ]
hmap = {}
heap = []
ans = []
heapq.heapify(heap)

A.sort()
B.sort()

up = len(A)-1
dwn = len(A)-1

heapq.heappush(heap, (-(A[up]+B[dwn]), up, dwn))
hmap.__setitem__((up,dwn),1)

while len(ans) != len(A):
    val, u, d = heapq.heappop(heap)
    ans.append(-val)
    # print(ans)
    # print(val, u, d)
    if u > 0 and d >= 0:
        if (u-1,d) not in hmap:
            hmap.__setitem__((u-1,d),1)
            heapq.heappush(heap,(-(A[u-1]+B[d]), u-1,d))
    if u >= 0 and d > 0:
        if (u,d-1) not in hmap:
            hmap.__setitem__((u,d-1),1)
            heapq.heappush(heap, (-(A[u]+B[d-1]), u, d-1))

print(ans)
print(heap)






