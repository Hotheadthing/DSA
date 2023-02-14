A = [2, 3, 6, 7]
# A.sort()
B = 7
A = [10, 1, 2, 7, 6, 1, 5]
# A = [1, 1, 2, 5, 6, 7, 10]
B = 8
# A = [2, 1, 3]
# B = 3
A.sort()
arr = []
ans = []
hmap = {}
for x in A:
    if x not in hmap:
        hmap.__setitem__(x,1)
    else:
        hmap[x] += 1


def sum(i,cur_sum):
    if cur_sum == B:
        # print(f"val of ans is {ans}")
        if ans.copy() not in arr:
            arr.append(ans.copy())
        return
    if cur_sum > B:
        return
    if i >= len(A):
        return

    cur_sum += A[i]
    ans.append(A[i])
    sum(i+1,cur_sum)
    cur_sum -= A[i]
    ans.pop()
    sum(i+1,cur_sum)






sum(0,0)
print(arr)