A = 1
rows = A
colms = A
matx = []
row = [["."] * A for i in range(A)]
columns = {}
pos_dig = {}
neg_dig = {}

def place(c):
    if c == A:
        copy = ["".join(x) for x in row ]
        matx.append(copy)
        return

    for i in range(A):
        if i in columns or (i+c in pos_dig) or (i-c in neg_dig):
            continue

        columns.__setitem__(i,1)
        pos_dig.__setitem__(i+c,1)
        neg_dig.__setitem__(i-c,1)
        row[c][i] = "Q"
        place(c+1)
        del pos_dig[i+c]
        del neg_dig[i-c]
        del columns[i]
        row[c][i] = "."

place(0)
print(matx)

