A = [15, 10, 6]
A = [14, 10, 4]
A = [ 8, 4, 5, 7, 6, 2 ]

n = len(A)
summ = 0
for val in A:
    summ += val
summ = summ//2
dp = [[n+1 for i in range(summ+1)] for j in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for i in range(1,n+1):
    for j in range(1,summ+1):
        if A[i-1] <= j:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-A[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
for k in range(summ,-1,-1):
    if dp[n][k] < n:
        print(dp[n][k])


























#     if len(arr) == 1:
#         return arr.copy()
#
#     for i in range(len(arr)):
#         val.append(arr.pop(0))
#         ans = permute(arr,val)
#         print(ans,val)
#         if ans != None:
#             for x in ans:
#                 temp = x
#                 for d in val:
#                     if temp - d >= 0 or d- temp >= 0:
#                         v = abs(temp-d)
#                         hmap.__setitem__((temp,d),v)
#                         temp = v
#                     else:
#                         v = x + d
#                         hmap.__setitem__((temp,d),v)
#                         temp = v
#             for d in val:
#                 arr.append(val.pop(0))
# permute(A,[])





