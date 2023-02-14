import sys
sys.setrecursionlimit(10**6)
A = 26+2
arr = [-1] * (A+1)
# print(arr)

def pattern(a,range):
    if range == 0:
        return 0
    if 0 < range <= 2:
        return 1

    if a[range] != -1:
        return a[range]

    val = pattern(a,(range-1)%10000007) + pattern(a,(range-2)%10000007)
    a[range] = val
    return val % 10000007

print(pattern(arr,A))
print(arr)
