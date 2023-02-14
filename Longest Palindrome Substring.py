A = "ac"
length = len(A)
ans = 0
b = []
o_len = 0
r_len = 0
c = []
for i in range(length):
    count = 1
    left = i-1
    right = i+1
    while (left >= 0 and right < length):
        if A[left] == A[right]:
            count += 2
            x = right - left
            if x > o_len:
                o_len = x
                b.append(left)
                b.append(right)
        else:
            break
        left -= 1
        right += 1
    ans = max(ans,count)
for i in range(length-1):
    count = 0
    left = i
    right = i + 1
    while (left >= 0 and right < length):
        if A[left] == A[right]:
            count +=2
            x = right - left
            if x > r_len:
                r_len = x
                c.append(left)
                c.append(right)
        else:
            break
        left -=1
        right +=1
    ans = max(ans,count)
print(b)
print(c)
print(ans)
if b == []:
    m_o_len = 0
else:
    m_o_len = b[-1] - b[-2]
if c == []:
    m_e_len = 0
else:
    m_e_len = c[-1] - c[-2]

if ans ==1:
    print(A[0])
else:
    if m_o_len > m_e_len:
        print(A[b[-2]:b[-1]+1])
    else:
        print(A[c[-2]:c[-1]+1])
