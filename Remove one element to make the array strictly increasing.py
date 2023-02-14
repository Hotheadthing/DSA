nums = [2, 3, 1, 2]        #[100, 21, 3]  #[100, 21, 100]
x = nums[0]
length = len(nums)
flag = 1
count = 1

for i in range(1,length):
    if x == nums[i]:
        count += 1


if count == length:
    flag = count
else:
    for i in range(1,length-1):
        if nums[i+1]> nums[i] > x and flag < 2:
            x = nums[i]
        elif nums[i+1]< nums[i] > x or nums[i+1] > nums[i] < x or nums[i+1] == nums[i] == x:
            flag += 1
if flag > 2:
    print("false")
else:
    print("true")
