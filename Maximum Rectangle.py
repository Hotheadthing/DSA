A = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
    ]
# A = [[0, 1, 0, 1],
#      [1, 0, 1, 0]]
# A = [
#   [0, 1, 1],
#   [1, 0, 0],
#   [1, 0, 0],
#   [1, 0, 0],
#   [1, 0, 0],
#   [1, 1, 1],
#   [0, 1, 0]
# ]

def max_area(arr):
    area = 0
    maxarea = 0
    index = 0
    stack = []
    while index < len(arr):
        if len(stack) == 0 or arr[index] >= arr[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_element = arr[stack.pop()]
            area = top_element * index
            if len(stack) != 0:
                area = top_element * (index - stack[-1] - 1)
            maxarea = max(maxarea,area)

    while len(stack) != 0:
        top_element = arr[stack.pop()]
        area = top_element * index
        if len(stack) != 0:
            area = top_element * (index - stack[-1] - 1)
        maxarea = max(area,maxarea)

    return maxarea


result = max_area(A[0])

for i in range(1,len(A)):
    for j in range(len(A[i])):
        if A[i][j]:
            A[i][j] += A[i-1][j]
    result = max(result,max_area(A[i]))

print(result)

