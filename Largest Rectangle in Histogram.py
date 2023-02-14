A = [2, 1, 5, 6, 2, 3]
# A = [2]

stack = []
max_area = 0
index = 0

while index < len(A):
    if (not stack) or A[index] >= A[stack[-1]]:
        stack.append(index)
        # print(f"the value of stack is index = {index}, stack = {stack}")
        index += 1

    else:
        top_elem = stack.pop()
        # print(f"the value of top element = {top_elem}")
        # print(f"value of stack is {stack}")
        # print(f"the value of index is {index}")
        if stack:
            area = A[top_elem] * (index - stack[-1] - 1)
            max_area = max(area,max_area)
        else:
            area = A[top_elem]*index
            max_area = max(area,max_area)

while stack:
    top_elem = stack.pop()

    if stack:
        area = A[top_elem] * (index - stack[-1] - 1)
        max_area = max(area, max_area)
    else:
        area = A[top_elem]*index
        max_area = max(area, max_area)

print(max_area)





