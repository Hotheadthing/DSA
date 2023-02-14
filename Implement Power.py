import math
A = -2
B = 3
C = 3
def power(A,B,C):
    if B == 0:
        return 1
    x = power(A, B//2, C)
    if B % 2 == 0:
        return (x * x) % C
    else:
        return ((x*x) % C * A) % C


z = power(-2,3,3)
print(z)

# print((-2**3) % 3)