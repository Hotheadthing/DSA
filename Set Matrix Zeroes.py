# matrix = [[1,1,1],
#           [1,0,1],
#           [1,1,1]]
matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
row_len = len(matrix[0])
col_len = len(matrix)
result = []
for i in range(col_len):
    for j in range(row_len):
        if matrix[i][j] == 0:
            result.append([i,j])
print(result)

for i in range(len(result)):
    x = result[i][1]
    y = result[i][0]
    for j in range(col_len):
        matrix[j][x] = 0
    for k in range(row_len):
        matrix[y][k] = 0
print(matrix)

