# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4
A = [5,1,3]
B = 5
A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 202
A = [7,6,5,4,0,1,2,3]
B= 3
n = len(A)
left = 0
right = n-1
ans = -1
if n == 1:
    ans = 0
else:
    while left <= right:
        mid = (left+right) // 2
        if A[mid] == B:
            print(mid)
            break
        elif A[mid] > A[left]:
            if A[left] <= B < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if A[mid] < B <= A[right]:
                if B == A[right]:
                    print(right)
                else:
                    left = mid + 1
            else:
                right = mid - 1

