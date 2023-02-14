A = 3
arr = []
def move(start,target,mid,n):
    if n == 0:
        return
    move(start,mid,target,n-1)
    arr.append([n,start,target])
    move(mid,target,start,n-1)

x = move(1,3,2,A)
print(*arr)



