import numpy as np

A = [[1, 2],
     [3, 4]]
# print(A[1][0])
B = [[5, 6],
     [7, 8]]
# [1(5) + 2(7)    1(6) + 2(8)
#  3(5) + 4(7)    3(6) + 4(8)]
# result = []
# x = 0
# y = 0
# z = 0
# a_length = len(A)
# b_length = len(B)
# for i in range(len(A)):
#     for j in range(len(B)):
#         x += A[i][j] * B[j][i]
#     result.append(x)
#     x = 0
# print(result)
C = np.dot(A,B)
print(C)
