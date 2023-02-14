import heapq
A = [3, 2, 3]
B = 4
A = [1,2,1]
B = 2
A = [355,667]
B = 867
heapq.heapify(A)
arr = []
consumed = 0
for i in range(len(A)):
    if len(A) == 0:
        break
    val = heapq.heappop(A)
    if val <= B:
        ate = val//2
        consumed += ate
        left = val - ate
        if len(A) != 0:
            n = heapq.heappop(A)
            n = n+left
            heapq.heappush(A,n)
        else:
            break
    else:
        break

print(consumed)







