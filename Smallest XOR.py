import copy
A = 3
B = 3
A_bin = bin(A)[2:]
# print(A_bin)
ans = ""
x = []
for i in range(len(A_bin)):
    x.append(0)
count = 0
for i in range(len(A_bin)):
    if A_bin[i] == "1":
        count += 1
# print(count)
if B >= len(A_bin):
    for i in range(B):
        ans += "1"
else:
    for i in range(len(A_bin)):
        if count <= B:
            if A_bin[i] == "1":
                x[i] = 1
                B -= 1
            else:
                x[i] = 0
        else:
            if A_bin[i] == "1" and B != 0:
                x[i] = 1
                B -= 1
            else:
                x[i] = 0
# print(x)


for i in range(len(x)-1,-1,-1):
    if x[i] != 1 and B != 0:
        x[i] = 1
        B -= 1
    elif B == 0:
        break
# print(x)

if ans == "":
    for i in range(len(x)):
        ans = ans + str(x[i])

print(int(ans,2))