A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']

for d in range(len(A)):
    A[d] = ord(A[d])
    if A[d] >= 65 and A[d] < 90:
        y = (A[d]^32)
        A[d] = chr(y)
    else:
        A[d] = chr(A[d])
print(A)

