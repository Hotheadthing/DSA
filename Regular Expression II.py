A = "aab"
B = "c*a*b"
A = "acz"
B = "a.a"
A = "baaaaaabaaaabaaaaababababbaab"
B = "..a*aa*a.aba*a*bab*"
len_A = len(A)
len_B = len(B)

def dfs(n,m):
    dp = [[False for i in range(n+1)] for j in range(m+1)]
    dp[0][0] = True

    for i in range(1,len(dp[0])):
        if B[i-1] == "*":
            dp[0][i] = dp[0][i-2]

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if A[i-1] == B[j-1] or B[j-1] == ".":
                dp[i][j] = dp[i-1][j-1]
            elif B[j-1] == "*":
                dp[i][j] = dp[i][j-2]
                if B[j-2] == A[i-1] or B[j-2] == ".":
                    dp[i][j] = dp[i][j] | dp[i-1][j]
            else:
                dp[i][j] = False

    print(dp)



dfs(len_B,len_A)