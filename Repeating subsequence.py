A = "abab"
# A = "abba"
len_A = len(A)

dp = [[0 for i in range(len_A+1)] for j in range(len_A+1)]
# dp[0][0] = 0
print(dp)

for i in range(1,len_A+1):
    for j in range(1,len_A+1):
        if i == j:
            continue
        elif A[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp)

val = dp[len_A][len_A-1]

if val >= 2:
    print(1)
else:
    print(0)