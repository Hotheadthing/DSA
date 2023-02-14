A = [2, 1, 4, 10]
A_map = {}
B = [3, 6, 2, 10, 10]
B_map = {}

for d in A:
    if d not in A_map:
        A_map.__setitem__(d,1)
    else:
        A_map[d] += 1

for d in B:
    if d not in B_map:
        B_map.__setitem__(d,1)
    else:
        B_map[d] +=1

length_A = len(A_map)
length_B = len(B_map)

C = []
if length_A <= length_B:
    for d in A_map:
        if d in B_map:
           C += [d] * min(A_map[d],B_map[d])
else:
    for d in B_map:
        if d in A_map:
            C += [d] * min(A_map[d], B_map[d])
print(C)
