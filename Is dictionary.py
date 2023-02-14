# A = ["hello", "scaler", "interviewbit"]
# B = "adhbcfegskjlponmirqtxwuvzy"

A = ["none", "no", "fine"]
B = "qwertyuiopasdfghjklzxcvbnm"

B_map = {}

for i in range(len(B)):
    if B[i] not in B_map:
        B_map.__setitem__(B[i],i)

print(B_map)

length = len(A)
flag = -1
x = (length + 1) // 2
if length % 2 != 0:
    for i in range(len(A)-2):
        if B_map[A[(x-2)-i][0]] < B_map[A[x-1][0]] < B_map[A[x+i][0]]:
            flag = 1
        elif B_map[A[(x-2)-i][0]] > B_map[A[x-1][0]] > B_map[A[x+i][0]]:
            flag = 2
            break
        elif B_map[A[(x-2)-i][0]] < B_map[A[x-1][0]] > B_map[A[x+i][0]]:
            flag = 2
            break
        elif B_map[A[x-2][i]] > B_map[A[x-1][i]] < B_map[A[x][i]]:
            flag = 2
            break
if flag == 1:
    print(1)
elif flag == 2:
    print(0)


flag1 = -1
if length % 2 == 0:
    for i in range(len(A) - 1):
        if B_map[A[i][0]] < B_map[A[i + 1][0]]:
            flag1 = 1
        elif B_map[A[i][0]] > B_map[A[i + 1][0]]:
            flag1 = 2
            break
if flag1 == 1:
    print(1)
elif flag1 == 2:
    print(0)






