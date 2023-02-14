import heapq

# A = 2
# B = 3
# C = 5
# D = 5
# A = 3
# B = 2
# C = 7
# D = 3
A = 3
B = 11
C = 7
D = 50
# 3 7 9 11 21 27 33 49 63 77 81 99 121 147
# 189 231 243 297 343 363 441 539 567 693 729 847
# 891 1029 1089 1323 1331 1617 1701 2079 2187 2401 2541
# 2673 3087 3267 3773 3969 3993 4851 5103 5929 6237
# 6561 7203 7623
q = []
heapq.heapify(q)
heapq.heappush(q, A)
heapq.heappush(q, B)
heapq.heappush(q, C)
result = []
hmap = {}
while D != 0:
    val = heapq.heappop(q)
    if len(result) == 0:
        result.append(val)
        hmap.__setitem__(val, 1)
        heapq.heappush(q, val * val)
        D -= 1
    else:
        if val not in hmap:
            result.append(val)
            hmap.__setitem__(val, 1)
            D -= 1
            for i in range(len(result)):
                heapq.heappush(q, val * result[i])

print(result)
