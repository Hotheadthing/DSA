# A = ["hello", "scaler", "interviewbit"]
# B = "adhbcfegskjlponmirqtxwuvzy"

# A = ["fine", "none", "no", "man", "mango"]
# B = "qwertyuiopasdfghjklzxcvbnm"


A = [ "lzummwrhylyjl" ]
B = "htbskjnygxmuqwiavdzfocelpr"

dic_map = {}
for d in range(len(B)):
    if B[d] not in dic_map:
        dic_map.__setitem__(B[d], d)

print(dic_map)

if len(A) == 1:
    print(1)
else:
    same = []
    flag = -1
    for i in range(len(A) - 1):
        if dic_map[A[i][0]] < dic_map[A[i + 1][0]]:
            flag = 1
        elif dic_map[A[i][0]] > dic_map[A[i + 1][0]]:
            flag = 2
            break
        else:
            same.append(A[i])
            same.append(A[i + 1])

    if flag == 1 and same == []:
        print(1)
    elif flag == 2:
        print(0)

    print(same)

    if flag == 1 and same != []:
        for i in range(0, len(same) - 1, +2):
            test_flag = -1
            # print(min(len(same[i]),len(same[i+1])))
            l = 0
            while l < (min(len(same[i]), len(same[i + 1])) - 1):
                l = l + 1
                if same[i][l] == same[i + 1][l]:
                    test_flag = test_flag
                elif same[i][l] > same[i + 1][l]:
                    test_flag = 2
                    break
                else:
                    test_flag = 1
                    break
            if test_flag == -1 and len(same[i]) > len(same[i + 1]):
                test_flag = 2
                break
            else:
                test_flag = 1

        if test_flag == 2:
            print(0)
        else:
            print(1)





