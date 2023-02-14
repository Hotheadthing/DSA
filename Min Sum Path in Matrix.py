A = [
       [1, 3, 2],
       [4, 3, 1],
       [5, 6, 1]
     ]

# A = [
#        [1, -3, 2],
#        [2, 5, 10],
#        [5, -5, 1]
#      ]

for i in range(1,len(A)):
    A[i][0] = A[i][0] + A[i-1][0]

for j in range(1,len(A[0])):
    A[0][j] = A[0][j] + A[0][j-1]

print(A)


for i in range(1,len(A)):
    for j in range(1,len(A[0])):
        A[i][j] = A[i][j] + min(A[i-1][j],A[i][j-1])

print(A[len(A)-1][len(A[0])-1])