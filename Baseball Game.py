ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1","C"]
arr = []
for i in range(len(ops)):
    if ops[i] == "C":
        arr.pop(-1)
    elif ops[i] == "D":
        z = 2*arr[-1]
        arr.append(z)
    elif ops[i] == "+":
        y = arr[-2] + arr[-1]
        arr.append(y)
    else:
        arr.append(int(ops[i]))

ans = 0
for d in arr:
    ans += d
print(ans)