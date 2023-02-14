A = [ 1, 2, -1, 1, 3, -1, 1, 4 ]
B = [ 1, 2, -1, 1, 3, -1, 1, 4 ]

# for d in A:
#     B.append(d)

for d in range(len(A)):
    if d == 0:
        A[d] = A[d]
    else:
        A[d] = A[d] + A[d-1]
print(A)
maximum = 0
x = -1
for i in range(len(A)):
    if A[i] == 0:
        maximum = max(maximum, i)
        x = -1
    if A[i] < A[i-1]:
        if A[i] in A[:i]:
            y = A.index(A[i])
            if i-y > maximum:
                x = y
                maximum = max(maximum,i-y)
if x == -1 and maximum != 0:
    print(B[0:0 + maximum+1])
elif x != -1:
    print(B[x+1:x + maximum + 1])









