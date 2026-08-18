nums = [1,1,1,2,2,2,3,3,3]

seen = set()

for  x  in nums:
    if x in seen:
        print(f" the number {x} is duplicate ")

    seen.add(x)
