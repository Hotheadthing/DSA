A = 20
B = 33
C = 20
D = []
D.append(A)
D.append(B)
D.append(C)
D.sort()
result = ""
for d in D:
    result = result + str(d)
print(result)

