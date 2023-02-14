nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [-2,0,-1,6]
# nums = [1,0,-1,2,3,-5,-2]
# nums = [-1,0,-2,2]
nums = [0,2]
# nums = [2,-5,-2,-4,3]
# nums = [3,-1,4]
nums1 = []
for j in range(len(nums)):
    nums1.append(nums[j])

print(nums1)
maximum = 0
for i in range(len(nums1)):
    maximum = max(maximum,nums1[i])
    for j in range(i+1,len(nums1)):
        nums1[i] = nums1[i]*nums1[j]
        maximum = max(maximum,nums1[i])

print(maximum)
