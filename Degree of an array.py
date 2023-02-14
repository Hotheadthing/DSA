nums = [1,2,2,3,1]
# nums = [1,2,2,3,1,4,2]
nMap = {}

for i in range(len(nums)):
    if nums[i] not in nMap:
        nMap.__setitem__(nums[i],1)
    else:
        nMap[nums[i]] += 1

maxim = 0
arr = []
for d in nMap:
    if nMap[d] > maxim:
        arr = [d]
        maxim = nMap[d]
    elif nMap[d] == maxim:
        arr.append(d)

length = 999999

for i in range(len(arr)):
    l = 0
    r = 0
    x = 0
    for j in range(len(nums)-1,-1,-1):
        if (nums[j] == arr[i]) and (r == 0):
            r = j
        elif (nums[j] == arr[i]) and (r != 0):
            l = j
            x += (r - l)
            l = 0
            r = j
        if j == 0:
            x += 1
            length = min(length,x)
print(length)



