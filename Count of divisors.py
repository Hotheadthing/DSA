import math
A = [2, 3, 4, 5]
# A = [8, 9, 10]
A = [ 20, 39, 29, 51, 96, 32, 35, 50, 57, 7, 59, 51, 85, 55, 8, 26, 15, 4, 4, 18, 32, 49, 40, 46, 83, 77, 100, 92 ]
arr = []

val = max(A)
A1 = []
v1 = math.floor(math.sqrt(val))
for i in range(val+1):
    if i == 0 or i == 1:
        A1.append(1)
    else:
        A1.append(2)

for i in range(2,v1+1):
    for j in range(2*i,val+1,i):
        # print(i,j)
        if j % i == 0:
            if j // i != i:
                A1[j] += 2
            else:
                A1[j] += 1
#
print(A1[20])
# ans = []
# for d in A:
#     ans.append(A1[d])
# print(ans)






