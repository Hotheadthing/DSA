A = [
         [5, 4],
         [6, 4],
         [6, 7],
         [2, 3]
     ]
A = [
         [8, 9],
         [8, 18]
     ]

# A = [
#   [17, 11],
#   [15, 11],
#   [13, 4],
#   [17, 2],
#   [13, 1],
#   [10, 17],
#   [15, 12]
# ]
# A = [
#   [6, 18],
#   [2, 14],
#   [5, 6],
#   [4, 15],
#   [8, 11],
#   [3, 11],
#   [11, 10],
#   [5, 11]
# ]
A.sort(key=lambda x:x[0])
print(A)
arr = []

hmap = {}
for i in range(len(A)):
    arr.append(A[i][1])
    hmap.__setitem__(A[i][0],1)
# print(arr)
print(hmap)
dp = [1 for i in range(len(arr))]
print(dp)

for i in range(1,len(arr)):
    for j in range(i-1,-1,-1):
        if A[i][0] > A[j][0] and arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print (max(dp))