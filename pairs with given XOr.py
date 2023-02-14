# A = [5, 4, 10, 15, 7, 6]
# B = 5

A = [3, 6, 8, 10, 15, 50]
B = 5

A_map = {}
count = 0
for d in A:
    if d^B not in A_map:
        A_map.__setitem__(d,1)
    else:
        count += 1
print(count)
print(A_map)
