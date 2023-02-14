import math
import sys
sys.setrecursionlimit(10**6)
A = 2
B = 27
B_facto = math.factorial(B)

M = 1000000007

def power(x, y, m):
    if y == 0:
        return 1
    w = power(x, y//2, m)
    if y % 2 == 0:
        return ((w*w) % m) % m
    else:
        return((w*w) % m * (x % m)) % m

def solve(A, B):
    M = 1000000007
    mod = 1000000007
    M = mod
    initial = 2
    ans = 1
    while initial <= B:
        ans = (ans * initial) % (mod - 1)
        initial += 1
    return power(A, ans, M)


x = solve(A, B)
print(x)

