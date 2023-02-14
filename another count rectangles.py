A = [1, 2]
B = 5
A = [1, 2]
B = 1
A = [ 1, 2, 3, 4, 5 ]
B = 5
A = [ 8, 15, 19, 21, 26, 30, 45, 48, 59, 66, 67, 72, 134, 143, 152, 174, 182, 185, 201, 207, 229, 234, 250, 253, 261, 303, 306, 312, 330, 359, 382, 385, 398, 427, 439, 442, 443, 455, 457, 484, 491 ]
B = 902
without_duplicates = []
for d in A:
    if d not in without_duplicates:
        without_duplicates.append(d)
count = 0
# print(len(A),len(without_duplicates))
l = 0
n = len(without_duplicates)
r = n-1

while l < r:
    if without_duplicates[l]*without_duplicates[r] < B:
        val = r-l
        count += val
        l += 1
    else:
        r -= 1
count = count * 2

for i in range(len(A)):
    if A[i] * A[i] < B:
        count += 1
    else:
        break
print(count)


