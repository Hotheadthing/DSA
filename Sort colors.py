nums = [2,0,2,1,1,0]
zero = 0
one = 0
two = 0
output = []
for i in range(len(nums)):
    if nums[i] == 0:
        zero += 1
    elif nums[i] == 1:
        one += 1
    else:
        two += 1

for j in range(zero):
    nums[j] = 0
for k in range(zero,zero+one):
    nums[k] = 1
for l in range(zero+one,len(nums)):
    nums[l] = 2
print(nums)
