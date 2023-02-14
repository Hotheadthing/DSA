B = "00000000000000000000000000000000"
l_B = len(B)
decNum = 3
C = (bin(decNum)[2:])
print(C)
l_C = len(C)
D = []
for digit in C:
    D.append((digit))
print(D)
for i in range(l_B-l_C):
    D.insert(0,str(0))
print(D)
D.reverse()
print(D)
X = ''.join(D)
print(X)

s = int(X,2)
print(s)