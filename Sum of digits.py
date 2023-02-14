def sum(A):
    if A == 0:
        return 0
    # A = A % 10 + sum(A // 10)
    while A >= 10:
        A = A % 10 + sum(A//10)
    return A

    # if A == 1:
    #     return 1
    # else:
    #     return 0


x = sum(83557)
print(x)
