nums = [2,2,3,1]
nums.sort()
nMap = {}
for i in range(len(nums)):
    if nums[i] not in nMap:
        nMap.__setitem__(nums[i],1)

arr = []
for d in nMap:
    arr.append(d)

if len(arr) < 3:
    print(arr[-1])
else:
    print(arr[-3])