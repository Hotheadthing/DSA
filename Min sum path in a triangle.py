A = [
         [2],
         [3, 4,],
         [6, 5, 7],
         [4, 1, 8, 3]
    ]

A = [ [1] ]

A = [
              [8],
             [8,7],
            [7,4,4],
           [9,1,5,5],
          [5,8,2,9,8],
         [2,0,7,4,8,5],
        [8,3,0,6,2,2,5],
       [2,2,7,1,5,2,1,1,0]
   ]


for i in range(len(A)-2,-1,-1):
    for j in range(len(A[i])):
        A[i][j] = A[i][j] + min(A[i+1][j],A[i+1][j+1])

print(A[0][0])