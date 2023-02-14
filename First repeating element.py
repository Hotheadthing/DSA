#A = [10, 5, 3, 4, 3, 5, 6]
A = [6, 10, 5, 4, 9, 120]
M = {}
for d in A:
    if d not in M:
        M.__setitem__(d,1)
    else:
        M[d] +=1
print(M)
flag = False
for d in M:
    if M[d] > 1:
        flag = True
        break
if flag == True:
    for d in A:
        if M[d] >1:
            print(d)
            break
else:
    print(-1)