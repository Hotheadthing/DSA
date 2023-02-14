A = [4, 0, 2, 1, 3]
n = len(A)
ans = []
for i in range(n):
    new_val = A[A[i]] % n
    A[i] = n*new_val + A[i]

for i in range(n):
    ans.append(A[i]//n)

print(ans)
