# A = "abababab"
A = "aaaa"
A = "abcaabcaab"
# A = "hqhq"
# A = "abababababb"
n = len(A)
arr = [0] * n
j = 0
for i in range(1,len(A)):
    if A[i] == A[j]:
        arr[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            arr[i] = 0
        else:
            while A[i] != A[j]:
                if j == 0:
                    j = -1
                    break
                else:
                    j = arr[j-1]
            arr[i] = j + 1
            j += 1
print(arr)
print(len(A)-arr[-1])











#
# n = len(A)
# lps = [0] * n
# for i in range(1, n):
#     x = lps[i - 1]
#     while A[x] != A[i]:
#         if x == 0:
#            x = -1
#            break
#
#         x = lps[x - 1]
#         # print(x,i)
#         # print(A[x],A[i])
#
#     lps[i] = x + 1
# # print(n - lps[-1])
# print(lps)
