A = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
B = 3
# A = [
#       [5, 17, 100, 111],
#       [119, 120, 127, 131]
#     ]
# B = 3
A = [
  [3],
  [29],
  [36],
  [63],
  [67],
  [72],
  [74],
  [78],
  [85]
]
B = 41
A =[
  [3, 4, 9, 10, 14, 17, 18, 20, 29, 32],
  [33, 36, 38, 46, 51, 52, 56, 56, 56, 58],
  [66, 72, 72, 76, 76, 76, 82, 85, 90, 96]
]
B = 56

n = len(A)
# print(n)
m = len(A[0])
arr = []

for i in range(n):
    arr.append(A[i][m-1])

print(arr)
top = 0
bottom = len(arr)-1
x = 0
ans = -1
if top != bottom:
    while top <= bottom:
        mid = (top + bottom) // 2
        # print(A[mid][m-1])
        if A[mid][m-1] == B:
            ans = mid
        elif A[mid][m-1] > B:
            bottom = mid - 1
        else:
            top = mid + 1
        y = mid
        if A[mid][m-1] > B:
            x = mid

f_ans = 0
print(x)
if ans == -1:
    ans = x
    left = 0
    right = m-1
    while left <= right:
        mid = (left+right) // 2
        if A[ans][mid] == B:
            f_ans = 1
            break
        elif A[ans][mid] > B:
            right = mid - 1
        else:
            left = mid + 1
else:
    f_ans = 1

print(f_ans)

