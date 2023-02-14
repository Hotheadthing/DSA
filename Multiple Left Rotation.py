A = [ 4, 74, 35, 16, 100, 77, 50, 51, 31, 29, 67, 12, 43, 31, 83, 2, 85, 85, 39, 27, 64, 86, 5 ]
length = len(A)
# print(length)
B = [73]
C = []
for digit in B:
    if digit > length:
        A = A
        while digit > length:
            digit = digit - length
        Y = A[0:digit]
        E = A[digit:]
        D = [*E,*Y]
        C.append(D)
    else:
        A = A
        Y = A[0:digit]
        E = A[digit:]
        D = [*E, *Y]
        C.append(D)

print(C)
