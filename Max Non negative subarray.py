# A = [1, 2, 5, -7, 2, 3]
# A = [10, -1, 2, 3, -4, 100]
# A = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
A = [ -1, -1, -1, -1, -1 ]
# A = [ 1, 2, 5, -7, 2, 5 ]
# A = [0, 0, -1, 0]
# A = [ -1469348094, 1036140795, 2040651434, -317097467, 1376710097, 1330573317, 1687926652 ]

current_max = 0
global_max = 0
arr = []
l = 0
r = 0

for i in range(len(A)):
    if A[i] >= 0:
        current_max = max(current_max,current_max+A[i])
        if current_max >= global_max:
            global_max = current_max
            r = i
            arr = []
            arr.append(l)
            arr.append(r)
    else:
        l = i+1
        current_max = 0


print(A[arr[0]:arr[1]+1])

