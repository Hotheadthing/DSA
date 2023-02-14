import heapq

A = [1, 40, 2, 3]
B = 2
A = [2, 1, 17, 10, 21, 95]
B = 1
arr = []
temp_arr = []
for i in range(B+1):
    temp_arr.append(A[i])

heapq.heapify(temp_arr)
arr.append(heapq.heappop(temp_arr))

for i in range(B+1,len(A)):
    temp_arr.append(A[i])
    heapq.heapify(temp_arr)
    arr.append(heapq.heappop(temp_arr))

for i in range(len(temp_arr)):
    arr.append(heapq.heappop(temp_arr))

print(arr)
