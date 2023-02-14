A = [1,3,2,4,5]
A = [ 1, 2, 3, 5, 6, 13, 15, 16, 17, 13, 13, 15, 17, 17, 17, 17, 17, 19, 19 ]
B = []
for d in A:
    B.append(d)
minimum = 999999999999
maximum = -99999999999
B.sort()
# print(A)
# print(B)
for i in range(len(B)):
    if A[i] != B[i]:
        minimum = min(minimum,i)
        maximum = max(maximum,i)


print(minimum,maximum)



