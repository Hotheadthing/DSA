A = [0, 1, 0, 2]
A = [1, 2]
A.append(0)
storage = 0
m_left = []
maxleft = 0
maxright = 0
m_right = []

# Creating left max array
for i in range(len(A)-1):
    if A[i] > maxleft:
       m_left.append(maxleft)
       maxleft = A[i]
    else:
        m_left.append(maxleft)
print(m_left)

# Creating right max array
for i in range(len(A)-1,-1,-1):
    if A[i] > maxright:
        m_right.append(maxright)
        maxright = A[i]
    else:
        m_right.append(maxright)
m_right.reverse()
m_right.pop(-1)
print(m_right)

for i in range(len(A)-1):
    if i != 0:
        storage += max(0, min(m_left[i], m_right[i]) - A[i])
print(storage)

