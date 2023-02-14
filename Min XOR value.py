A = [0, 2, 5, 7]
# A = [0, 4, 7, 9]
A = [12, 4, 6, 2]

result = 9999999999

for i in range(len(A)-1):
    val = A[i]^A[i+1]
    result = min(result,val)
print(result)
