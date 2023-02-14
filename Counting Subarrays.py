A = [1, 11, 2, 3, 15]
B = 10
count = 0
n = len(A)

for i in range(n):
    # print(i)
    if A[i] < B:
        count += 1
    z = A[i]
    for j in range(1+i,n,1):
        # print(f"the value of j is {j}")
        z += A[j]
        if z < B:
            count += 1
        else:
            break
print(count)
