a = [1,2,2]
b = 4
count = 0
for i in range(len(a)):
    if b - a[i] in a[(i+1):]:
        count = 1
        break
    else:
        count = 0
print(count)
