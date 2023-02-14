A = 6
B = 2*A
dp = [0 for i in range(B+1)]
print(dp)
dp[0] = 1
dp[2] = 1
print(dp)
for i in range(4,B+1,2):
    for j in range(0,i-1,2):
        dp[i] += dp[j]*dp[i-2-j]
print(dp)