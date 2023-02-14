A = [ [1, 1],
      [1, 1] ]
# A=[
#   [8, 9, 9, 1, 7],
#   [5, 5, 10, 1, 0],
#   [7, 7, 5, 8, 6],
#   [7, 3, 7, 9, 2],
#   [7, 7, 8, 10, 6]
# ]


length = len(A)
result = 0
for i in range(length):
      for j in range(length):
            tl = (i+1)*(j+1)
            br = (length-i)*(length-j)
            total = tl * br
            result += (total * A[i][j])
print(result)

