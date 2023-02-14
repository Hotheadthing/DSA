A = [1, 2, 3, 4, 5]
B = 5
A = [5, 10, 20, 100, 105]
B = 110
i = 0
n = len(A)
j = n-1
# print(n)
count = 0
while j > i:
    if A[i] + A[j] == B:
        count += 1
        i += 1
        j -= 1
    elif A[i] + A[j] > B:
        j -= 1
    else:
        i += 1
print(count)