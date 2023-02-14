import sys
sys.setrecursionlimit(10**6)
A = 2
B = 2

# D = []
#
# for i in range(A):
#     x = ""
#     y = ""
#     z = ""
#     if i == 0:
#         D.append(str(i))
#     else:
#         for j in range(len(D[i-1])):
#             if D[i-1][j] == "0":
#                 x = "01"
#                 z += x
#             else:
#                 y = "10"
#                 z += y
#         D.append(z)
#
# print(D[-1][B-1])

def sym(n,k):
    if k == 1:
        return 0
    parent = (k+1) // 2
    prev_val = sym(n-1,parent)
    if k % 2 == 1:
        return prev_val
    else:
        return 1 - prev_val

x = sym(A,B)
print(x)

