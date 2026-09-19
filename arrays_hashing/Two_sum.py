nums = [3,4,5,6]
target = 8
skim = {}
for i in range(len(nums)):
   j = target - nums[i]
   if j in skim:
      print([skim[j],i])
   skim[nums[i]] = i

