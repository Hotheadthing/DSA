from queue import Queue

A = 7
q = Queue()
q.put("1")
q.put("2")
q.put("3")
arr = []
count = 0

while count != A:
    ans = q.get()
    arr.append(int(ans))
    val = ans + "1"
    va1 = ans + "2"
    val2 = ans + "3"
    q.put(val)
    q.put(va1)
    q.put(val2)
    count += 1

print(arr)