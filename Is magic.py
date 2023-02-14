A = 83557
n = len(str(A))
A = str(A)

while n > 1:
    ans = 0
    for i in range(n):
        ans += int(A[i])
    A = str(ans)
    n = len(str(A))
print(ans)
