name = "swiss"

dict = {}

for char in name:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

for i in dict:
    if dict[i] == 1:
        print(f"First non-repeating character in {name} is {i}")
        break