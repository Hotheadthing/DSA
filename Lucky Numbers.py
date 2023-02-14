A = 21
arr = []

for i in range(A+1):
    arr.append(i)

# print(arr)

for i in range(2,len(arr)):
    if arr[i] == i:
        # print(i)
        for j in range(2*i,len(arr),i):
            if arr[j] == j:
                arr[j] = 0
            else:
                arr[j] += 1
            # print(f"the value of j is {j}")

ans = 0
for i in range(2,len(arr)):
    if arr[i] == 1:
        ans += 1
print(ans)