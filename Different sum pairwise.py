A = [1, 3, 5]
mod = int(1e9)+7
x = 1
ans = 0
n=len(A)
for i in range(32):
    cnt = 0
    for j in A:
        if j&x!=0:
            cnt+=1
    ans+=cnt*(n-cnt)
    ans%=mod
    x=x*2
ans*=2
ans%=mod
print(ans)

print(2&1)