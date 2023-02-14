A = [1, 2, 3, 1, 2, 4]
A = [ 186, 256, 102, 377, 186, 377 ]

val = A[0]

for i in range(1,len(A)):
    val = val ^ A[i]

val_bin = bin(val)[2:]
ind = 0
for i in range(len(val_bin)-1,-1,-1):
    if val_bin[i] == "1":
        ind = len(val_bin)-1 - i
        break

element0 = 0
element1 = 0
arr = []
for d in A:
    if d & (1<<ind) != 0:
        element0 = element0 ^ d
    else:
        element1 = element1 ^ d

arr.append(element0)
arr.append(element1)
arr.sort()
print(arr)