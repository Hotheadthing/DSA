A = [1, 5, 4, 3]
A = [1]
i = 0
n = len(A)
j = n-1
ans = 0

while j > i:
    ans = max(ans,(j-i)*min(A[i],A[j]))
    if A[i] > A[j]:
        j -= 1
    else:
        i += 1
print(ans)