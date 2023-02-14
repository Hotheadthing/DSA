from queue import Queue

q = Queue()
A = [ 6, 7, 1, 2, 4, 5, 8, 3 ]
B = [ 3, 7, 2, 5, 1, 8, 4, 6 ]
q2 = Queue()
count = 0

for i in range(len(A)):
    q.put(A[i])

for i in range(len(B)):
    q2.put(B[i])

while q2.empty() == False:
    b_val = q2.get()
    a_val = q.get()
    while a_val != b_val:
        count += 1
        q.put(a_val)
        a_val = q.get()
    count += 1
print(count)


