A = 3
B = 2
C = 3
D = 9
E = 6
F = 2
G = 6
A = int(input())
for i in range(A):
    x = int(input())
    y = int(input())
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    print(lcm)
