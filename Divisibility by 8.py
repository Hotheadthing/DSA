A = "123"
length = len(A)
if length < 3:
    for i in range(0,3-length):
        zero = "0"
        A = zero + A

x = int(A[-3:])

if x % 8 == 0:
    print(1)
else:
    print(0)

