nums = [-100,-98,-1,2,3,4]
nums = [-1,-2,1,2,3]
count = 0
ans = 1
nums.sort(reverse=True)
print(nums)
for i in range(len(nums)):
    if nums[i] < 0:
        count += 1
if count != 0:
    if count % 2 != 0:
        count = count - 1
for i in range(count):
    nums[-1-i] = abs(nums[-1-i])
print(nums)
nums.sort(reverse=True)
print(nums)
# for i in range(3):
#     ans = ans * nums[i]
#
# print(ans)