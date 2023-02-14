A = "abcabcbb"
A = "AaaA"
A_map = {}
length = 0
n = len(A)
l = 0
r = 0
while r < n:
    if A[r] not in A_map:
        A_map.__setitem__(A[r],1)
        r += 1
    else:
        cur_len = r - l
        length = max(length,cur_len)
        A_map[A[r]] += 1
        while A_map[A[r]] != 1:
            A_map[A[l]] -= 1
            if A_map[A[l]] == 0:
                del A_map[A[l]]
            l += 1
        r += 1
        # print(A_map)
print(length)
