# A = "111000"    #3
# A = "111011101"    #7
# A = "11010110000000000"    #4
# A = "1000010001111110"    #7
# A = "0111001101111101010010"  #8
# A = "11110000100111000101110010111101"   #6
# A = "00000011111111"  #8
# A = "0111110110"   #7
# A = "10110011001001101110100"  # 6
A = "00000011111111"
B = []
for i in A:
    B.append(int(i))
n = len(A)
c = 0
for i in range(n):
    if B[i] == 1:
        c += 1
    if c == n:
        print(n)
    # elif c == 0:
    #     print(c)
ans = 0
for i in range(n):
    l = 0
    r = 0
    if B[i] == 0:
        for j in range(i - 1, -1, -1):
            if B[j] == 1:
                l += 1
            else:
                break
        for j in range(i + 1, n):
            if B[j] == 1:
                r += 1
            else:
                break
        cnt_ = l + r
        if cnt_ < c:
            cnt_ = cnt_ + 1
        if ans < cnt_:
            ans = cnt_
print(ans)
