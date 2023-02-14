A = [1, 5, -3, 4, -2]
B = 2
C = 1
D = -1
A = [3, 2, 1]
B = 1
C = -10
D = 3
A = [ -21, 34, 3, 46, 8, -47, -47 ]
B = -13
C = 10
D = 9

def dfs(x,y,z,n):
    l_max = [0] * n
    l_max[0] = x*A[0]
    for i in range(1,n):
        l_max[i] = max(l_max[i-1],A[i]*x)

    r_max = [0] * n
    r_max[n-1] = z*A[n-1]
    for j in range(n-2,-1,-1):
        r_max[j] = max(r_max[j+1],A[j]*z)

    ans = -999999999999
    for k in range(n):
        ans = max(ans,l_max[k] + (y*A[k]) + r_max[k])

    return ans


print(dfs(B,C,D,len(A)))

























# result = -99999999999
# def dfs(i,j,k,result):
#     if k > len(A)-1:
#         j += 1
#         return False
#     if j > len(A)-1:
#         i += 1
#         return False
#     if i > len(A)-1:
#         return False
#
#     result = max(result,(index_B[i] + index_C[j] + index_D[k]))
#     print(result,index_B[i],index_C[j],index_D[k])
#     dfs(i,j,k+1,result)
#     if k == len(A) -1:
#         k = j+1
#     dfs(i,j+1,k,result)
#     if j == len(A)-1:
#         j = i+1
#     dfs(i+1,j,k,result)
#     if i == len(A) -1:
#         return False
#
#
# print(dfs(0,0,0,result))


