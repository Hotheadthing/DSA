import math

def isPowerOfFour(n: int) -> bool:
    x = math.log(n,3)
    print(x)

    if x == x.__ceil__():
        return True
    else:
        return False

x = isPowerOfFour(129140163)
print(x)

