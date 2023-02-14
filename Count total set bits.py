A = 3
n = A+1
ans = 0
set_size = 2
print(n)
while set_size//2 <= n:
    ans += (n//set_size) * (set_size//2)
    ans %= 1000000007
    print(n % set_size)
    if (n % set_size) > (set_size//2):
        x = (n % set_size) - (set_size//2)
        # print(x)
        ans %= 1000000007
    set_size *= 2
    # print(set_size)
# print(ans)

