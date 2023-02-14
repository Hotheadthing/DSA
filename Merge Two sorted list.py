A = [1,2,3]
B = [0]
output = []
if len(A) == 0:
    for i in range(len(B)):
        output.append(B[i])
elif len(B) == 0:
    for i in range(len(A)):
        output.append(A[i])
elif len(B) == len(A) == 0:
    output = output
else:
    for i in range(min(len(B), len(A))):
        if A[i] <= B[i]:
            output.append(A[i])
            output.append(B[i])
        elif A[i] > B[i]:
            output.append(B[i])
            output.append(A[i])

print(output)

