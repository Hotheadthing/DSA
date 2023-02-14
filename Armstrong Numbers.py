y = 1000000
z= []
j = []
for i in range(y):
    i = (i+1)
    x = 0
    w = []
    for digits in str(i):
        w.append(digits)
    for digits in w:
        x += int(digits) * int(digits) * int(digits)
        if x == (i):
            z.append(x)
for i in z:
    if i not in j:
        j.append(i)
for digits in j:
    print(digits)









