from numpy import *
A = 3
limit = A*A
B = []
for i in range(1,limit+1,1):
    B.append(i)
B = array(B)
answer = B.reshape(A,A)
x = answer[-1]

x = list(x)
x.reverse()

answer[-1] = x
print(answer)