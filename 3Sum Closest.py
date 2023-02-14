nums = [-1,2,1,-4]
target = 1
nums.sort()
times = (len(nums) - 3) + 1
sum = 0
result = []
print(nums)
ans = 0
for i in range(times):
    sum += nums[i]
    for j in range(i+1,(i+1)+2):
        sum += nums[j]
    result.append(sum)
    sum = 0
print(result)

for d in result:
    x = abs(target - d)
print(ans)