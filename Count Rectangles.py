A = [1, 1, 2, 2]
B = [1, 2, 1, 2]
A = [1, 1, 2, 2, 3, 3]
B = [1, 2, 1, 2, 1, 2]

mMap = {}
n = len(A)
m = len(B)
arr = []
for i in range(n):
    x = [A[i],B[i]]
    arr.append(x)
    mMap.__setitem__(str(x),1)

print(mMap)
print(arr)
count  = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i][0] != arr[j][0] and arr[i][1] != arr[j][1]:
            # print(arr[i],arr[j])
            co_ordinate1 = [arr[i][0],arr[j][1]]
            co_ordinate2 = [arr[j][0],arr[i][1]]
            # print(f"the value of co-ordinates are {co_ordinate2,co_ordinate1}")
            if str(co_ordinate1) in mMap and str(co_ordinate2) in mMap:
                count += 1
print(count//2)

