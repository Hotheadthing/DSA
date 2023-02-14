A = "abobc"
count = 0
for i in range(len(A)-2):
    if A[i] == 'b' and A[i+1] == 'o' and A[i+2] == 'b':
        count += 1
print(count)