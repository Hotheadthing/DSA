A = [5]
A.sort(reverse=True)
print(A)
sum = 0
# for i in range(len(A)):


for i in range(len(A)):
    if i == 0:
        continue
    else:
        A[i] = A[i] + A[i-1]
print(A)
sum = A[-1]
result = A[-1]
for i in range(len(A)):
    result += sum - A[i]

print(result)