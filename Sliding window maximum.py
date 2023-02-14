from collections import deque
A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
A = [2, 5, -1, 7, -3, -1, -2]
B = 4
A = [2, -1, 3]
B = 2
# A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
# B = 6
q = deque()
q1 = deque()
ans = []
ans1 = []
for r in range(len(A)):
    l = r - B + 1

    if len(q) != 0 and q[0] < l:
        q.popleft()

    if len(q1) != 0 and q1[0] < l:
        q1.popleft()

    while len(q1) != 0 and A[q1[-1]] >= A[r]:
        q1.pop()

    while len(q) != 0 and A[q[-1]] <= A[r]:
        q.pop()

    q.append(r)
    q1.append(r)

    if r >= B-1:
        ans.append(A[q[0]])
        ans1.append(A[q1[0]])


print(ans)
print(ans1)
min_max_sum = 0
for i in range(len(ans)):
    min_max_sum += (ans[i] + ans1[i]) % 1000000007


print(min_max_sum)
