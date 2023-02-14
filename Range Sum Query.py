A = [ 7, 3, 1, 5, 5, 5, 1, 2, 4, 5 ]
# ans = 12 28 11 38
B = [
  [7, 10],
  [3, 10],
  [3, 5],
  [1, 10]
]
ans = []
for n in range(len(A)):
            if n == 0:
                continue
            else:
                k = (n-1)
                A[n] = A[n] + A[k]
for i in range(len(B)):
  x = B[i]
  if x[0] != 1:
    sum = (A[x[1]-1]) - (A[x[0]-2])
    ans.append(sum)
  else:
    sum = (A[x[1]-1])
    ans.append(sum)
print(ans)



