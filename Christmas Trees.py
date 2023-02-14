A = [1, 3, 5]
B = [1, 2, 3]
sum = 99999

for i in range(len(A)-2):
    for j in range(i+1,len(A)-1):
        for h in range(j+1,len(A)):
            if A[h] > A[j] > A[i]:
                x = B[h] + B[j] + B[i]
                if x < sum:
                    sum = x

if sum == 99999:
    print(-1)
else:
    print(sum)


























