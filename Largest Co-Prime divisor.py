import math
A = 30
B = 12

def find_gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return find_gcd(a%b, b)
    if b > a:
        return find_gcd(b%a, a)


def cpFact(A, B):
    while find_gcd(A, B) != 1:
        A = A // find_gcd(A, B)
    return A

x = cpFact(A,B)
print(x)