from queue import Queue

A = [1, 2, 3, 4, 5]
B = 3
A = [5, 17, 100, 11]
B = 2
q = Queue()
arr = []
for i in range(len(A)):
    q.put(A[i])

n = len(A)
push = n - B

count = 0
while count != B:
    ans = q.get()
    arr.append(ans)
    count += 1

arr.reverse()

for i in range(len(arr)):
    q.put(arr[i])

for i in range(push):
    ans = q.get()
    q.put(ans)

arr1 = []

while q.empty() == False:
    ans = q.get()
    arr1.append(ans)

print(arr1)

