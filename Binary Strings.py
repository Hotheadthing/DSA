A = "00010110"
B = 3
# A = "011"
# B = 3
arr = []
for i in range(len(A)):
    arr.append(A[i])
min_operations = 0
n = len(A)
times = n - B + 1

for i in range(times):
    flag = False
    if arr[i] == "0":
        arr[i] = "1"
        min_operations += 1
        flag = True
    for j in range(i+1,i+B):
        if flag == True:
            if arr[j] == "0":
                arr[j] = "1"
            else:
                arr[j] = "0"


flag = True
for i in range(len(arr)):
    if arr[i] == "0":
        flag = False
        break

if flag == True:
    print(min_operations)
else:
    print(-1)



