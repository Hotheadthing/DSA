A = 10
B = [6, 7]
C = [5, 5]
A = 10
B = [5]
C = [10]

A = 80
B = [ 14, 13, 7, 5, 5, 7, 13, 16, 17, 1 ]
C = [ 10, 20, 9, 4, 15, 4, 4, 1, 15, 2 ]


def unboundedKnapsack(W, n, val, wt):
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[W]


print(unboundedKnapsack(A, len(B), B, C))