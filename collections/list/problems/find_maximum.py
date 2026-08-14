nums = [4,8,2,6,1,9]

max = 0
for i in range(len(nums)):
    if(nums[i] > max):
        max = nums[i]

print(f" find maximum of given list  {nums} is: {max}")