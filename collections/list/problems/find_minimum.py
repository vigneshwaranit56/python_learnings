import sys
nums = [4,8,2,6,1,9]

min = sys.maxsize
for i in range(len(nums)):
    if(nums[i] < min):
        min = nums[i]

print(f" find minimum of given list  {nums} is: {min}")