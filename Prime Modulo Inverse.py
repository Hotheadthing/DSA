import math
A = 6
B = 23
x = math.gcd(A,B)

def solve(A, B):
    power(A,B-2,B)

def power(x, y, M):
    if (y == 0):
        return 1

    p = power(x, y // 2, M) % M
    p = (p * p) % M

    if (y % 2 == 0):
        return p
    else:
        return ((x * p) % M)

y = solve(6,23)
print(y)