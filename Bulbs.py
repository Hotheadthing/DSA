A = [0, 0, 0, 1]
count = 0
change = 0
for i in range(len(A)):
    if A[i] == 0 and change % 2 ==0:
        count += 1
        change += 1
    elif A[i] == 1 and change % 2 != 0:
        count += 1
        change += 1
print(count)


