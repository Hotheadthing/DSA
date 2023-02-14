import functools
A = [3, 30, 34, 5, 9]
A = [2,3,9,0]
# A = [12,121]
A = [ 9, 99, 999, 9999, 9998 ]
#A = [ 412, 823, 580, 12, 220, 746, 541, 207, 603, 961, 743, 517, 747, 891, 550, 21, 991, 683, 19, 497, 584, 910, 984, 831, 335, 485, 203, 503, 448, 141, 350, 604, 380, 794, 770, 802, 747, 355, 888, 878, 219, 233, 60, 584, 648, 599, 100, 6, 423, 681, 188, 41, 413, 965, 204, 443, 896, 991, 698, 557, 813, 359, 972, 230, 497, 157, 644, 822, 16, 423 ]

def comparator(s1,s2):
    if int(s1+s2) < int(s2+s1):
        return -1
    elif int(s2+s1) > int(s1+s2):
        return 1
    else:
        return 0


nums = []
for i in range(len(A)):
    nums.append(str(A[i]))

nums = sorted(nums, key = functools.cmp_to_key(comparator),  reverse = True)
if nums[0] == '0':
    ans = "0"
else:
    ans = ''.join(nums)
print(ans)
