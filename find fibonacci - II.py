def fib(A):
    if A == 1:
        return 0
    if A == 2:
        return 1
    else:
        return fib(A-1) + fib(A-2)


x = fib(7)
print(x)
