A = [1, 2, 3, 4, 5]
B = 5
# A = [5, 10, 20, 100, 105]
# B = 110
# A = [ 1, 1000000000 ]
# B = 1000000000

i = 0
j = 1
sum = A[0]
n = len(A)
# print(n)
arr = []
while j <= n:
    if sum == B:
        arr.append(i)
        arr.append(j-1)
        break
    elif sum > B:
        sum -= A[i]
        i += 1
    else:
        if j > n-1:
            break
        else:
            sum += A[j]
            j += 1

if len(arr) == 0:
    print(-1)
else:
    print(A[arr[0]:arr[1]+1])