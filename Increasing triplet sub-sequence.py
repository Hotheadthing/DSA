nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6]
nums = [20,100,10,12,5,13]
count = 0
flag = False
if len(nums) < 3:
    print(False)
else:
    for x in range(len(nums)-2):
        k = nums[x+2]
        j = nums[x+1]
        i = nums[x]
        if i < j < k:
            flag = True
            break
print(flag)
