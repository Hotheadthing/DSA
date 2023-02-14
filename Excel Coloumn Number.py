Input = "ZY"
length = len(Input)
x = Input.lower()
result = 0
last = ord(x[-1]) - 96
for i in range(len(Input)):
    result += (ord(x[i])-96) *(26**(length -(i+1)))
print(result)

