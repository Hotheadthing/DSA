A = "abc"
B = "abcbacabc"
A = "aca"
B = "acaa"
mMap = {}
window_size = len(A)

for i in range(len(A)):
    if A[i] not in mMap:
        mMap.__setitem__(A[i],1)
    else:
        mMap[A[i]] += 1

strng_in_B = {}
for i in range(window_size):
    if B[i] not in strng_in_B:
        strng_in_B.__setitem__(B[i],1)
    else:
        strng_in_B[B[i]] += 1

def match_map(mMap,strng_in_B):
    for d in mMap:
        if d in strng_in_B:
            if mMap[d] == strng_in_B[d]:
                continue
            else:
                return False
        else:
            return False
    return True


count = 0
k = window_size - 1
loop_size = len(B) - k
l = 0
r = k
for i in range(loop_size):
    if i == 0:
        if match_map(mMap,strng_in_B) == True:
            count += 1
    else:
        strng_in_B[B[l]] -= 1
        if strng_in_B[B[l]] == 0:
            del strng_in_B[B[l]]
        l += 1
        r += 1
        if B[r] not in strng_in_B:
            strng_in_B.__setitem__(B[r],1)
        else:
            strng_in_B[B[r]] += 1

        if match_map(mMap, strng_in_B) == True:
            count += 1
print(count)



