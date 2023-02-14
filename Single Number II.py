nums = [2,2,3,2]
nmap = {}

for i in range(len(nums)):
    if nums[i] not in nmap:
        nmap.__setitem__(nums[i],1)
    else:
        nmap[nums[i]] += 1

for d in nmap:
    if nmap[d] < 3:
        print(d)
        break