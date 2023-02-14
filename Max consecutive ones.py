nums = [1,1,0,1,1,1]
ref = 0
compar = 0

for i in range(len(nums)):
    if nums[i] == 1:
        ref += 1
    else:
        compar = max(compar,ref)
        ref = 0
compar = max(ref,compar)
print(compar)