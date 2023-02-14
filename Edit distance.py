A = "Anshuman"
B = "Antihuman"
# A = "abad"
# B = "abac"
# A = "aaa"
# B = "aa"
# A = "abac"
# B = "aac"
A = "b"
B = "a"
# A = "aaa"
# B = "aa"
# A = "bbbaabaa"
# B = "aababbabb"
def dfs(n, m):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1,len(dp[0])):
        dp[0][i] = i
    # print(dp)
    for j in range(1,len(dp)):
        dp[j][0] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if B[j - 1] == A[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],dp[i-1][j-1]) +1

    return dp[m][n]



(dfs(len(B), len(A)))



