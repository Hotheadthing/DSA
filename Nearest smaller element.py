A = [4, 5, 2, 10, 8]
A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
stack = []
arr = [0] * len(A)
arr[0] = -1

for i in range(len(A)):
    if i == 0:
        stack.append(A[i])
    else:
        if A[i] > stack[-1]:
            arr[i] = stack[-1]
            stack.append(A[i])
        else:
            while A[i] < stack[-1]:
                stack.pop()
                if len(stack) == 0:
                    break
            if len(stack) == 0:
                arr[i] = -1
            else:
                arr[i] = stack[-1]
            stack.append(A[i])

print(arr)