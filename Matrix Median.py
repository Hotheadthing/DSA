A = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
# A = [[5, 17, 100]]
# A = [
#   [1, 1, 3, 3, 3, 3, 3]
#     ]
rows = len(A)
coloumns = len(A[0])
n = rows * coloumns
median = (n+1)// 2
l = 9999999999999
r = -999999999999

for i in range(rows):
    l = min(l,A[i][0])
    r = max(r,A[i][-1])


def count(arr,mid,median):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] <= mid:
                count += 1
            else:
                break
    if count >= median:
        return True
    else:
        return False

ans = 0
while l <= r:
    mid = (l+r) // 2
    if count(A,mid,median):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)

# rows = len(A)
# coloumn = len(A[0])
# # print(rows,coloumn)
# n = rows * coloumn
# # print(n)
# median = 0
# if n % 2 != 0:
#     median = (n + 1) // 2
# else:
#     median = n // 2
#
#
# def rank(arr, mid, median):
#     if mid == 0:
#         return False
#     count = 0
#     for i in range(rows):
#         for j in range(coloumn):
#             if arr[i][j] <= mid:
#                 count += 1
#     if count >= median:
#         return True
#     else:
#         return False
#
#
# l = 99999999999
# r = -9999999999
# for i in range(rows):
#     l = min(l,A[i][0])
#     r = max(r,A[i][-1])
# # print(l,r)
# ans = 0
# while l <= r:
#     mid = (l+r)//2
#     print(mid)
#     if rank(A,mid,median):
#         ans = mid
#         print(f"the value of ans is {ans}")
#         r = mid - 1
#     else:
#         l = mid + 1
#
# print(ans)
#
