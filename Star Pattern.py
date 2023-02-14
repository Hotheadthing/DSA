A = 7
B = A*2
z = '*'
s = z * B
s3 = ' '
print(s)
for i in range(A-1,0,-1):
    print(s[:i] + s3*(B-i*2) + s[:i])
for i in range(1,A,1):
    print(s[:i] + s3 * (B - i * 2) + s[:i])
print(s)
