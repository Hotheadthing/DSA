from collections import deque
A = "()())()"
A = "(a)())()"
A = "))"
A = "))m))w"
A = "))))(("
A = "()))()"
A = ")((p"
stack = deque()
arr = []
closing_brackets = [")"]
for i in range(len(A)):
    if len(stack) == 0:
        if A[i] == ")":
            arr.append(i)
        elif A[i] == "(":
            stack.append(A[i])
    else:
        if A[i] in closing_brackets:
            if stack[-1] == "(":
                stack.pop()
            else:
                arr.append(i)
        elif A[i] == "(":
            stack.append(A[i])
print(arr)
print(stack)
string = ""
brackets = 0
for i in range(len(A)):
    if i not in arr:
        string += A[i]
        if A[i] == "(" or A[i] == ")":
            brackets += 1
print(string)
hmap = {}
hmap.__setitem__(string,1)

A_arr = []
for i in range(len(string)):
    A_arr.append(string[i])

# print(A_arr)
n = len(A)
if len(A) == len(arr):
    print()
count = 0
for i in range(len(arr)):
    A_arr.insert(arr[i]-count,A[arr[i]])
    times = arr[i] - count
    count += 1
    # print(f"A_arr = {A_arr}")
    for j in range(times):
        # print(A_arr[j])
        if A_arr[j] == A[arr[i]]:
            # print(A_arr[j], A[arr[i]])
            del A_arr[j]
            str = ""
            # print(A_arr)
            for k in range(len(A_arr)):
                str += A_arr[k]
            # print(str)
            if str not in hmap:
                hmap.__setitem__(str,1)
            # print(A_arr,j,A[arr[i]])
            A_arr.insert(j,A[arr[i]])
            # print(A_arr)
    del A_arr[arr[i]]

# print(hmap)

ans = []

for x in hmap:
    ans.append(x)

print(ans)


