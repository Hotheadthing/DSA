A = [ 186, 256, 102, 377, 186, 377 ]   #De-Morgan's law
length = len(A)
Sum = 0
A.sort()
answer = []

for d in A:
    Sum = Sum^d

s_bin = bin(Sum)[2:]
print(s_bin)

index = 0
for i in range(len(s_bin)-1,-1,-1):
    if s_bin[i] == '1':
        index = len(s_bin)-1 - i
        break

element1 = 0
element2 = 0

for d in A:
    if d & (1<<index) != 0:
        element1 = element1 ^ d
    else:
        element2 = element2 ^ d
print([element1,element2])
