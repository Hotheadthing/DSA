A = 3
B = [1, 2]
C = [2, 3]
A = 2
B = [1, 2]
C = [2, 1]
test = []
test.append(B)
test.append(C)
print(test)

premap = {c:[] for c in range(A+1)}
print(premap)

for prcrs,pocrs in test:
    premap[pocrs].append(prcrs)

print(premap)

visit = set()


def dfs(crs):
    if crs in visit:
        return False
    if premap[crs] == []:
        return True
    visit.add(crs)
    for val in premap[crs]:
        if dfs(val) == False:
            return False
    visit.remove(crs)
    premap[crs] = []
    return True


for i in range(1,A+1):
    if dfs(i) == False:
        print(False)
        break
print(True)

