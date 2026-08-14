nums = [1, 2, 3, 4, 5]

# 1. Double every number
double_number = [2 * x for x in nums]
print(f"double number {nums} is {double_number}")

# 2. Square every number
square_number = [x * x for x in nums]
print(f"square number {nums} is {square_number}")


# 3. Get only even numbers
even_number = [x for x in nums if x % 2 == 0]
print(f"even number {nums} is {even_number}")


test =  [ x ** 3 for x in nums]

print(f"number power of 2  {nums} is {test}")\

nums = [-3, 5, -7, 2]

postive_numbers = [ abs(x) for  x in nums ]

print(f" negative number {nums}are in convert into postive {postive_numbers}")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_number = [x * x for x in nums if x %2 == 0 ]

print(f" num of {nums} and contions squre of even numberes {even_number}")