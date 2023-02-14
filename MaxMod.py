A = [2, 6, 4]
B = []
length = len(A)
for digit in A:
    B.append(digit)
B.sort()
A_j = B[-1]
A_i = 0
for digit in range(length-1,-1,-1):
    print(digit)
    if A[digit-1] != A[digit]:
        A_i = A[digit-1]
result = (A_i % A_j)
print(result)
