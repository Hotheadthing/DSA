A = 2
B = 4
C = [ 8, 7 ]
Maximum = []
C_Max = []
Max = 0
z = 0
y = []
if B in C:
    y.append(B)
for i in range(A):
    if i ==0:
        C[i] = C[i]
    else:
        C[i] = C[i] + C[i-1]
print(C)
if C[-1] <= B:
    y.append(C[-1])
elif C[0] <= B:
    y.append(C[0])
elif C[0] > B:
    y.append(0)
else:
    for j in range(A):
        S = C[j]
        if j == 0 and C[j] == B:
            y.append(B)
            break
        for a in range(j+1,A,1):
            z = C[a] - S
            y.append(z)

# for digit in y:
#     if digit <= B and digit >= Max:
#         Maximum.append(digit)
# Maximum.sort()
# for d in C:
#     if d <= B:
#         C_Max.append(d)
# C_Max.sort()
# print(Maximum)
# print(C_Max)
# if C_Max == []:
#     print(Maximum[-1])
# elif Maximum[-1] > C_Max[-1]:
#     print(Maximum[-1])
# else:
#     print(C_Max[-1])










