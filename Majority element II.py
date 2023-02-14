nums = [2,2]
n = len(nums)/3
x = (n.__floor__())
nmap = {}
result = []
if x == 0:
    for d in nums:
        if d not in result:
            result.append(d)
else:
    for d in nums:
        if d not in nmap:
            nmap.__setitem__(d,1)
        else:
            nmap[d] += 1
    for i in nmap:
        if nmap[i] > x:
            result.append(i)
print(result)



