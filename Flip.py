A = "010"
A = "111"
A = "0011101"
A = "01010110"
# A = "1101010001"
A = "0111000100010"

ones = 0
for i in range(len(A)):
    if A[i] == "1":
        ones += 1
total = ones
arr = []
s = 0
flag = False
for j in range(len(A)):
    if A[j] == "1":
        ones -= 1
    if A[j] == "0" and flag == False:
        arr.append(j+1)
        ones += 1
        flag = True
        if ones > total:
            arr.append(j+1)
            total = ones
    elif A[j] == "0" and flag == True:
        ones += 1
        if ones > total:
            arr.append(j+1)
            total = ones
print(arr)
if len(arr) > 2:
    y = []
    y.append(arr[0])
    y.append(arr[-1])
    print(y)
else:
    print(arr)

