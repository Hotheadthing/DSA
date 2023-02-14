A = "aba"
A = "aab"
A = "abcde"
A = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
len_A = len(A)
C = [[0 for i in range(len_A)] for j in range(len_A)]
P = [[False for k in range(len_A)] for l in range(len_A)]

w = 0
x = 0
y = 0

for i in range(len_A):
    C[i][i] = 0
    P[i][i] = True

for y in range(2,len_A+1):
    for i in range(len_A+1-y):
        w = y + i - 1

        if y == 2:
            P[i][w] = (A[i] == A[w])
        else:
            P[i][w] = (A[i]==A[w]) and P[i+1][w-1]

        if P[i][w] == True:
            C[i][w] = 0
        else:
            C[i][w] = 999999999999
            for x in range(i,w):
                C[i][w] = min(C[i][w],C[i][x] + C[x+1][w] +1)

print(C[0][len_A-1])
























def is_palindrome(q):
    return q == q[::-1]


def dfs(i,j):
    if i >= j or is_palindrome(A[i:j+1]):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 9999999999

    for k in range(i,j):
        dp[i][j] = min(dp[i][j], dfs(i,k) + dfs(k+1,j) + 1)

    return dp[i][j]

