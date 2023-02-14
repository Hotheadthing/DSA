A = 5
B = 2
C =[ 1000000000, 1000000000, 999999999, 999999999, 999999998, 1 ]

C_map = {}

for d in C:
    if d not in C_map:
        C_map.__setitem__(d,1)
    else:
        C_map[d] += 1
print(C)
x = 0
for d in C_map:
    if C_map[d] == B:
        x += d

if x == 0:
    print(-1)
else:
    print(x % 1000000007)


