import math
A = 'pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn'
# A = "ABEC"
# count = 0
# length = len(A)
# for i in range(length):
#     if A[i] == 'a' or A[i] == 'e':
#         count += (length - i)
#     elif A[i] == 'i' or A[i] == 'o':
#         count += (length - i)
#     elif A[i] == 'u' or A[i] == 'A':
#         count += (length - i)
#     elif A[i] == 'E' or A[i] == 'I':
#         count += (length - i)
#     elif A[i] == 'O' or A[i] == 'U':
#         count += (length - i)
# count = count % 10003
# print(count)
length = len(A)
total = 0
for i in range(length):
    if A[i] == 'a' or A[i] == 'e':
        total += length - i
    elif A[i] == 'i' or A[i] == 'o':
        total += length - i
    elif A[i] == 'u' or A[i] == 'A':
        total += length - i
    elif A[i] == 'E' or A[i] == 'I':
        total += length - i
    elif A[i] == 'O' or A[i] == 'U':
        total += length - i
total = total % 10003
print(total)
