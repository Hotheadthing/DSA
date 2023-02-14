x = 2634
A = str(x)
print(A)
A_map = {}

for d in A:
    if d not in A_map:
        A_map.__setitem__(d,1)
    else:
        A_map[d] += 1
# print(A_map)

x = 1
count = 0
flag = False
mMap = A_map.copy()
print(mMap)
for d in A_map:
    x = x*int(d)
    count += 1
    if A_map[d] > 1:
        flag = False
        break
    elif count >= 2 and str(x) in A_map.keys():
        flag = False
        break
    else:
        flag = True

if flag == False:
    print(0)
else:
    print(1)


