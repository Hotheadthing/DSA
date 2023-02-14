A = [1, 2, 3, 4, 0]
A = [2, 0, 1, 3]
mx = 0
count = 0

for i in range(len(A)):
    mx = max(mx,A[i])
    if mx == i:
        count +=1
print(count)