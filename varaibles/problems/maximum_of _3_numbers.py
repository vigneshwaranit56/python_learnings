a = 10
b = 20
c = 15

# finding the maximum of 3 numbers with operators
if a > b and a > c:
    print("The maximum number is:", a)
elif b>a and b>c:
    print("The maximum number is:", b)
else:
    print("The maximum number is:", c)

# finding the maximum of 3 numbers with built-in function
max_num = max(a, b, c)
print("The maximum number is:", max_num)

