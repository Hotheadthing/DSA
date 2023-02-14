import math
A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
# A = [5,5,5,15]
# A = [1]
A = [ 46, 1, 2, 1, 1, 1, 5, 45, 1, 1, 2, 5, 1, 40, 1, 1, 1, 1, 1, 1, 1, 1, 1, 31, 1 ]
# A = [ 1, 31, 1, 1, 1, 1, 14, 2, 1, 1, 1, 2, 22, 1, 11, 1, 1, 1, 1, 23, 1, 1, 11, 1, 11 ]
# A = [ 42, 2, 1, 6, 2, 2, 16, 1, 4, 2, 1, 1, 19, 1, 1, 6, 4, 1, 2, 36, 2, 2, 1, 2, 34 ]
# A = [ 9, 3, 1, 1, 3, 30, 3, 2, 1, 3, 1, 2, 1, 44, 11, 1, 1, 1, 1, 19, 3, 3, 11, 1, 33 ]
n = len(A)
A.sort(reverse=True)
arr = []
size = math.floor(math.sqrt(n))

mmap = {}

for i in range(len(A)):
    if A[i] not in mmap:
        mmap.__setitem__(A[i],1)
    else:
        mmap[A[i]] += 1
# print(mmap)
for i in range(size+1):
    x = A[i]
    # print(f"the value of x is {x}")
    if mmap[x] > 0:
        arr.append(x)
        for j in range(n):
            gcd = math.gcd(x,A[j])
            print(x,A[j],gcd)
            mmap[gcd] -= 1
            print(f"the value of freq map {mmap}")
        if mmap[gcd] == 0:
            A.remove(gcd)
        # print(A)

# for d in mmap:
#     if mmap[d] > 0:
#         arr.append(d)
print(arr)




####################### Working #####################################

# def gcd(A, B):
#     if B == 0:
#         return A
#
#     return gcd(B, A%B)
# A.sort(reverse=True)
# n = len(A)
#
# dict_A = {}
# result = []
#
#
# for i in A:
#     if i in dict_A and dict_A[i] > 0:
#         dict_A[i] -= 1
#     else:
#         for j in result:
#             print(f"the value of j is {j}")
#             gcd_val = gcd(i, j)
#             print(gcd_val)
#             if gcd_val in dict_A:
#                 dict_A[gcd_val] += 2
#             else:
#                 dict_A[gcd_val] = 2
#         result.append(i)
#         print(dict_A)
# #
# # print(result)
#
#
#
#
