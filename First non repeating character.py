from collections import deque
q = deque()
hmap = {}
A = "abadbc"
# A = "abcabc"
# A = "jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"
str = ""

for i in range(len(A)):
    if A[i] not in hmap:
        hmap.__setitem__(A[i],1)
        q.append(A[i])
    else:
        if A[i] != q[0]:
            hmap[A[i]] += 1
        else:
            q.popleft()
            if len(q) != 0:
                while hmap[q[0]] > 1:
                    q.popleft()
    if len(q) == 0:
        str += "#"
    else:
        str += q[0]
print(str)