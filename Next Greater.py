A = [4, 5, 2, 10]
A = [3,2,1]
stack = []
arr = [0]*len(A)
arr[len(A)-1] = -1

for i in range(len(A)-1,-1,-1):
    if i == len(A)-1:
        stack.append(A[i])
    else:
        if A[i] < stack[-1]:
            arr[i] = stack[-1]
            stack.append(A[i])
        else:
            while A[i] >= stack[-1]:
                stack.pop()
                if len(stack) == 0:
                    break
            if len(stack) == 0:
                arr[i] = -1
            else:
                arr[i] = stack[-1]
            stack.append(A[i])

print(arr)
