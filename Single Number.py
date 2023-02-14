A = [1, 2, 2]
binary = []
for digit in A:
    binary.append(bin(digit)[2:])
print(binary)
sum = 0
for digit in binary:
    sum = sum^int(digit)
ind= binary.index(str(sum))
print(A[ind])
