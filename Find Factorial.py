def fac(A):
    if A < 2:
        return 1
    else:
        return A * fac(A-1)

x = fac(1)
print(x)
