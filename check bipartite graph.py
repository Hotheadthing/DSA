A = 3
B = [ [0, 1], [0, 2], [1, 2] ]
A = 2
B = [ [0, 1] ]
A = 10
B = [
  [7, 8],
  [1, 2],
  [0, 9],
  [1, 3],
  [6, 7],
  [0, 3],
  [2, 5],
  [3, 8],
  [4, 8]
]
set1 = set()
set2 = set()

for i in range(len(B)):
    if B[i][0] not in set1:
        set1.add(B[i][0])
        if B[i][0] in set2:
            print(0)
            break
    if B[i][1] not in set2:
        set2.add((B[i][1]))
        if B[i][1] in set1:
            print(0)
            break

print(set1)
print(set2)