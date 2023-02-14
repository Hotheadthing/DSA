# A = [1, 2, 3, 4, 5]
# B = 6
A = [5, 10, 20, 100, 105]
B = 110

n = len(A)


sum = 0
result = []

b = []

for i in range(len(A)):
    b.append(A[i])

for i in range(len(b)):
    if i == 0:
        b[i] = b[i]
    else:
        b[i] = b[i] + b[i-1]

A_map = {}
for i in range(len(b)):
    if b[i] == B:
        result.append(i)
        break
    if b[i] - B not in A_map:
        A_map.__setitem__(b[i],i)
    elif b[i] - B in A_map:
        result.append(A_map[b[i] - B])
        result.append(i)
        break

if result == []:
    print(-1)
elif len(result) == 1:
    print(A[0:result[0]+1])
else:
    print(A[result[0]+1:result[1]+1])
