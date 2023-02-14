A = 5
B = [[1, 2],
     [4, 1],
     [2, 4],
     [3, 4],
     [5, 2],
     [1, 3]]

# A = 5
# B = [
#     [1, 2],
#     [2, 3],
#     [3, 4],
#     [4, 5]
# ]
# A = 4
# B = [
#     [1, 2],
#     [2, 3],
#     [4, 3]
# ]

path = []
check = [0] * (A + 1)
check[0] = 1
check[1] = 1
for i in range(A + 1):
    path.append([])

for j in range(len(B)):
    path[B[j][0]].append(B[j][1])

print(path)

for i in range(1, len(path)):
    for j in range(len(path[i])):
        if check[path[i][j]] != 1:
            check[path[i][j]] = 1

print(check)
print(check[A])

# stack = [1]
# check[1] = 1
#
# while len(stack) != 0:
#     val = stack.pop(0)
#     if val == A:
#         break
#     if val not in hmap:
#         break
#     for i in range(len(hmap[val])):
#         # print(hmap[val][i])
#         if check[hmap[val][i]] != 1:
#             stack.append(hmap[val][i])
#             check[hmap[val][i]] = 1
# print(check[-1])
# print(check)
#
# T = len(B)
#
# for cur in range(T):
#     row = B[cur][0]
#     val = B[cur][1]
#     adj_list[row].append(val)
