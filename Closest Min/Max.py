A = [ 4, 4, 4, 4, 4 ]
B = []
x = -1
y = -1
length = []
for digits in A:
    B.append(digits)
B.sort()
B_min = B[0]
B_Max = B[-1]
if len(A) == 1 or B_Max == B_min:
    print(1)
else:
    for i in range(len(A)):
        if A[i] == B_min and y == -1:
            x = i
        elif A[i] == B_min and y != -1:
            x = i
            z = abs(y-x)
            length.append(z)
        elif A[i] == B_Max and x == -1:
            y = i
        elif A[i] == B_Max and x != -1:
            y = i
            z = abs(y - x)
            length.append(z)
    length.sort()
    print(length)


