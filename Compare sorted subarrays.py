A = [1, 7, 11, 8, 11, 7, 1]
B = [
    [0, 2, 4, 6]
]
# A = [ 0, 100000 ]
# B = [
#   [0, 0, 0, 0],
#   [1, 1, 1, 1],
#   [0, 1, 0, 1]
#     ]
# A = [1, 3, 2]
# B = [
#     [0, 1, 1, 2]
# ]


A = [ 100000, 100000, 100000, 100000, 100000 ]
B = [
  [0, 3, 1, 4],
  [0, 1, 2, 3],
  [4, 4, 1, 1],
  [1, 3, 0, 0],
  [2, 4, 1, 1]
]
A = [ 5, 3, 4, 4 ]
B = [
  [0, 1, 2, 3]
]

# Optimised Code
A1 = A.copy()
print(A1)
arr = []
for i in range(1,len(A1)):
    A1[i] = A1[i] + A1[i-1]

print(A1)

def if_exist(l1,r1,l2,r2):
    sum = 0
    sum1 = 0
    if l1 == 0:
        sum = A1[r1]
    else:
        sum = A1[r1] - A1[l1-1]

    if l2 == 0:
        sum1 = A1[r2]
    else:
        sum1 = A1[r2] - A1[l2-1]
    sum_map = {}
    sum1_map = {}
    if sum == sum1:
        for i in range(l1,r1+1):
            if A[i] not in sum_map:
                sum_map.__setitem__(A[i],1)
            else:
                sum_map[A[i]] += 1
        for j in range(l2,r2+1):
            if A[j] not in sum1_map:
                sum1_map.__setitem__(A[j],1)
            else:
                sum1_map[A[j]] += 1
        for d in sum1_map:
            if d not in sum_map:
                return 0
            elif sum_map[d] != sum1_map[d]:
                return 0
        return 1
    else:
        return 0



for i in range(len(B)):
    l1 = B[i][0]
    r1 = B[i][1]
    l2 = B[i][2]
    r2 = B[i][3]
    w = if_exist(l1,r1,l2,r2)
    arr.append(w)

print(arr)


































# Code working - Needs optimisation
# arr = []
# for j in range(len(B)):
#     # print(B[j])
#     map_one = {}
#     map_two = {}
#     for i in range(0,len(B[0]),2):
#         x = B[j][i]
#         y = B[j][i+1] + 1
#         if i == 0:
#             for i in range(x,y):
#                 if A[i] not in map_one:
#                     map_one.__setitem__(A[i], 1)
#                 else:
#                     map_one[A[i]] += 1
#         else:
#             for j in range(x, y):
#                 if A[j] not in map_two:
#                     map_two.__setitem__(A[j], 1)
#                 else:
#                     map_two[A[j]] += 1
#     flag = True
#     for d in map_one:
#         if d in map_two:
#             map_two[d] -= 1
#             if map_two[d] == 0:
#                 del map_two[d]
#         else:
#             flag = False
#             break
#     if flag == True:
#         arr.append(1)
#     else:
#         arr.append(0)
#
#
# print(arr)





