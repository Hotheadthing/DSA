A = [2,2]
A = [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]
# A = [3,11,-1,5]
# A = [2,2]
A.sort()
# print(A)
sub1 = []
sub2 = []
n = len(A)
for i in range(0,n,2):
    sub1.append(A[i])
    sub2.append(A[i+1])

print(sub1)
print(sub2)
minimum = 0
for i in range(len(sub1)):
    minimum += abs(sub1[i]-sub2[i])

print(minimum)
A.sort(reverse=True)
s1 = []
s2 = []
for i in range(n//2):
    s1.append(A[i])
for j in range(n//2,n):
    s2.append(A[j])
# print(s1)
s2.sort()
# print(s2)
maximum = 0
for i in range(len(s1)):
    maximum += abs(s1[i] - s2[i])
print([maximum,minimum])