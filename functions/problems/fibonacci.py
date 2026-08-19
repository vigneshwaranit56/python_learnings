def fibonacci(n):

    a = 0
    b = 1
    finonacci = []
    for i in range(0,n+1):
        finonacci.append(a)
        temp = a
        a = b
        b = temp+b
    return finonacci


print(f" number 5 series of{fibonacci(5)}")


def fibonacci_r(n):

    if(n == 0):
        return 0
    if(n ==1):
        return 1

    return fibonacci_r(n-1)+fibonacci_r(n-2)

print(f" fibonacci recurssion of is {fibonacci_r(5)}")

