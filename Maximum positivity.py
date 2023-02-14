# A = [5, 6, -1, 7, 8]
# A = [1, 2, 3, 4, 5, 6, -1, 1, 2, 3, 4, 5, 6, -1, 1, 2, 3, 4, 5, 6, 7, -1]
A = [ -4970494, -664439, -3649300, -3123623, -6310530, 5544106, -4558683, -2209137, -6016890, 112968 ]
B = []
C = []
count = 1
length = 0
for i in range(len(A)):
    if A[i] > 0 and count == 1:
        B.append(A[i])
    if A[i] > 0 and count == 2:
        C.append(A[i])
    if A[i] < 0 and count == 1:
        count = 2
    if A[i] < 0 and count == 2:
        if len(B) >= len(C):
            C = []
        else:
            B = C
            C = []
print(B)
print(C)

if len(B) >= len(C):
    B = B
else:
    B = C
print(B)


