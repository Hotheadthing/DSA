A = [2, 4, 8, 6]
length = len(A)
index = []
countx = -1
county = -1
z = 0
if length == 2 or length % 2 != 0:
    print("NO")
elif A[0] % 2 != 0 or A[-1] % 2 != 0:
    print("NO")
else:
    for i in range(length-1,-1,-1):
        if A[i-1] % 2 ==0 and A[i-2] % 2 ==0:
            countx = (length-1) - (i-1)
            county = (i-2)
            if countx % 2 != 0 and county % 2 != 0:
                print("YES")
                break








