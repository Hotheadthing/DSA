A = [100, 4, 200, 1, 3, 2]
A = [2, 1]
hmap = {}
for d in A:
    if d not in hmap:
        hmap.__setitem__(d,1)
    else:
        hmap[d] += 1
print(hmap)
count = 0
for d in hmap:
    if d-1 in hmap:
        continue
    else:
        x = 1
        while d+1 in hmap:
            x += 1
            d += 1
            count = max(x,count)
print(count)