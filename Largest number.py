#A = [3, 30, 34, 5, 9]
A = [ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]     #9648527226766636354854724412368319
A = ['3', '30', '34', '5', '9']
if len(A) == 1:
    print(str(A[0]))
for i in range(len(A)):
    A[i] = str(A[i])


def sort():
    for i in range(len(A) - 1):
        if A[i + 1] > A[i]:
            A[i], A[i + 1] = A[i + 1], A[i]
    return (A)

for i in range(len(A)-1):
    x = sort()

result=''.join(x)

if(result=='0'*len(result)):
    print('0')
else:
    print(result)
# for i in range(len(A)):
#     for j in range(1+i, len(A)):
#         if A[j] > A[i]:
#             A[i], A[j]= A[j], A[i]
# result=''.join(A)
#
# if(result=='0'*len(result)):
#     print('0')
# else:
#     print(result)
