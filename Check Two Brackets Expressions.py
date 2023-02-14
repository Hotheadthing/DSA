# A = "-(a+b+c)"
# B = "-a-b-c"
A = "-(-(-(-a+b)-d+c)-q)"
B = "a-b-d+c+q"   #1
# A = "a+b-c+d-e"
# B = "(a+b-c+d-e)"
# A = "a-b-(c-d)"
# B = "a-b-c-d"
# A = "-(a+((b-c)-(d+e)))"
# B = "-(a+b-c-d-e)"   #1
# A = "-(-(-(-a+b)-d+c)-q)"
# B = "-(-(a-b-d+c+q))"
# A = "-(a-(-z-(b-(c+t)-x)+l)-q)"
# B = "-a+l-b-(z-(c+t)-x-q)"
# A = "a+b-c+d+e-f-g+h-i+j"
# B = "-(a-b+c+d+e-f+g-h-i+j)"

hmap1 = {}
hmap2 = {}

def find(a):
    minus_count = 0
    arr = []
    for i in range(len(a)):
        if ord('a') <= ord(a[i]) <= ord('z'):
            if a[i-1] == "(":
                sign = "+"
            elif i == 0:
                sign = "+"
            else:
                sign = a[i-1]
            if minus_count % 2 != 0:
                if sign == "+":
                    sign = "-"
                else:
                    sign = "+"
            # print(a[i],sign)
            # print(minus_count)
            hmap1.__setitem__(a[i], sign)
        elif a[i] == "-" and a[i+1] == "(":
            minus_count += 1
            arr.append("-(")
            # print(minus_count,i)
            # arr.append("(")
        elif a[i] == ")":
            if len(arr) != 0:
                val = arr.pop()
                if val == "-(":
                    minus_count -= 1
        elif a[i] == "(" and a[i-1] != "-":
            arr.append("(")

find(A)
# print(hmap1)
hmap2 = hmap1
hmap1 = {}
find(B)
print(hmap2)
print(hmap1)

if hmap2 == hmap1:
    print("1")
else:
    print("0")




