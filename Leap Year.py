A = 1999
if A % 400 == 0:
    print(1)
elif A % 4 == 0 and A % 100 != 0:
    print(1)
else:
    print(0)