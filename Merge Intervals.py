# intervals = [[1,3],[6,9]]
# newInterval = [2,6]
# intervals = [[3,5],[8,10]]
# newInterval = [1,12]
# intervals = [[3,5], [4,9]]
# newInterval = [2,6]
# intervals = [[3,6], [8,10]]
# newInterval = [1,2]
intervals = [ (242769, 298578), (1485821, 3549159), (3601003, 3781492), (3918406, 4233355), (4859263, 6371214), (6524141, 6876393), (11134739, 12804010), (13308849, 14330671), (14577529, 15007662), (15458500, 16738297), (18468996, 23667578), (25476991, 25797327), (26147944, 28198553), (28272397, 29024013), (29403740, 30131864), (31627582, 32418203), (33266069, 33752547), (34495644, 34871446), (35550469, 36108659), (36926556, 37261232), (38583039, 39006804), (39509631, 41893216), (42374004, 42931714), (44269968, 44369083), (45143617, 45563132), (47682511, 51195515), (51927143, 54183020), (58277563, 58496820), (59191747, 62019729), (63220700, 64115749), (64510556, 65776930), (66171734, 67878747), (70757042, 76924935), (77187481, 77197369), (77698059, 77933160), (78173032, 78658045), (80964341, 85215059), (85715400, 87324172), (88079827, 90407584), (90761708, 91759576), (93179322, 94449428), (95477202, 95486054), (96068708, 98287029) ]
newInterval = (104389575, 78104302)
res = []
N = len(intervals)
for i in range(N):

    if newInterval.start > intervals[i].end:
        res.append(intervals[i])

    elif intervals[i].start > newInterval.end:
        res.append(newInterval)
        k = i
        while k < N:
            res.append(intervals[k])
            k += 1
        return res

    else:
        newInterval.start = min(newInterval.start, intervals[i].start)
        newInterval.end = max(newInterval.end, intervals[i].end)

res.append(newInterval)
return (res)





















# arr = []
# # newInterval.sort()
# flag = 0
# for i in range(len(intervals)):
#     if newInterval[0] > intervals[i][1]:
#         arr.append(intervals[i])
#     elif newInterval[1] < intervals[i][0]:
#         if newInterval not in arr:
#             arr.append(newInterval)
#         #if intervals[i] not in arr:
#         arr.append(intervals[i])
#         newInterval = intervals[i]
#         flag = 1
#     else:
#         if newInterval[0] > intervals[i][0]:
#             newInterval[0] = intervals[i][0]
#             newInterval[1] = max(newInterval[1],intervals[i][1])
#             arr.append(newInterval)
#         else:
#             newInterval[1] = max(newInterval[1],intervals[i][1])
#             if len(arr) == 0:
#                 arr.append(newInterval)
#         flag = 1
# print(flag)
# if flag == 0:
#     arr.append(newInterval)
#     # arr.sort()
#     print(arr)
# else:
#     print(arr)