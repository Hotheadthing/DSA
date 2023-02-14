import math
A = 6
B = 2
C = 13

n = math.factorial(A)
r = math.factorial(B)
n_r = math.factorial(A-B)
ans = n // (r * n_r)

print(ans % C)


