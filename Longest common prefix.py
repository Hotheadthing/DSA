#A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abab", "a", "abcd"]
index = []
length = len(A)
x = 9999999
y = ""
for i in range(length):
    l = len(A[i])
    if l < x:
        x = l
        y = A[i]
if length == 1:
    print(A[0])
else:
    for j in range(len(y)):
        for i in range(length-1):
            if (A[i][j]!=A[i+1][j]):
                index.append(j)
            else:
                continue
if len(index) == 0:
    print(y)
else:
    z = index[0]
    print(y[0:z])




