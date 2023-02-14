import heapq
A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
heapq.heapify(A)
total_combine_cost = 0
while len(A) != 1:
    rope1 = heapq.heappop(A)
    rope2 = heapq.heappop(A)
    combine_cost = rope1 + rope2
    total_combine_cost += combine_cost
    heapq.heappush(A, combine_cost)

print(total_combine_cost)
