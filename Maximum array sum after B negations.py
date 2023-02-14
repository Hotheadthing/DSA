import heapq

A = [24, -68, -29, -9, 84]
B = 4
A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
B = 10

heapq.heapify(A)
for i in range(B):
    min_element = heapq.heappop(A)
    element_added = - min_element
    heapq.heappush(A, element_added)

max_sum = 0
for i in range(len(A)):
    max_sum += A[i]

print(max_sum)


