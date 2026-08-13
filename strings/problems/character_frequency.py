fruit = "banana"

dict = {}

for char in fruit:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1  


print(f"Character frequency in {fruit} is {dict}")