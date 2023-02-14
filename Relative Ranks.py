score = [5,4,3,2,1]
score = [10,3,8,9,4]
ref_arr = []
for i in range(len(score)):
    ref_arr.append(score[i])
ref_arr.sort(reverse=True)

nMap = {}

for i in range(len(ref_arr)):
    nMap.__setitem__(ref_arr[i],i+1)

ans = []
for i in range(len(score)):
    if nMap[score[i]] == 1:
        ans.append("Gold Medal")
    elif nMap[score[i]] == 2:
        ans.append("Silver Medal")
    elif nMap[score[i]] == 3:
        ans.append("Bronze Medal")
    else:
        ans.append(str(nMap[score[i]]))
print(ans)