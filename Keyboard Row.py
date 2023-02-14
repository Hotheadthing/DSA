words = ["Hello","Alaska","Dad","Peace"]
words = ["omk"]
words = ["adsdf","sfd"]
ans = []
f_row = "qwertyuiop"
s_row = "asdfghjkl"
t_row = "zxcvbnm"

for i in range(len(words)):
    flag = True
    y = words[i][0].lower()
    if y in s_row:
        for j in range(1,len(words[i])):
            if words[i][j] not in s_row:
                flag = False
                break
            if j == len(words[i]) - 1 and flag == True:
                ans.append(words[i])
    elif y in f_row:
        for j in range(1,len(words[i])):
            if words[i][j] not in f_row:
                flag = False
                break
            if j == len(words[i]) - 1 and flag == True:
                ans.append(words[i])
    elif y in t_row:
        for j in range(1,len(words[i])):
            if words[i][j] not in t_row:
                flag = False
                break
            if j == len(words[i]) - 1 and flag == True:
                ans.append(words[i])
print(ans)

