A = "ADOBECODEBANC"
B = "ABC"
# A = "Aa91b"
# B = "ab"

B_map = {}
n = len(B)

for i in range(n):
    if B[i] not in B_map:
        B_map.__setitem__(B[i], 1)
    else:
        B_map[B[i]] += 1

print(B_map)


def is_present(B_map, A_map):
    for d in B_map:
        if d in A_map:
            if B_map[d] <= A_map[d]:
                continue
            else:
                return False
        return False
    return True


l = 0
r = len(B_map) - 1
A_map = {}
length = 99999999999999
string = ''
for i in range(r + 1):
    if A[i] not in A_map:
        A_map.__setitem__(A[i], 1)
    else:
        A_map[A[i]] += 1
while r < len(A):
    x = is_present(B_map, A_map)
    if x is True:
        cur_length = r - l + 1
        if cur_length < length:
            length = cur_length
            string = A[l:r+1]
        A_map[A[l]] -= 1
        if A_map[A[l]] == 0:
            del A_map[A[l]]
        l += 1
        while A[l] not in B_map:
            A_map[A[l]] -= 1
            if A_map[A[l]] == 0:
                del A_map[A[l]]
            l += 1
    else:
        r += 1
        if r < len(A):
            if A[r] not in A_map:
                A_map.__setitem__(A[r],1)
            else:
                A_map[A[r]] += 1
print(string)

