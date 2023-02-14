import math
A = 1
B = 2
C = 3
# A = 19
# B = 11
# C = 13

l = min(B, C)
r = min(B, C) * A

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    elif a > b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)
x = gcd(B,C)
z= (B*C)//x
ans  = 0
while l <= r:
    mid = (l+r)//2
    x = (mid // B) + (mid // C) - (mid // math.lcm(B,C))

    if x > A:
        r = mid - 1
    elif x == A:
        ans = mid
        r = mid -1
    else:
        l = mid + 1
print(ans)
#
#
