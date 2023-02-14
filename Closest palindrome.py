A = "abbba"
# A = "adaddb"
A = "aba"
count = 0
i = 0
n = len(A)
j = n-1

while i <= j:
    if A[i] != A[j]:
        if count == 0:
            count += 1
        else:
            count += 1
            break
    i += 1
    j -= 1
    if i == j:
        if count == 0:
            count += 1
if count == 1:
    print("Yes")
else:
    print("No")