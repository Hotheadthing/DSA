import math
A = [1, 17, 8]
A = [2, 2, 2]
A = [ 428, 56, 88, 12 ]
A = [ 323950831, 617081634, 113102555, 478465683, 352924446, 995310809, 111567227, 760837709, 746915507 ]
A = [ 41 ]
arr = []
ans = []
hmap = {}
for i in range(len(A)):
    if A[i] not in hmap:
        hmap.__setitem__(A[i] % 1000000003,1)
    else:
        hmap[A[i]] += 1


def perm():
    if len(ans) > 1:
        val = ans[-1] + ans[-2]
        sqrt = math.sqrt(val)
        if sqrt != int(sqrt):
            return
    if len(ans) == len(A):
        arr.append(ans.copy())
        return

    for d in hmap:
        if hmap[d] > 0:
            ans.append(d)
            hmap[d] -= 1
            perm()
            hmap[d] += 1
            ans.pop()
perm()
print(arr)
print(len(arr))
# def checker(arr):
#     flag = False
#     flag1 = False
#     for i in range(1,len(arr)-1):
#         v = arr[i]
#         v1 = arr[i+1]
#         v2 = arr[i-1]
#         sum = v + v1
#         square_root = math.sqrt(sum)
#         if square_root == int(square_root):
#             flag = True
#         sum2 = v + v2
#         sqrt = math.sqrt(sum2)
#         if sqrt == int(sqrt):
#             flag1 = True
#
#         if flag and flag1 == True:
#             return True
#         else:
#             return False
#
#
# result = []
# for i in range(len(arr)):
#     bol = checker(arr[i])
#     if bol:
#         result.append(arr[i])
#
# if len(result) % 2 == 0:
#     print(len(result)//2)
# else:
#     print(len(result))




