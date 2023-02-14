nums = [1,1,1,2,2,3]
# nums = [0,0,1,1,1,1,2,3,3]
nmap = {}
result = 0
for d in nums:
    if d not in nmap:
        nmap.__setitem__(d,1)
    else:
        nmap[d] += 1

for d in nmap:
    if nmap[d] > 2:
        x = nmap[d] - 2
        for i in range(x):
            nums.remove(d)
print(nums)