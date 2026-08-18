nums = [1, 2, 2, 3, 3, 3]


map = {}

for x in nums:
    if x in map:
        map[x] +=1
    else:
        map[x] = 1

print(f"map {map}")