A = [2, 1, 3]
n = len(A)
Sum = 0
for i in range(n):
    Sum += A[i] * (n-i) * (i+1)
print(Sum)
