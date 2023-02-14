A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
B = [00000000000000000000000000000000]
ans = 0

for i in range(32):
    count = 0
    for j in range(len(A)):
        x = bin(A[j])[2:]
        y = x[i]
        if y == "1":
            count += 1
        print(count)
    if count % 3 != 0:
        ans = ans | (1 << i)
# print(ans)