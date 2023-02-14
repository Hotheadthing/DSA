A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2
A =[
  [1, 3, 5, 7],
  [2, 4, 6, 8]
   ]
B = 10
A =[
  [2, 8, 8, 8],
  [2, 8, 8, 8],
  [2, 8, 8, 8],
   ]
B = 8
n = len(A)
m = len(A[0])

i = 0
j = m - 1
arr = []
while (i < n) and (j >= 0):
    if A[i][j] > B:
        j -= 1
    elif A[i][j] < B:
        i += 1
    else:
        arr.append(i+1)
        arr.append(j+1)
        break

print(arr)
result = []
if len(arr) == 0:
      print(-1)
else:
      for i in range(len(A[0])):
            if A[arr[0]-1][i] == B:
                  result.append(arr[0])
                  result.append(i+1)
                  break
      if len(result) == 0:
            z = (arr[0]*1009) + arr[1]
            print(z)
      else:
            z = (result[0]*1009) + result[1]
            print(z)
