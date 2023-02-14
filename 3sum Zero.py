A = [-1,0,1,2,-1,4]
A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
A.sort()
print(A)
n = len(A)
def two_sum(i,j,target,A):
    arr = []
    while j > i:
        if A[j] + A[i] == target:
            x = [-target,A[i],A[j]]
            if x not in arr:
                arr.append(x)
            i += 1
            j -= 1
        elif A[j] + A[i] > target:
            j -= 1
        else:
            i += 1
    return arr
arr = []
valuestaken = []
for i in range(n):
    x = 0 - A[i]
    val = i+1
    if x not in valuestaken:
        valuestaken.append(x)
        ans = two_sum(val,n-1,x,A)
        if ans != []:
            for j in range(len(ans)):
                arr.append(ans[j])
print(arr)
