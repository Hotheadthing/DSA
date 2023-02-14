n = 10
lower = 1
upper = n
count = 0
if upper < 3:
    print(0)
else:
    for num in range(lower, upper):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                count += 1
print(count)