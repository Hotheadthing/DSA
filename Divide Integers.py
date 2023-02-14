import math
A = 7
B = -3
sign = -1 if ((A < 0) ^
              (B < 0)) else 1

# print(sign)

dividend = abs(A)
divisor = abs(B)
#
#
if (dividend == 0):
    print(0)

if (divisor == 1):
    print((sign * dividend))

print(math.floor(sign * math.exp(math.log(dividend) -
                                 math.log(divisor))))

