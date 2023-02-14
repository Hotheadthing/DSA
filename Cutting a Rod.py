A = [3, 4, 1, 6, 2]
# A = [1, 5, 2, 5, 6]
l = len(A)

def unbounded(n,val):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    print(dp)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j >= i:
                dp[i][j] = max(dp[i-1][j],val[i-1]+dp[i][j-i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][n])

unbounded(l,A)