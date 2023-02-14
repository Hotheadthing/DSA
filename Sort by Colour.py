A = [0, 1, 2, 0, 1, 2]
zero = []
one = []
two = []

for i in range(len(A)):
    if A[i] == 0:
        zero.append(A[i])
    elif A[i] == 1:
        one.append(A[i])
    else:
        two.append(A[i])

x = zero + one + two
print(x)