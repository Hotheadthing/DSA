nums = [1,2,3]
nums = [0]
result = [[]]
for i in range(len(nums)):
    result.append([nums[i]])
    for j in range(i + 1, len(nums)):
        result.append([nums[i],nums[j]])

if nums not in result:
    result.append(nums)

print(result)
