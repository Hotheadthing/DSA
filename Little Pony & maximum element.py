a = [1,4,2]
b = 3
a.sort()
# print(a)
c = len(a)
# print(c)
count = 0
if b in a:
    for i in range(c-1,-1,-1):
        if a[i] > b:
            a.pop(i)
            count += 1
else:
    count = -1

print(count)