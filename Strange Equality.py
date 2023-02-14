import copy
A = 5
B = copy.deepcopy(A)
C = ""

z = (bin(A)[2:])
x = 0
for i in range(len(z)):
    B = B ^ (1<<i)
print(B)

for i in range(len(z)+1):
    if i == 0:
        C = C + "1"
    else:
        C = C + "0"
C = (int(C,2))
print(B^C)
# print(z)
# print(bin(2)[2:])