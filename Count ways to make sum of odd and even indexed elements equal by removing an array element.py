A = [2, 1, 6, 4]
L = len(A)
Count = 0
for i in range(L):
    B = []
    E_Sum = 0
    O_Sum = 0
    for digit in A:
        B.append(digit)
    del B[i]
    for j in range(len(B)):
        if j % 2 == 0:
            E_Sum += B[j]
        else:
            O_Sum += B[j]
    if E_Sum == O_Sum:
        Count += 1
print(Count)










