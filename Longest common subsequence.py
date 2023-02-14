A = "abbcdgf"
B = "bbadcgf"
A = "aaaaaa"
B = "ababab"
A = "bebdeeedaddecebbbbbabebedc"
B = "abaaddaabbedeedeacbcdcaaed"
len_A = len(A)
len_B = len(B)
print(len_A,len_B)
def dfs(n,m):
    if n >= m:
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[j-1] == B[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])


        print(dp)
    # else:
    #     dp = [[0 for i in range(m+1)] for j in range(n+1)]
    #     for i in range(1,n+1):
    #         for j in range(1,m+1):
    #             if j >= i:
    #                 if A[j-1] == B[i-1]:
    #                     dp[i][j] = dp[i-1][j-1] + 1
    #                 else:
    #                     dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    #             else:
    #                 dp[i][j] = dp[i-1][j]
    #     return dp[n][m]



print(dfs(len_A,len_B))