A = "1001"
B = "0011"


# A = "111"
# B = "111"
def compute_z(s, z):
    l = 0
    r = 0
    n = len(s)
    for i in range(1, n, 1):
        if (i > r):
            l = i
            r = i
            while (r < n and s[r - l] == s[r]):
                r += 1
            z[i] = r - l
            r -= 1

        else:
            k = i - l
            if (z[k] < r - i + 1):
                z[i] = z[k]

            else:
                l = i
                while (r < n and s[r - l] == s[r]):
                    r += 1
                z[i] = r - l
                r -= 1


b = B + B
print(b)
b = b[0:len(b) - 1]
print(b)
ans = 0
s = A + "$" + b
n = len(s)
z = [0 for i in range(n)]
compute_z(s, z)
for i in range(1, n, 1):
    if (z[i] == len(A)):
        ans += 1
print(ans)
