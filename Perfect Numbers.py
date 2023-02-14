from queue import Queue
A = 4
one = "11"
two = "22"
q = Queue()
q.put("11")
q.put("22")
count = 0
ans = 0
while count != A:
    ans = q.get()
    n = len(ans)//2
    val = ans[0:n] + "11" + ans[n:]
    val1 = ans[0:n] + "22" + ans[n:]
    q.put(val)
    q.put(val1)
    count += 1

print(ans)






