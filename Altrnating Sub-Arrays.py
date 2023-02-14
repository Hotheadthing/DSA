# A = [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
# B = 2  # (2*B + 1)
A = [1, 0, 1, 0, 1]
B = 1
# A = [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1 ]
# B = 1
actual = 2 * B + 1
n = len(A)
result = []
flag = False
if B == 0:
    for j in range(n):
        result.append(j)
else:
    for i in range((n - actual) + 1):
        z = []
        z.append(i)
        # print(f"The value of i is {i}")
        for j in range(1 + i, i + actual, 1):
            # print(j)
            if A[j] != A[z[-1]]:
                z.append(j)
            else:
                continue
        if len(z) == actual:
            result.append(z[(actual + 1) // 2 - 1])
        else:
            continue
print(result)


        # print(flag)
#         if flag == False:
#             result.append(z[(actual + 1) // 2 - 1])
#         else:
#             continue
# print(result)

#             if A[i] != A[i+1] and A[i] == A[i+2]:
#                 z.append(j)
#         if len(z) == 1:
#             continue
#         else:
#             result.append(z[(actual+1)//2 -1])
# print(result)

# conditions to be added:
# -) Currently being limited to fixed range for checking(alternates)
# -) If the array dosent contains alternates, returning of blank.
