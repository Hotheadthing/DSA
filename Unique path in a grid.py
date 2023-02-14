A = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
     ]

A = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
     ]

dp = []

for i in range(len(A)):
    arr = []
    for j in range(len(A[0])):
        if A[i][j] == 1:
            arr.append(-1)
        else:
            arr.append(1)
    dp.append(arr)

# print(dp)

for i in range(1,len(dp)):
    if dp[i-1][0] == -1:
        dp[i][0] = -1

for j in range(1,len(dp[0])):
    if dp[0][j-1] == -1:
        dp[0][j] = -1


for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if dp[i][j] == -1:
            continue
        else:
            if dp[i-1][j] != -1 and dp[i][j-1] != -1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif dp[i-1][j] == -1 and dp[i][j-1] != -1:
                dp[i][j] = dp[i][j-1]
            elif dp[i-1][j] != -1 and dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = -1

rows = len(dp)
colm = len(dp[0])

if dp[rows-1][colm-1] == -1:
    print(0)
else:
    print(dp[rows-1][colm-1])




