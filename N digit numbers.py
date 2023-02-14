import sys
sys.setrecursionlimit(10**6)
A = 75
B = 22
A = 1
B = 3
mod = 1000000007
def solve(digit,cur_sum):
    if digit == 0:
        return cur_sum == 0

    if cur_sum == 0:
        return 1

    ans = 0
    for i in range(0,10):
        if cur_sum - i >= 0:
            # print(digit-1,cur_sum-i)
            ans += solve(digit-1,cur_sum-i)
            # print(ans)

    return ans


ans = 0
for i in range(1,10):
    if B-i >= 0:
        ans += solve(A-1,B-i)


print(ans)

