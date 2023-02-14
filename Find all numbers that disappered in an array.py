nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
# nums = [2,2]
quer = []

nMap = {}
ref = 1
for i in range(len(nums)):
    nMap.__setitem__(ref,0)
    ref += 1

print(nMap)

for j in range(len(nums)):
    nMap[nums[j]] += 1

for d in nMap:
    if nMap[d] == 0:
        quer.append(d)
print(quer)