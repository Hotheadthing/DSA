
A = "....x..xx...x.."
A = "....xxx"
A = ".x.x.x..x"
# A = "x.xx..."
# A = "xx.....xx.x..xxxx..xxxx.xx..xx..x.xxxx"     #79
arr = []
seated = 0

for i in range(len(A)):
    if A[i] == "x":
        arr.append(i-seated)
        seated += 1

print(arr)

if seated == len(A) or seated == 0:
    print(0)

median = (seated-1)//2

median_val = arr[median]

mod = 10000003
jumps = 0
for i in range(len(arr)):
    jumps = (jumps % mod + abs(arr[i] - median_val) % mod) % mod

print(jumps)


