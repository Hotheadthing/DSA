A = [1, 2]
D =[]
B = 1
Length = len(A)
Sum = []
for i in range(Length):
    if i == 0:
        continue
    else:
        A[i] = A[i] + A[i-1]
# new_A = [5, 3, 6, 7, 9]
if B == Length:
    print(A[-1])
# For first three:
Sum.append(A[B-1])
# For last three:
Sum.append(A[-1] - A[(Length-B) - 1])
# For every other case:
for i in range(B-1,0,-1):
    Sum1 = A[i-1] + (A[-1] - A[-(B-i+1)])
    Sum.append(Sum1)
Sum.sort()
print(Sum[-1])
