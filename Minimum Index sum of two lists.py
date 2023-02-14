list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
list1 = ["k","KFC"]
list2 = ["k","KFC"]
count = 9999999
ans = []

for i in range(len(list1)):
    if list1[i] in list2:
        z = (i + list2.index((list1[i])))
        if z == count:
            ans.append(list1[i])
        elif z < count:
            ans = []
            ans.append(list1[i])
            count = z
print(ans)