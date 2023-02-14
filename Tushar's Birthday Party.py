A = [2, 4, 6]
B = [2, 1, 3]
C = [2, 5, 3]

# A = [2]
# B = [1]
# C = [2]

W = max(A)
def unboundedknapsack(W,wt,val,n):
    dp = [0 for i in range(W+1)]

    for i in range(W+1):
        for j in range(n):
            if wt[j] <= i:
                if dp[i] == 0:
                    dp[i] = dp[i-wt[j]] + val[j]
                else:
                    dp[i] = min(dp[i], dp[i - wt[j]] + val[j])


    return dp

dp = unboundedknapsack(W,B,C,len(B))

cost = 0
for val in A:
    cost += dp[val]

print(cost)
