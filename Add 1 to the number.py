A = [0, 2, 3]
string = ""
z = []
for i in range(len(A)):
    string += str(A[i])

y = int(string) + 1
l = str(y)
for d in l:
    z.append(int(d))

print(z)



