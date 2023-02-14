nums = [5,7,7,8,8,10]
target = 8
ans = []
for i in range(len(nums)):
    if nums[i] == target:
        ans.append(i)

if ans == []:
    print([-1,-1])
elif len(ans) > 2:
    ans2 = []
    ans2.append(ans[0])
    ans2.append(ans[-1])
    print(ans2)
elif len(ans) == 1:
    ans.append(ans[0])
    print(ans)
else:
    print(ans)