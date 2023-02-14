A = [4, 7, 3, 8]
max_left = []
max_left.append(0)
maxright = 0
max_right = []
stack = []
for i in range(len(A)):
    if not stack:
        stack.append(A[i])
    else:
        if A[i] > stack[-1]:
            while A[i] > stack[-1]:
                stack.pop()
                if len(stack) == 0:
                    break



print(max_left)

for i in range(len(A)-1,-1,-1):
    if A[i] > maxright:
        max_right.append(maxright)
        maxright = A[i]
    else:
        max_right.append(maxright)

max_right.reverse()
print(max_right)