import  math
arr = [81, 84, 28, 50, 39, 6, 39, 83, 8, 73]
for j in arr:
        count=0
        X=[]
        Z = int(math.sqrt(j))
        for digit in range(1,Z+1):
            if j % digit == 0:
                Y = j // digit
                X.append(digit)
                X.append(Y)
        X.remove(j)
        for digit in X:
            count += digit
        if count != j:
            print("NO")
        else:
            print("YES")

# Z = int(math.sqrt(A))
# for digit in range(1,Z+1):
#     if A % digit == 0:
#         Y = A // digit
#         X.append(digit)
#         X.append(Y)
# X.remove(A)
# for digit in X:
#     count += digit
# if count != A:
#     print("NO")
# else:
#     print("Yes")
