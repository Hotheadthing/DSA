nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
# nums = [1,1,1,1,1]
# nums = [0]
# nums = [3,2,1]
# nums = [2,0,2,0,1]
# nums = [3,1,1,1,1]
# nums = [4,1,1,3,1,1,1]
# nums = [1,2,3]
ans = []
arr = 0
for i in range(len(nums) - 1):
            count = 0
            while i < len(nums) - 1:
                i = nums[i] + i
                count += 1
                if i < len(nums) - 1 and nums[i] == 0:
                    count = 0
                    break

            ans.append(count)
print(ans)
















# w = 9999999
# for i in range(1, len(ans)):
#     if ans[i] != 0:
#         w = min(w,ans[i])
#         break
# print(ans[0],ans[w])
# if len(nums) == 1:
#      print(0)
# elif nums[0] >= len(nums) - 1:
#     print(1)
# elif ans[0] != 0 and ans[0] < ans[w]:
#     print(ans[0])
# else:
#     if nums[0] >= ans[w]:
#         print(ans[w] + 1)
#     nums = nums[:ans.index(ans[w])]
#     if len(nums) == 1:
#         print(ans[w] + 1)
#     else:
#         for i in range(len(nums) - 1):
#             count = 0
#             while i < len(nums) - 1:
#                 i = nums[i] + i
#                 count += 1
#                 if i < len(nums) - 1 and nums[i] == 0:
#                     count = 0
#                     break
#
#             ans[w] += count
#
#         print(ans[w])