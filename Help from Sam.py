A = 14
count = 0
x = bin(A)[2:]
B = []
for digit in x:
    B.append(int(digit))

for d in B:
    if d == 1:
        count +=1
print(count)