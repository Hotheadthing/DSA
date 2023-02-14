A = [60, 100, 120]
B = [10, 20, 30]
C = 50
# A = [10, 20, 30, 40]
# B = [12, 13, 15, 19]
# C = 10


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
                print(K)
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# print(knapSack(C,B,A,len(A)))

# ************ Optimised ****************
def knapSack(W, wt, val, n):
    dp = [0 for i in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):
            # print(f"val of w is {w}")
            # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]

print(knapSack(C,B,A,len(A)))