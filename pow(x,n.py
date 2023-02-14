x = 2.00000
n = 10

def pow(x,n):
    if n == 0:
        return 1
    return (x * pow(x,n-1))
y = pow(3,3)
print(y)
