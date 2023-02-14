import heapq
A = 4
B = 3
C = [2, 1, 1]
A = 4
B = 3
C = [2, 2, 2]

min_heap = []
max_heap = []
for x in C:
    heapq.heappush(max_heap,-x)
    heapq.heappush(min_heap,x)


max_val = 0
temp = A

while temp > 0:
    val = -heapq.heappop(max_heap)
    max_val += val
    if val - 1 > 0:
        heapq.heappush(max_heap,-(val-1))

    temp -= 1

# print(max_val)

min_val = 0
temp = A
while temp > 0:
    val = heapq.heappop(min_heap)
    min_val += val
    if val-1 > 0:
        heapq.heappush(min_heap,val-1)
    temp -= 1

# print(min_val)

print([max_val,min_val])