A="AbcaZeoB"
A = A + A
B = []
for d in A:
    B.append(d)
vowels = "aeiou"
C = []
for i in range(len(B)):
    x = ord(B[i])
    if x >= 65 and x <= 90:
        continue
    else:
        if B[i] in vowels:
            B[i] = '#'
            C.append(B[i])
        else:
            C.append(B[i])
C = ''.join(C)
print(C)
