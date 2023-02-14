A = 47
A = 9
val = 0
for i in range(10):
    if 5**i > A:
        val = i-1
        break
arr = []
coins = 0
for i in range(val):
    ans = A // 5**(val-i)
    coins += ans
    arr.append(5**(val-i) * ans)
    A = A - arr[-1]

print(coins+A)