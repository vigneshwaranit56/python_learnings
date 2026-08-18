nums = [1,2,3,3,2,1,4]

seen = {}

for x in nums:

    if x in seen:
        seen[x] +=1
    else:
        seen[x] = 1

print(f" mapping the number counts {seen}")


for i in seen:

    if(seen[i] == 1):
        print(f"first unique character {i}")