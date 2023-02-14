
# A = "acz"
# B = "a?a"
# A = "aab"
# B = "c*a*b"
# A = "acz"
# B = "a.a"
# A = "a"
# B = "?"
# A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# B = "*"
# A = "bcaccbabaa"
# B = "bb*c?c*?"
# A = "cc"
# B = "***??******c"
# A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# B = "*b"
# A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# B = "a**************************************************************************************"
A = "bcaabacaba"
B = "b**?*?ab"
A = "ac"
B = "ab*c"
A = "baaaaaabaaaabaaaaababababbaab"
B = "..a*aa*a.aba*a*bab*"
# A = "aaa"
# B = "a*"
A = "cc"
B = "?"
C = ""
i = 0
while i < len(B):
    if B[i] != "*":
        C+=B[i]
        i+=1
    else:
        while i < len(B) and B[i] == "*":
            # print(i)
            i += 1
        C+= "*"
print(C)
len_C = len(C)
len_A = len(A)
def dfs(n,m):
    dp = [[False for i in range(len(C)+1)] for j in range(len(A)+1)]
    dp[0][0] = True
    if C[0] == "*":
        dp[0][1] = True

    # print(dp)
    # A = bcaabacaba
    # B = b*?*?ab
    for i in range(1,len(A)+1):
        for j in range(1,len(C)+1):
            # print(B[j-1])
            if (C[j-1] == "?") or (A[i-1] == C[j-1]):
                # print(A[i-1],C[j-1],dp[i-1][j-1])
                dp[i][j] = dp[i-1][j-1]
                # print(dp[i][j])
            else:
                if C[j-1] == "*":
                    # print(A[i - 1], C[j - 1], dp[i - 1][j],dp[i][j-1],j)
                    dp[i][j] = (dp[i-1][j]) or (dp[i][j-1])
                    # print(dp[i][j])

    print(dp)
    print(dp[len_A][len_C])
    # print(dp[m][n])
    # print(len(dp),n+1)
    # print(len(dp[0]),m+1)
    # return dp[n][m]


val = dfs(len_A,len_C)
# if val == True:
#     print(1)
# else:
#     print(0)