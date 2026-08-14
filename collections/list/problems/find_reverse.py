nums = [1,2,3,4,5]

print(f" rverse by operators of ::-1 {nums[::-1]}")

reverse_nums = []

for i in range(1,len(nums)+1):
    reverse_nums.append(nums[-i])

print(f"reverse nums list {nums} is {reverse_nums}")