import math
A = 411753753
B = 1876
C = 7430

min_val = B*C
x = math.gcd(B,C)
min_val = min_val // x
count = A // min_val
print(count)