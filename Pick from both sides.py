A =[5, -2, 3, 1, 2]
D = []
B = 3
R = 0
L = B - R
Sum = 0
f_arr = []
arr = []
arr2 = []

for i in range(len(A)-1,-1,-1):
    D.append(A[i])
for i in range(L):
    Sum2 = 0
    Sum += A[i]
    arr.append(Sum)

    R = B - (i)
    for j in range(R):
        # print(j)
        Sum2 += D[j]
    arr2.append(Sum2)
print(arr2)
print(arr)
f_arr.append(arr[-1])
f_arr.append(arr2[0])
del arr[-1]
del arr2[0]
# print(arr)
# print(arr2)
for i in range(len(arr)):
    x = arr[i] + arr2[i]
    f_arr.append(x)
f_arr.sort()
print(f_arr[-1])

