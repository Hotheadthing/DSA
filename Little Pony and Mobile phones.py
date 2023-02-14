# A = [ 25, 43, 47, 95, 98 ]
# B = [ 184, 533, 811, 330, 509, 192 ]

A= [3, 4, 4, 6]
B= [20, 4, 10, 2]
# count = []
#
# for i in range(1,len(A)):
#     A[i] = A[i] + A[i-1]
# print(A)
# print(B)
# for digit in B:
#     i = len(A)//2
#     # print(i)
#     if digit > A[-1]:
#         count.append(len(A))
#     elif digit < A[0]:
#         count.append(0)
#     elif digit > A[i]:
#         while digit > A[i]:
#             i = i+1
#         count.append(len(A[:i]))
#         print(f"the {A[:i]}")
#     elif digit < A[i]:
#         while digit < A[i]:
#             i = i-1
#         count.append(len(A[:i+1]))
#         # print(i)
# print(count)
# # print(A[:2])
#

prefix_sum = []
summation = 0
for value in A:
    summation +=value
    prefix_sum.append(summation)
final_answer = []
print (prefix_sum)
print(B)
for value in B:
    low, up = 0, len(prefix_sum)
    while(low < up):
        mid = (low + up)//2
        print(low)
        print(f"the {up}")
        if value < prefix_sum[mid]:
            up = mid
        else:
            low = mid + 1
    final_answer.append(low)
print(final_answer)
