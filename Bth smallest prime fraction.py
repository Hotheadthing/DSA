import heapq
A = [1, 2, 3, 5]
B = 3
A = [1, 7]
B = 1
A = [ 719, 983, 9293, 11321, 14447, 16411, 17881, 22079, 28297 ]
B = 42

arr = []
heapq.heapify(arr)

for i in range(1,len(A)):
    heapq.heappush(arr, (1/A[i], 0, i))

ans = []
while B > 0:
    if len(arr) == 0:
        break
    _, p, q = heapq.heappop(arr)
    B -= 1
    if B == 0:
        ans = [A[p], A[q]]  # Return will work
        print(ans)
    p += 1
    if p < q:
        heapq.heappush(arr, (A[p]/A[q], p, q))

print(ans)




