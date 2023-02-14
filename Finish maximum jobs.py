import heapq
A = [1, 5, 7, 1]
B = [7, 8, 8, 8]
# A = [3, 2, 6]
# B = [9, 8, 9]
end_time = []

for i in range(len(B)):
    heapq.heappush(end_time,(B[i],A[i]))

print(end_time)

number_of_jobs = 1
e,s = heapq.heappop(end_time)
for i in range(len(end_time)):
    e1,s1 = heapq.heappop(end_time)
    if s1 >= e:
        number_of_jobs += 1
        e = e1
        s = s1


print(number_of_jobs)




