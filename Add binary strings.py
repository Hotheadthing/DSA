A = "100"
B = "11"

#My Solution
# a = []
# b = []
# s_a = 0
# s_b = 0
# r = 0
# for i in A:
#     a.append(int(i))
# for j in B:
#     b.append(int(j))
#
# a.reverse()
# for h in range(len(a)):
#     s_a += a[h] * 2**(h)
#
# b.reverse()
# for m in range(len(b)):
#     s_b += b[m] * 2**(m)
#
# r = s_b + s_a
# r = (bin(r)[2:])
# print(r)

#Using Inbuilt function

sum = bin(int(A, 2) + int(B, 2))
print(sum[2:])




