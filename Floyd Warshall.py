import math
A = 4
B = 6
C = 2
D = [1, 2, 3, 2, 4, 3]
E = [2, 3, 4, 4, 1, 1]
F = [4, 1, 1, 1, 1, 1]
G = [1, 1]
H = [2, 3]
A = 3
B = 3
C = 2
D = [1, 2, 1]
E = [2, 3, 3]
F = [3, 1, 1]
G = [2, 1]
H = [3, 2]
A = 15
B = 18
C = 29
D = [ 11, 2, 2, 6, 2, 8, 9, 3, 14, 15, 4, 14, 8, 7, 8, 6, 2, 12 ]
E = [ 2, 1, 1, 2, 1, 1, 7, 3, 2, 13, 2, 1, 6, 1, 7, 1, 2, 10 ]
F = [ 8337, 6651, 29, 7765, 3428, 5213, 6431, 2864, 3137, 4024, 8169, 5013, 7375, 3786, 4326, 6415, 8982, 6864 ]
G = [ 6, 2, 1, 15, 12, 2, 14, 10, 13, 15, 15, 4, 8, 7, 9, 4, 15, 13, 12, 5, 2, 10, 1, 11, 14, 7, 3, 13, 12 ]
H = [ 5, 2, 15, 13, 6, 2, 8, 6, 3, 13, 15, 3, 1, 1, 4, 4, 5, 8, 1, 3, 1, 10, 15, 9, 2, 1, 1, 10, 2 ]
#-1 0 -1 4024 -1 0 8379 -1 -1 4024 0 -1 5213 3786 18415 0 -1 -1 -1 -1 29 0 -1 18583 3137 3786 -1 -1 -1
A = 4
B = 6
C = 2
D = [ 1, 2, 3, 2, 4, 3 ]
E = [ 2, 3, 4, 4, 1, 1 ]
F = [ 4, 1, 1, 1, 1, 1 ]
G = [ 1, 1 ]
H = [ 2, 3 ]

dist_matrix = [[math.inf for i in range(A+1)] for j in range(A+1)]
hmap = {}
for i in range(B):
    conct1 = (D[i],E[i])
    conct2 = (E[i],D[i])
    distac = F[i]
    if conct1 not in hmap and conct2 in hmap:
        val = min(hmap[conct2],distac)
        hmap[conct1] = val
        hmap[conct2] = val
    elif conct2 not in hmap and conct1 in hmap:
        val = min(hmap[conct1],distac)
        hmap[conct2] = val
        hmap[conct1] = val
    elif conct2 in hmap and conct1 in hmap:
        val = min(hmap[conct2],hmap[conct1],distac)
        hmap[conct2] = val
        hmap[conct1] = val
    else:
        hmap[conct2] = distac
        hmap[conct1] = distac

for i in range(A+1):
    for j in range(A+1):
        if i == j:
            dist_matrix[i][j] = 0
        elif (i,j) in hmap:
            dist_matrix[i][j] = hmap[(i,j)]

for k in range(A+1):
    for i in range(A+1):
        for j in range(A+1):
            dist_matrix[i][j] = min(dist_matrix[i][j],dist_matrix[i][k] + dist_matrix[k][j])

for i in range(A+1):
    for j in range(A+1):
        if dist_matrix[i][j] == math.inf:
            dist_matrix[i][j] = -1

# print(dist_matrix)

result = []
for i in range(C):
    result.append(dist_matrix[G[i]][H[i]])

print(result)


