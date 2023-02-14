A = "aabcc"
B = "dbbca"
C = "aadbbcbcac"
A = "aabcc"
B = "dbbca"
C = "aadbbbaccc"
A = "noUdRp97xFvpifeSXGwOjcVNhHo9N2D"
B = "6iZItw9A3fj86uYx04tvWKLtl9BK"
C = "n6ioUdRpZ97ItwxF9Av3fj86upYxif0eS4XtvWKLtlG9wOBKjcVNhHo9N2D"
len_A = len(A)
len_B = len(B)
len_C = len(C)
print(len_A,len_B,len_C)
if len_A + len_B != len_C:
    print(0)

dp = [[False for i in range(len_B+1)] for j in range(len_A+1)]
# print(dp)

for i in range(len_A+1):
    for j in range(len_B+1):
        if i == 0 and j == 0:
            dp[i][j] = True

        elif i == 0:
            if C[j-1] == B[j-1]:
                dp[i][j] = dp[i][j-1]

        elif j == 0:
            if C[i-1] == A[i-1]:
                dp[i][j] = dp[i-1][j]

        elif C[i+j-1] == A[i-1] and B[j-1] != C[i+j-1]:
                dp[i][j] = dp[i-1][j]
        elif C[i+j-1] == B[j-1] and C[i+j-1] != A[i-1]:
                dp[i][j] = dp[i][j-1]
        elif C[i+j-1] == B[j-1] and C[i+j-1] == A[i-1]:
                dp[i][j] = dp[i][j-1] | dp[i-1][j]

print(dp[len_A][len_B])