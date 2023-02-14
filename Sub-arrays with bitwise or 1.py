A = 5
B = [0, 1, 0, 0, 0]
count = 0
sum = 0
total = (A*(A+1)) // 2
for i in range(A):
    if B[i] == 0:
        count += 1
    elif B[i] != 0 and count != 0:
        sum += (count * (count+1)) // 2
        count = 0

if count == 1:
    sum += 1
elif count > 1:
    sum += (count * (count + 1)) // 2


total = total - sum

print(total)




