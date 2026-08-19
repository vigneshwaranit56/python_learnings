def factorial(number):
    result = 1
    for i in range(1,number+1):
        result *=i

    return result

print(f" factorial number of {5} is {factorial(5)} ")