# A = [1, 2, 1, 3, 4, 3]
# B = 3

A = [1]
B = 1
result = []
length = len(A) - B + 1

if B > len(A):
    result = result
else:
    A_map = {}
    for i in range(B):
        if A[i] not in A_map:
            A_map.__setitem__(A[i], 1)
        else:
            A_map[A[i]] += 1

    result.append(len(A_map))
    for i in range(1, length):
        r = i + (B - 1)
        if A[r] not in A_map:
            A_map.__setitem__(A[r], 1)
        else:
            A_map[A[r]] += 1
        A_map[A[i - 1]] -= 1
        if A_map[A[i - 1]] == 0:
            A_map.pop(A[i - 1])
        result.append(len(A_map))
print(result)





















# else:
#     for i in range(length):
#         A_map = {}
#         l = i
#         r = i + B
#         x = A[l:r]
#         for d in range(len(x)):
#             if x[d] not in A_map:
#                 A_map.__setitem__(x[d], 1)
#             else:
#                 A_map[x[d]] += 1
#         result.append(len(A_map))
# print(result)






