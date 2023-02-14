# A = [1, 3, -1]
# A = [2]
# A= [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ]
A = [ -98, -5, 37, -97, 38, 22, 70, 42, 61, 84 ]   # 191
# A = [2, 2, 2]
# A = [ 55, -8, 43, 52, 8, 59, -91, -79, -18, -94 ]

maximum1 = -9999999999
minimum1 = 9999999999
maximum2 = -9999999999
minimum2 = 9999999999

for i in range(len(A)):
    maximum1 = max(maximum1, A[i] + i)
    minimum1 = min(minimum1, A[i] + i)
    maximum2 = max(maximum2, A[i] - i)
    minimum2 = min(minimum2, A[i] - i)

print(max(maximum1-minimum1,maximum2-minimum2))