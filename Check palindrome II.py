A ="yzfbzbyyrurquqf"
#A = "abbaee"
length = len(A)
print(length)
A_map = {}

for d in A:
    if d not in A_map:
        A_map.__setitem__(d,1)
    else:
        A_map[d] +=1
print(A_map)
flag = False
count = 0
if length % 2 == 0:
    for d in A_map:
        if A_map[d] % 2 != 0:
            flag = False
            break
        else:
            flag = True
flag1 = False
if length % 2 != 0:
    for d in A_map:
        if A_map[d] % 2 == 0:
            flag1 = True
        elif A_map[d] % 2 != 0 and count == 0:
            flag1 = True
            count += 1
        elif A_map[d] % 2 != 0 and count == 1:
            flag1 = False
            break

if length % 2 == 0 and flag == False:
    print(0)
elif length % 2 == 0 and flag == True:
    print(1)

if length % 2 != 0 and flag1 == False:
    print(0)
elif length % 2 != 0 and flag1 == True:
    print(1)