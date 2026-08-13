
num = 121
n = 121

result = 0
while n> 0:
    #  build   
    r = n%10
    #  extract
    result = (result*10)+r
    #  drop
    n = n//10

if result == num:
    print(f"The given number {num} is a palindrome")
else:
    print(f"The given number {num} is not a palindrome")