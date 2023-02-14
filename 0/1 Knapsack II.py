A = [6, 10, 12]
B = [10, 20, 30]
C = 50
# A = [1, 3, 2, 4]
# B = [12, 13, 15, 19]
# C = 10
# A = [2, 1, 3]
# B = [3, 2, 4]
# C = 5
A = [ 6, 1, 3, 9, 7, 1, 3, 5, 9, 7, 6, 1, 10, 1, 1, 7, 2 ]
B = [ 44, 49, 30, 24, 35, 5, 7, 41, 17, 27, 32, 9, 45, 40, 27, 24, 38 ]
C = 297   #69
n = len(B)

summ = 0
for v in A:
    summ += v
# print(summ)
def knapsack(W,n):
    dp = [[999999999 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,W+1):
            if j == A[i-1]:
                dp[i][j] = min(dp[i-1][j],B[i-1]+dp[i-1][j-A[i-1]])
            elif j > A[i-1]:
                if dp[i-1][j-A[i-1]] != 999999999:
                    dp[i][j] = min(dp[i - 1][j], B[i - 1] + dp[i - 1][j - A[i - 1]])
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n]


val = (knapsack(summ,len(B)))
for i in range(len(val)-1,-1,-1):
    if val[i] <= C:
        print(i)
        break
