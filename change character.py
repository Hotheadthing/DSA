A = "abcabbccd"
B = 3
C = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(A)):
    if A[i] == 'a':
        C[0] += 1
    if A[i] == 'b':
        C[1] += 1
    if A[i] == 'c':
        C[2] += 1
    if A[i] == 'd':
        C[3] += 1
    if A[i] == 'e':
        C[4] += 1
    if A[i] == 'f':
        C[5] += 1
    if A[i] == 'g':
        C[6] += 1
    if A[i] == 'h':
        C[7] += 1
    if A[i] == 'i':
        C[8] += 1
    if A[i] == 'j':
        C[9] += 1
    if A[i] == 'k':
        C[10] += 1
    if A[i] == 'l':
        C[11] += 1
    if A[i] == 'm':
        C[12] += 1
    if A[i] == 'n':
        C[13] += 1
    if A[i] == 'o':
        C[14] += 1
    if A[i] == 'p':
        C[15] += 1
    if A[i] == 'q':
        C[16] += 1
    if A[i] == 'r':
        C[17] += 1
    if A[i] == 's':
        C[18] += 1
    if A[i] == 't':
        C[19] += 1
    if A[i] == 'u':
        C[20] += 1
    if A[i] == 'v':
        C[21] += 1
    if A[i] == 'w':
        C[22] += 1
    if A[i] == 'x':
        C[23] += 1
    if A[i] == 'y':
        C[24] += 1
    if A[i] == 'z':
        C[25] += 1
C.sort()
count = 0
for i in range(len(C)):
    if C[i] <= B and C[i] != 0:
        B = B- C[i]
        C[i] = 0
    elif C[i] > B:
        count += 1
    elif B == 0:
        break

print(count)