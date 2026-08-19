def greet():
    print("hello world")

greet()


def add(a,b):
    return a+b

print(f"addition of two number {4} , {5} is {add(4,5)}")


def greet(name,message="hello"):

    print(f" {message} {name}!!")

greet("vignesh")

greet("vignesh","Good Morning")


def add_numbers(*numbers):
    total = 0

    for x in numbers:
        total += x

    return total

num = [1,2,3,4,5,5,56]

print(f" total number  of {num} is {add_numbers(*num)}")



def show_user(**details):
    print(details)

show_user(name="Vignesh", age=30, city="Chennai")

square = lambda x: x * x

print(f"square of the number {square(5)}")