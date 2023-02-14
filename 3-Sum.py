A = [-1, 2, 1, -4]
B = 1
A = [1, 2, 3]
B = 6
A = [ -10, -10, -10 ]
B = -5
A = [ 5, -2, -1, -10, 10 ]
B = 5
# A = [ 7, 2, -5, 10, -3, 4, 9, 1, -6, -10 ]
# B = 2
A.sort()
print(A)
ans = 999999999999
n = len(A)
for i in range(len(A)-2):
    l = i+1
    r = n-1
    while l < r:
        sum = A[i] + A[l] + A[r]
        if sum == B:
            ans = B
            break
        if abs(ans-B) > abs(sum-B):
            ans = sum
        elif sum > B:
            r -= 1
        else:
            l += 1
print(ans)
# result = 999999999999
# for i in range(1,len(A)):
#     for j in range(i+1,len(A)):
#         sum = A[i-1] + A[i] + A[j]
#         if sum == B:
#             result = B
#             break
#         if abs(sum-B) < abs(result-sum):
#             result = sum
# print(result)






