nums = [3,10,5,25,2,8]
# nums = [14,70,53,83,49,91,36,80,92,51,66,70]
result = 0
zero = []
one = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        zero.append(nums[i])
    else:
        one.append(nums[i])
m_one = max(one)
m_zero = max(zero)
result1 = 0
for i in range(len(nums)):
    result = max(result,(nums[i]^m_one))

for i in range(len(nums)):
    result1 = max(result1,(nums[i]^m_zero))

print(max(result,result1))
print(1^0)