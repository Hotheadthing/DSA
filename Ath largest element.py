import heapq

A = 4
B = [1, 2, 3, 4, 5, 6]

# A = 2
# B = [15, 20, 99, 1]

arr = []
ans = []

for i in range(len(B)):
    if i < A-1:
        ans.append(-1)
        heapq.heappush(arr,B[i])
    else:
        if len(arr) < A:
            heapq.heappush(arr,B[i])
            val = heapq.heappop(arr)
            ans.append(val)
            heapq.heappush(arr,val)
        else:
            heapq.heappush(arr,B[i])
            heapq.heappop(arr)
            val = heapq.heappop(arr)
            ans.append(val)
            heapq.heappush(arr, val)
print(ans)



