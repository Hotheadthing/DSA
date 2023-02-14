import math
A = [21, 7, 3, 42, 63]
# A = [12, 15, 18]
pre = []
suff = []
for i in range(len(A)):
    pre.append(0)
    suff.append(0)

def get_gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return get_gcd(a % b, b)
    if b > a:
        return get_gcd(b % a, a)


pre[0] = A[0]
for i in range(1,len(A)):
    pre[i] = get_gcd(A[i],pre[i-1])

# print(pre)

suff[len(A)-1] = A[len(A)-1]
for i in range(len(A)-2,-1,-1):
    suff[i] = get_gcd(A[i],suff[i+1])

# print(suff)

ans = 0
for i in range(len(A)):
    if i == 0:
        ans = max(ans,get_gcd(0,suff[i+1]))
    elif i == len(A)-1:
        ans = max(ans,get_gcd(pre[i-1],0))
    else:
        ans = max(ans,get_gcd(pre[i-1],suff[i+1]))
print(ans)

















# for i in range(len(A)):
#     x = get_gcd(max_left[i],max_right[i])
#     ans = max(ans,x)
#
# print(ans)
# for i in range(len(A)):
#     j = i + 1
#     if i != len(A)-2 and i != len(A)-1:
#         # print(f"the value of i is {i}")
#         gcd = 0
#         while j < len(A)-1:
#             gcd = get_gcd(A[j],A[j+1])
#             j += 1
#         max_right[i] = gcd
#     elif i == len(A) - 2:
#         # print(f"the value of A[i+1] = {A[i+1]}")
#         max_right[i] = A[i+1]
#     elif i == len(A) - 1:
#         # print("the last one")
#         max_right[i] = 0
#
# print(max_right)
#
# for i in range(len(A)-1,-1,-1):
#     j = i - 1
#     if i != 0 and i != 1:
#         gcd = 0
#         while j > 0:
#             gcd = get_gcd(A[j],A[j-1])
#             j -= 1
#         max_left[i] = gcd
#     elif i == 1:
#         max_left[i] = A[0]
#     elif i == 0:
#         max_left[i] = 0
#
# print(max_left)
