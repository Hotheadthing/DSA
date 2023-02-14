# A = [1, 4, 10]
# B = [2, 15, 20]
# C = [10, 12]
A = [3, 5, 6]
B = [2]
C = [3, 4]
A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]
n = [len(A)-1,len(B)-1,len(C)-1]
p1,p2,p3 = n
# print(p1,p2,p3)
diff = 9999999999999

while p1 >= 0 and p2 >= 0 and p3 >= 0:
    diff = min(diff,max(abs(A[p1]-B[p2]),abs(B[p2]-C[p3]),abs(C[p3]-A[p1])))

    if A[p1] >= B[p2] and A[p1] >= C[p3]:
        p1 -= 1

    elif B[p2] >= A[p1] and B[p2] >= C[p3]:
        p2 -= 1

    else:
        p3 -= 1
print(diff)

