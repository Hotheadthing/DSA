# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
string = ""
string1 = ""
string2 = []

for i in range(len(l1)-1,-1,-1):
    string += str(l1[i])
for j in range(len(l2)-1,-1,-1):
    string1 += str(l2[j])
output = int(string) + int(string1)

output = str(output)

for d in range(len(output)-1,-1,-1):
    string2.append(int(output[d]))
print(string2)




