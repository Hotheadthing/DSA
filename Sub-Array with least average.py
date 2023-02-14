A=[3, 7, 5, 20, -10, 0, 12]
B=2
# A = [ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ]
# B = 9
n = len(A)
q = 0
Sum = 0
Index = 0
D = []
for i in range(n):
    D.append(A[i])
for i in range(len(A)):
    if i == 0:
        A[i] = A[i]
    else:
        A[i] = A[i] + A[i-1]
if B ==1:
    length = n
else:
    D = D[:-B+1]
    length = len(D)
for i in range(length):
    if i == 0:
        Sum = A[B-1]
        Index = i
    else:
        z = A[i+(B-1)] - A[i-1]
        if z < Sum:
            Sum = z
            Index = i
print(Index)


