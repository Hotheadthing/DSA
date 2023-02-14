nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums.sort()
print(nums)
result = []
count = 0
for i in range(len(nums)-1):
    if nums[i] + 1 == nums[i+1]:
        count += 1
    else:
        count += 1
        result.append(count)
        count = 0
result.append(count+1)
print(max(result))

