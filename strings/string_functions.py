name ="vignesh "

#split() function is used to split the string into list 
# of words based on the separator provided, 
# by default it will split based on space
print(name.split()) # it will split the string into list of words based on space

#strip() function is used to remove the leading and 
# trailing spaces from the string
stripped_name = name.strip()
print(len(stripped_name))

# replace() function is used to replace a substring with
#  another substring in the string
print(name.replace("vignesh", "Vignesh"))

# join() function is used to join the elements of a list or
# tuple into a single string using a specified separator
print("-".join(["vignesh", "is", "a", "good", "boy"]))

#upper() function is used to convert all the characters in 
# the string to uppercase
name = name.upper()
print(name) # it will convert all the characters in the string to uppercase
# lower() function is used to convert all the characters 
# in
print(name.lower()) # it will convert all the characters in the string to lowercase


# len() function is used to get the length of the string,
# which is the number of characters in the string
print(len(name)) # it will return the length of the string