A = [2, 4, 1]
A.sort()
x = A[1] - A[0]
flag = True
for i in range(len(A)-1):
    if x != A[i+1] - A[i]:
        flag = False
if flag == False:
    print(0)
else:
    print(1)


