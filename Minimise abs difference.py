A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]
max_abc = max(A[0],B[0],C[0])
result = 0
if C[0] == max_abc:
    print("in if loop")
    # 1st iteration
    l = 0
    val = C[0]
    r = 0
    diff = abs(C[0]-B[0])
    arr = []
    while l < len(C) and r < len(B):
        cur_diff = abs(C[l]-B[r])
        if cur_diff <= diff:
            x = [C[l],B[r]]
            arr = x
            diff = cur_diff
            r += 1
        else:
            l += 1
    print(arr)

    # 2nd iteration
    l = 0
    val = C[0]
    r = 0
    diff = abs(C[0] - A[0])
    arr1 = []
    while l < len(C) and r < len(A):
        cur_diff = abs(C[l] - A[r])
        if cur_diff <= diff:
            x = [C[l], A[r]]
            arr1 = x
            diff = cur_diff
            r += 1
        else:
            l += 1
    print(arr1)
    result = max(abs(arr[0]-arr[1]),abs(arr1[0]-arr1[1]),abs(arr[1]-arr1[1]))

elif B[0] == max_abc:
    # 1st iteration
    print("in elif loop")
    l = 0
    val = B[0]
    r = 0
    diff = abs(B[0]-C[0])
    arr = []
    while l < len(B) and r < len(C):
        cur_diff = abs(B[l]-C[r])
        if cur_diff <= diff:
            x = [B[l],C[r]]
            arr = x
            diff = cur_diff
            r += 1
        else:
            l += 1
    print(arr)

    # 2nd iteration
    l = 0
    val = B[0]
    r = 0
    diff = abs(B[0] - A[0])
    arr1 = []
    while l < len(B) and r < len(A):
        cur_diff = abs(B[l] - A[r])
        if cur_diff <= diff:
            x = [B[l], A[r]]
            arr1 = x
            diff = cur_diff
            r += 1
        else:
            l += 1
    print(arr1)
    result = max(abs(arr[0]-arr[1]),abs(arr1[0]-arr1[1]),abs(arr[1]-arr1[1]))

else:
    # 1st iteration
    print("in else loop")
    l = 0
    val = A[0]
    r = 0
    diff = abs(A[0]-B[0])
    arr = []
    while l < len(A) and r < len(B):
        cur_diff = abs(A[l]-B[r])
        if cur_diff <= diff:
            x = [A[l],B[r]]
            arr = x
            diff = cur_diff
            r += 1
        else:
            l += 1
    print(arr)

    # 2nd iteration
    l = 0
    val = A[0]
    r = 0
    diff = abs(A[0] - C[0])
    arr1 = []
    while l < len(A) and r < len(C):
        cur_diff = abs(A[l] - C[r])
        if cur_diff <= diff:
            x = [A[l], C[r]]
            arr1 = x
            diff = cur_diff
            r += 1
        else:
            l += 1
    print(arr1)
    result = max(abs(arr[0]-arr[1]),abs(arr1[0]-arr1[1]),abs(arr[1]-arr1[1]))
print(result)






