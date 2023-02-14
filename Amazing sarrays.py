A = "ABEC"
vowels = "AaEeIiOoUu"
count = 0
for i in range(len(A)):
    if A[i] in vowels:
        count += len(A) - i
print(count % 10003)
