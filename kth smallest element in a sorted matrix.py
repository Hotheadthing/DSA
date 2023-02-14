import heapq
A = [ [9, 11, 15],
       [10, 15, 17] ]
B = 6
A = [[5, 9, 11],
     [9, 11, 13],
     [10, 12, 15],
     [13, 14, 16],
     [16, 20, 21]]
B = 12

A = [
  [3, 5, 7, 9],
  [4, 6, 9, 12],
  [5, 9, 12, 16],
  [6, 10, 14, 19]
]
B = 15

arr = []

for i in range(len(A)):
       for j in range(len(A[0])):
              arr.append(A[i][j])

ans = 0
heapq.heapify(arr)
for i in range(B):
       ans = heapq.heappop(arr)

print(ans)




