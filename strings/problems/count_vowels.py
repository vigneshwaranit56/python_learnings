name = "hello"
count = 0
for char in range(len(name)):
    if name[char] in "aeiouAEIOU": # in check is used to check if the character is present in the string of vowels
        count += 1

print(f"Total vowels in {name} is {count}")