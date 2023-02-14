import math
A = [1, 2, 3]
# A = [9,4,9,1,5]
A = [ 9, 9, 3, 6, 7, 5 ]
# A = [ 8, 7, 5, 6, 8, 1 ]
# A = [ 56, 5, 40, 92, 58, 62, 48, 88, 24, 28, 43, 60, 60, 95 ]
arr = []
def isprime(n):
    if n <=1:
        return False
    x = math.floor(math.sqrt(n))
    for i in range(2, x+1):
        if n % i == 0:
            return False
    return True
ans = []
for d in A:
    x = isprime(d)
    ans.append(x)

print(ans)
count = 1
for d in ans:
    if d == True:
        count = (count % 1000000007 * 2) % 1000000007
print(count-1)





