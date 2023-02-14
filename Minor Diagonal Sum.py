A = [[3, 2],
      [2, 3]]
Sum = 0
for i in range(len(A)):
    Sum += A[(len(A) - 1) - i][i]
print(Sum)
