import math
A = 5
arr = []
for i in range(A + 1):
    if i == 0:
        arr.append(False)
    elif i == 1:
        arr.append(False)
    else:
        arr.append(True)

val = math.floor(math.sqrt(A) + 1)
for i in range(2, val):
    if arr[i] == True:
        for j in range(i * i, A + 1, i):
            arr[j] = False
print(arr)
itr = 2
while True:
    if arr[itr] and arr[A - itr]:
        print([itr, A - itr])
        break
    itr += 1