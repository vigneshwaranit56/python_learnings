nums1 = [1,2,3,4]
nums = [3,4,5,6]


set1 = set(nums1)
intersections = []
for n in nums:
    if n in set1:
        intersections.append(n)


print(f" for the to list {nums1} and {nums} intersections are {intersections}")