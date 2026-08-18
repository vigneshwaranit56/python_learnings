nums = [3, 5, 4, 8]
target = 12

map = {}

for x in range(len(nums)):

    map[nums[x]] = x

print(f"map for teh nums and index {map}")


for i  in range(len(nums)):
    if target- nums[i]in map.keys():
        print(f"the pairs are {i} {map.get(target-nums[i])}")


nums.sort()

left = 0
right = len(nums)-1


while left < right:

    sum = nums[left]+nums[right] 
    if sum == target:
        print(f"the pairs are {left} {right} and numbers are {nums[left]} {nums[right]} and sum {sum} ")
        right -= 1
        left += 1

    elif(sum > target):
        right -= 1
    else:
        left += 1

