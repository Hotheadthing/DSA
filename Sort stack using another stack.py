from collections import deque
# A = [5, 4, 3, 2, 1]
# A = [5, 17, 100, 11]
A = [ 17, 88 ]
A = [ 66, 96, 43, 28, 14, 1, 41, 76, 70, 81, 22, 11, 42, 78, 4, 88, 70, 43, 90, 6, 12 ]
q = deque()
arr = []
while A != 0:
    if len(q) == 0:
        q.append(A[-1])
        A.pop()
    else:
        if len(q) != 0:
            if A[-1] > q[-1]:
                q.append(A[-1])
                A.pop()
            else:
                ans = A[-1]
                A.pop()
                while ans < q[-1]:
                    A.append(q[-1])
                    q.pop()
                    if len(q) == 0:
                        break
                q.append(ans)
        if len(A) == 0:
            break

for i in range(len(q)):
    arr.append(q[i])

print(arr)