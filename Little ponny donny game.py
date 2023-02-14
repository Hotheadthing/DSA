A = 8
Flag = True
Ponny = []
Donny = []
for i in range(1,A,1):
    A = 8
    P = 0
    D = 0
    while A > 1:
        A = A - i
        P += 1
        Flag = False
        A = A - i
        D += 1
        Flag = True
    Ponny.append(P)
    Donny.append(D)
print(Ponny)
print(Donny)









