A = [1, 2]
Lead = []
Lead.append(A[-1])
x = A[-1]
length = len(A)
for i in range(length-2,-1,-1):
    if A[i] > x:
        x = A[i]
        Lead.append(A[i])
print(Lead)



