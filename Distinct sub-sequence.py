A = "abc"
B = "abc"
# A = "rabbbit"
# B = "rabbit"
# A = "ABCDE"
# B = "AEC"
# A = "abc"
# B = "dec"
A = "aaaababbababbaabbaaababaaabbbaaabbb"
B = "bbababa"   #22113
len_A = len(A)
len_B = len(B)
# n = 0
# m = 0
def knapsack(n,m,a,b):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    # print(dp)
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(a[j-1],b[i-1])
            if a[j-1] == b[i-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j][i-1],dp[j-1][i])
    print(dp)

    for i in range(1,len(dp)):
        dp[i][m] = i - dp[i][m]

    print(dp)


knapsack(len_A,len_B,A,B)
# print(len_A)
# print(2**28)


arr = [1,2,2,3,4,4,5,5,6,7,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
ans = 0
for val in arr:
    ans+= val

print(ans)


























# def dfs(a,b,i,j,dp):
#     if dp[i][j] != -1:
#         return dp[i][j]
#     if j == 0:
#         dp[i][j] = 1
#     elif i == 0:
#         dp[i][j] = 0
#     else:
#         if a[i-1] != b[j-1]:
#             dp[i][j] = dfs(a,b,i-1,j,dp)
#         else:
#             dp[i][j] = dfs(a,b,i-1,j,dp) + dfs(a,b,i-1,j-1,dp)
#
#     return dp[i][j]
#
# dp = [[-1] * (len(B)+1) for j in range(len_A+1)]
# if m > n :
#     print(0)
# else:
#     print(dfs(A,B,len_A,len_B,dp))
# count = 0
# flag = True
# for k in range(len(A)):
#     if j >= len_B:
#         break
#     if A[i] == B[j]:
#         i += 1
#         j += 1
#     else:
#         if A[i] != B[j]:
#             if len_A > len_B:
#                 len_A -= 1
#                 i += 1
#                 count += 1
#             else:
#                 flag = False
#                 break
#
# print(count,flag)
#
# if flag == False:
#     print(0)
# else:
#     print(2**count + count)
