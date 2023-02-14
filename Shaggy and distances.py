#A = [7, 1, 3, 4, 1, 7]
A = [1, 2, 3]
length = 0
A_map = {}
count = 0
flag = False
for d in A:
    if d not in A_map:
        A_map.__setitem__(d,1)
        count += 1
    elif d in A_map and flag == False:
        x = A.index(d)
        length = (count) - x
        flag = True
        count +=1
    elif d in A_map and flag == True:
        x = A.index(d)
        length = min((count)-x,length)
        count +=1

if length == 0:
    print(-1)
else:
    print(length)