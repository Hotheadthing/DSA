from numpy import *

# A = [[1, 2, 3, 0],
#      [4, 5, 6, 0],
#      [7, 8, 9, 0],
#      [0, 0, 0, 0]]
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = []
D = []
E = []
for i in range(len(A)+2):
    arr = zeros(len(A),int)
    B.append(arr)
m2 = matrix(B)
# for j in m2:

q = [[[0, 0,0]],
 [[0,0, 0]],
 [[0 ,0, 0]],
 [[0, 0, 0]],
 [[0, 0, 0]]]


for i in range(len(A)):
    x = A[i]
    x.reverse()
    A[i] = x
# print(A)
m = matrix(A)
# print(m.diagonal(offset = -2))

for i in range(len(A)-1,-(len(A)),-1):
    x = m.diagonal(offset = i)
    D.append(x)
print(*D)

m3 = q + D
print(m3)
# for j in D:
#     arr = array(j)
#     E.append(arr)
# print(E)

# D = array(D)

