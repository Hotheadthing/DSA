A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]
p = len(A)
q = len(B)
r = len(C)
a = 0
b = 0
c = 0
diff = 999999999999
while a < p and b < q and c < r:
    maximum = max(A[a], B[b], C[c])
    minimum = min(A[a], B[b], C[c])

    gap = maximum - minimum

    if gap < diff:
        a = a
        b = b
        c = c
        diff = gap

    if A[a] == minimum:
        a += 1
    elif B[b] == minimum:
        b += 1
    else:
        c += 1
print(diff)