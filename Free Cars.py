import heapq
A = [1, 3, 2, 3, 3]
B = [5, 6, 1, 3, 9]

A = [3, 8, 7, 5]
B = [3, 1, 7, 19]

A = [ 1, 7, 6, 2, 8, 4, 4, 6, 8, 2 ]
B = [ 8, 11, 7, 7, 10, 8, 7, 5, 4, 9 ]

arrangement = []

arr = []
for i in range(len(A)):
    arr.append([A[i],B[i]])


arr.sort(key= lambda x:x[0])
# print(arr)

for i in range(len(arr)):
    if len(arrangement) < arr[i][0]:
        heapq.heappush(arrangement,arr[i][1])
    else:
        if arrangement[0] < arr[i][1]:
            heapq.heappop(arrangement)
            heapq.heappush(arrangement,arr[i][1])
# print(arrangement)

max_profit = 0

for x in arrangement:
    max_profit += x

print(max_profit)


