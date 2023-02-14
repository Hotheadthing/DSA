A = [
        [1, 2, 3, 4],
        [2, 3, 4, 5]
     ]

A = [
        [1],
        [2]
     ]

A = [
  [14, 87, 36, 23],
  [37, 59, 21, 68]
]
# colm1 = A[0]
# colm2 = A[1]
#
# print(colm1,colm2)
A = [[37,87,36,68]]
val1, val2 = 0, 0
if len(A[0]) == 1:
    val2 = A[0][0]
else:
    for n in A[0]:
        temp = max(n+val1,val2)
        val1 = val2
        val2 = temp

print(val2)

# vl1, vl2 = 0,0
# if len(A[1]) == 1:
#     vl2 = A[1][0]
# else:
#     for n in A[1]:
#         temp = max(n+vl1,vl2)
#         vl1 = vl2
#         vl2 = temp
#
# print(vl2)
#
# print(max(val2,vl2))



