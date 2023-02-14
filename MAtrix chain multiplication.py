A = [40, 20, 30, 10, 30]
A = [10, 20, 30]

dp = [[-1 for i in range(1000)] for j in range(1000)]


def dfs(i,j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 999999999999
    for k in range(i,j):
        dp[i][j] = min(dp[i][j],dfs(i,k) + dfs(k+1,j) + A[i-1]*A[k]*A[j])

    return (dp[i][j])

print(dfs(1,len(A)-1))


