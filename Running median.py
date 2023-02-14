import heapq
A = [1, 2, 5, 4, 3]
# A = [5, 17, 100, 11]
min_heap = []
max_heap = []
heapq.heapify(min_heap)
heapq.heapify(max_heap)

median_arr = []

for i in range(len(A)):
    heapq.heappush(max_heap, -A[i])
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    median_arr.append(-max_heap[0])


print(median_arr)


