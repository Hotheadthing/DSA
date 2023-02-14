A = [ 96, -71, 18, 66, -39, -32, -16, -83, -11, -92, 55, 66, 93, 5, 50, -45, 66, -28, 69, -4, -34, -87, -32, 7, -53, 33, -12, -94, -80, -71, 48, -93, 62 ]
sum = 0
E = []
print(A)
for d in range(len(A)):
    sum += A[d]
    E.append(sum)
print(E)

A_map = {}
for d in E:
    if d not in A_map:
        A_map.__setitem__(d,1)
    else:
        A_map[d] += 1
print(A_map)

sum1 = 0
flag = False
for i in range(len(A)):
    sum1 += A[i]
    if A[i] == 0 or sum == 0:
        flag = True
        break

for d in A_map:
    if A_map[d] > 1:
        flag = True
print(flag)






