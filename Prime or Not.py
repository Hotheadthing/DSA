A = 15
flag = True
output = 1
for i in range(A):
    if i+2 != A:
        Z = A % (i+2)
        if Z == 0:
            output = 0
            break
        else:
            flag = False
            continue
if not flag and output == 1:
    print("Yes")
else:
    print("No")