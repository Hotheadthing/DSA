A = [1]
n = len(A)
A.sort()
print(A)
sum = 0

for i in range(1,n):
    j = i
    while j != 0:
        sum += (A[i] - A[i-j]) *(2**(j-1))
        j -= 1
print(sum)














