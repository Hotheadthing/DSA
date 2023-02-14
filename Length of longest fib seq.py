A = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(2):
#     arr.append(A[i])
A = [1, 3, 7, 11, 12, 14, 18]
A = [ 8, 11, 20, 27, 33, 36 ]
# A = [ 4, 7, 13, 19, 26, 36, 39, 49, 56 ]
# A = [ 2, 8, 11, 14, 19, 26, 34, 37, 43, 52 ]
# A = [ 7, 11, 16, 19, 26, 35, 36, 46, 47, 53, 56, 62 ]
hmap = {}

for i in range(len(A)):
    hmap.__setitem__(A[i],1)


max_len = 0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        x = A[j]
        y = A[i] + A[j]
        length = 2
        while y in hmap:
            z = x+y
            x = y
            y = z
            length += 1
            max_len = max(max_len,length)

print(max_len)

