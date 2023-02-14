A = 11
B = (bin(A)[2:])
count = 0
for digit in B:
    if digit == "1":
        count += 1
print(count)