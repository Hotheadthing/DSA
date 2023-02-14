nums = [4,3,2,7,8,2,3,1]
nMap = {}

for i in range(len(nums)):
    if nums[i] not in nMap:
        nMap.__setitem__(nums[i],1)
    else:
        nMap[nums[i]] += 1
result = []
for d in nMap:
    if nMap[d] == 2:
        result.append(d)
print(result)