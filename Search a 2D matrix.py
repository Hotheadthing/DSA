matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

row_len = len(matrix[0])
col_len = len(matrix)

for i in range(col_len):
    if target <= matrix[i][-1]:
        if target in matrix[i]:
            print(True)
            break
        else:
            print(False)
            break


