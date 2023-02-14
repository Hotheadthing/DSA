A = "abcd"
A = "aab"
A = "gbedggcjac"  # 1
A = "wwuvuw" #0

even = []
odd = []


def check(s):
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) == 1:
            return False
    return True

for i in range(len(A)):
    if ord(A[i]) % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])

even.sort()
odd.sort()

bol = check(even + odd)
bol1 = check(odd + even)
if bol == True:
    print(1)
elif bol1 == True:
    print(1)
else:
    print(0)

