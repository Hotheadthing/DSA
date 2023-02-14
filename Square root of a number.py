A = 9
z = 0
q = 0
X =[]
r = A//2
# print(r)
while (r * r) > A:
    r = r//2
    X.append(r)
print(X)
print(r)
for j in range(r,X[-2]):
    # print(j)
    if j*j == A:
        z = j
    else:
        q = -1

if z != 0:
    print(z)
else:
    print(q)
