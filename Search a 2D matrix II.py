# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5
# matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#           [18, 21, 23, 26, 30]]
# target = 20
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
target = 19
search = 0
for i in range(len(matrix[0])):
    if matrix[0][i] > target:
        search = i-1
        break
    else:
        search = len(matrix[0]) - 1
# print(search)

flag = False
search2 = 0
for j in range(len(matrix)):
    if matrix[j][search] == target:
        flag = True
        break
    else:
        if matrix[j][search] > target:
            search2 = j
    if target in matrix[j]:
        flag = True
        break
print(flag)