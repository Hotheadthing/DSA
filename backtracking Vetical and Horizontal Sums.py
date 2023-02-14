A = 3
B = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
     ]
C = 2
A = 1
B = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
     ]
C = 2
# A = 1
# B = [
#   [-1, -7],
#   [1, -4],
#   [2, 0],
#   [-3, 0],
#   [3, 3],
#   [1, 6]
# ]
# C = 4
# A = 4
# B = [
#   [-7, 8, 5, 8, 6, -2, 3, -1, 0],
#   [1, -7, -5, -7, -2, -10, 8, 1, 10]
# ]
# C = 5
# A = 5
# B = [
#   [-26756, 10502, 58254, 51006, -11763],
#   [-80783, 27204, -69137, 85674, 98526],
#   [89392, 81760, 4097, -95447, 37441],
#   [-69303, -9142, -15049, 5725, -53608],
#   [-33370, -31024, -69442, 61104, -35427],
#   [-40400, -50504, -24182, 97184, 76346],
#   [29647, -51502, -3161, -52211, -72014],
#   [69454, -2948, -43166, -86416, -82483],
#   [-78949, 71674, 39112, 93629, -47763]
# ]
# C = 85667
A = 4
B = [
  [-48170],
  [19513],
  [61107],
  [-12979],
  [13621],
  [64563],
  [-63397],
  [-75761]
]
C = 8117

A = 3
B = [
  [-68927, -67555, -13915, -66467],
  [36227, -69309, -47992, -83281],
  [-5022, 83744, 95911, 95639],
  [-25913, 30347, -48860, -77287]
]
C = 22764

rows = len(B)
colms = len(B[0])

mmap_rows = {}
mmap_colms = {}

def check(r,c,A):
    print(r,c,A)
    sum = 0
    count = 0
    if r not in mmap_rows:
        for i in range(len(B[r])):
            if sum + B[r][i] > C:
                count += 1
                sum -= B[r][i]
            else:
                sum += B[r][i]
        print(f"value of count is {count}")
        mmap_rows.__setitem__(r, count)

        if count > A:
            return 0
        else:
            A -= count
    else:
        count = mmap_rows[r]
        if count > A:
            return 0

    sum1 = 0
    count1  = 0
    if c not in mmap_colms:
        for j in range(len(B)):
            print(f"zzzz {B[j][c]}")
            if sum1 + B[j][c] > C:
                count1 += 1
                print("here")
                sum1 -= B[j][c]
            else:
                sum1 += B[j][c]
        mmap_colms.__setitem__(c,count1)
        if count1 > A:
            return 0
        else:
            A -= count1
    else:
        count1 = mmap_colms[c]
        if count1 > A:
            return 0

    return 1


for i in range(rows):
    for j in range(colms):
        bol = check(i,j,A)
        if bol == 0:
            print(0)
            break


r_count = 0
for r in mmap_rows:
    r_count += mmap_rows[r]

c_count = 0
for c in mmap_colms:
    c_count += mmap_colms[c]

M_count = max(r_count,c_count)
print(mmap_colms)
print(mmap_rows)
rw_len = len(mmap_rows)
col_len = len(mmap_colms)

# print(mmap_colms[1],mmap_rows[1])
rcount = 0
if rw_len >= col_len:
    for i in range(col_len):
        # print(mmap_rows[i],mmap_colms[i])
        # print("Here")
        rcount += max(mmap_rows[i],mmap_colms[i])
    # print(col_len,rw_len)
    for j in range(col_len,rw_len):
        # print("here")
        rcount += mmap_rows[j]
else:
    for i in range(rw_len):
        rcount += max(mmap_rows[i],mmap_colms[i])
        # print("no")
    for j in range(rw_len,col_len):
        # print("No")
        rcount += mmap_colms[j]

print(rcount)
if (len(mmap_colms) == 1) or len(mmap_rows) == 1:
            r_count -= 1
print(rcount)
if rcount > A:
    print(0)
else:
    print(1)







