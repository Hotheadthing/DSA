# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
board = [["a","a"]]
word = "aa"
mword = {}
length = len(word)
count = 0
for i in range(len(word)):
    if word[i] not in mword:
        mword.__setitem__(word[i],1)
    else:
        mword[word[i]] += 1
for j in range(len(board)):
    emap = {}
    for k in range(len(board[j])):
        if board[j][k] not in emap:
            emap.__setitem__(board[j][k], 1)
        else:
            emap[board[j][k]] += 1
    for d in mword:
        if len(mword) == len(emap):
            if (d in emap) and (emap[d] >= 1):
                mword[d] = emap[d] - mword[d]
        elif (d in emap) and (emap[d] >= 1):
            if mword[d] != 0:
                mword[d] -= 1
            emap[d] -= 1

flag = True
for d in mword:
    if mword[d] > 0:
        flag = False
        break
    else:
        flag = True
print(flag)

