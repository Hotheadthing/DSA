import heapq

A = 3
B = [6, 5]
# A = 5
# B = [2, 4, 6, 8, 10]

for i in range(len(B)):
    B[i] = -1 * B[i]

heapq.heapify(B)

choclates_eaten = 0
for times in range(A):
    val = -(heapq.heappop(B))
    choclates_eaten += val
    choclates_added = (val/2)
    heapq.heappush(B, -choclates_added.__floor__())

print(choclates_eaten)