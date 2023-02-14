A = "bebeeed"
# A = "aedsead"
A = "cbbcacdcdadc"
len_A = len(A)

def dfs(n):
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if l == 2 and A[i] == A[j]:
                dp[i][j] = 2
            elif A[i] == A[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    print(dp)
    print(dp[0][n-1])


# ************************* Recursive Solution *******************
# public int calculateRecursive(char str[],int start,int len){
#         if(len == 1){
#             return 1;
#         }
#         if(len ==0){
#             return 0;
#         }
#         if(str[start] == str[start+len-1]){
#             return 2 + calculateRecursive(str,start+1,len-2);
#         }else{
#             return Math.max(calculateRecursive(str, start+1, len-1), calculateRecursive(str, start, len-1));
#         }
#     }



dfs(len_A)