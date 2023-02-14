A = 3
B = [[1, 2, 2],
     [1, 3, 2],
     [2, 3, 3]
     ]
# A = 7
# B = [
#   [1, 2, 468],
#   [2, 3, 335],
#   [3, 1, 501],
#   [2, 4, 170],
#   [2, 5, 725],
#   [2, 7, 479],
#   [4, 6, 359],
#   [5, 6, 963]
# ]
# A = 3
# B = [
#     [1, 2, 465],
#     [1, 3, 706],
#     [2, 3, 146]
# ]  # 101
A = 68
B = [
  [26, 43, 131],
  [5, 40, 847],
  [23, 35, 988],
  [21, 59, 446],
  [29, 42, 806],
  [6, 15, 617],
  [6, 24, 751],
  [15, 40, 490],
  [13, 15, 339],
  [1, 48, 964],
  [27, 39, 136],
  [9, 42, 698],
  [49, 67, 210],
  [40, 58, 631],
  [47, 54, 225],
  [2, 10, 909],
  [45, 59, 738],
  [2, 8, 475],
  [14, 27, 921],
  [40, 57, 373],
  [13, 58, 294],
  [2, 46, 856],
  [52, 57, 735],
  [8, 21, 562],
  [22, 60, 57],
  [4, 49, 607],
  [33, 49, 185],
  [30, 64, 76],
  [12, 43, 383],
  [7, 41, 120],
  [16, 67, 742],
  [24, 53, 433],
  [10, 12, 685],
  [6, 46, 780],
  [9, 19, 280],
  [19, 41, 284],
  [35, 41, 668],
  [64, 65, 837],
  [50, 60, 126],
  [3, 7, 119],
  [28, 64, 738],
  [49, 51, 29],
  [12, 28, 120],
  [10, 40, 578],
  [3, 36, 738],
  [8, 9, 92],
  [17, 54, 557],
  [9, 30, 796],
  [1, 59, 61],
  [29, 62, 902],
  [16, 39, 794],
  [7, 44, 433],
  [42, 66, 137],
  [2, 33, 581],
  [11, 39, 876],
  [12, 16, 908],
  [22, 65, 185],
  [11, 62, 75],
  [7, 31, 720],
  [15, 32, 791],
  [21, 38, 477],
  [23, 41, 42],
  [21, 52, 352],
  [25, 57, 330]
]
# print(len(B))
copy = []
for val in B:
    copy.append(val)

def find(parent,q):
    if parent[q] != q:
        parent[q] = find(parent,parent[q])

    return parent[q]


def union(parent,rank,u,v):
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1


B.sort(key=lambda x:x[2])
result = []
i = 0
e = 0
rank = []
parent = []

for node in range(A+1):
    parent.append(node)
    rank.append(0)

# print(B)
while e < A-1:
    print(i,e)
    src,des,wt = B[i]
    i = i + 1
    x = find(parent,src)
    y = find(parent,des)

    if x != y:
        e = e + 1
        result.append([src,des,wt])
        union(parent,rank,src,des)

ans = []
for v in copy:
    if v in result:
        ans.append(1)
    else:
        ans.append(0)

print(ans)
print(rank)
print(result)

import sys


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        dic = {}
        ind = 0
        for val in B:
            dic[tuple(B[ind])] = ind
            ind += 1

        def find(parent, q):
            while parent[q] != q:
                parent[q] = parent[parent[q]]
                q = parent[q]

            return q

        def union(parent, u, v):
            if find(parent, u) == find(parent, v):
                return
            x = find(parent, u)
            y = find(parent, v)
            parent[x] = y

        B.sort(key=lambda x: x[2])
        result = []
        for val in B:
            result.append(0)
        parent = []

        for node in range(A + 1):
            parent.append(node)

        i = 0
        while i < len(B):
            wt = B[i][2]
            j = i
            while j < len(B) and B[j][2] == wt:
                if find(parent, B[j][0]) != find(parent, B[j][1]):
                    result[dic[tuple(B[j])]] = 1
                else:
                    result[dic[tuple(B[j])]] = 0
                j += 1
            j = i
            while j < len(B) and B[j][2] == wt:
                union(parent, B[j][0], B[j][1])
                j += 1

            i = j

        return result






