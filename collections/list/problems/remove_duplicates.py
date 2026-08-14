nums = [1,2,2,2,3,3,4]

numbers_count = {}

for i in range(len(nums)):
    if nums[i] in numbers_count:
        numbers_count[nums[i]] +=1
    else:
        numbers_count[nums[i]] = 1


print(f" removed duplicates of {nums} list is {numbers_count.keys()}")