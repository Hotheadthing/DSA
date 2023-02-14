A = 37
B = 3
E =[]

A = bin(A)[2:]

for d in A:
    E.append(int(d))

for i in range(B,0,-1):
    E[-i] = 0

string = ''.join(str(x) for x in E)

x = int(string,2)
print(x)




# for i in range(B,0,-1):
#      A = A & (~(1 << i))
#      print(A)