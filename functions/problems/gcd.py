

def gcd(a,b):

    while(b > 0):

        temp = a % b
        a = b
        b = temp

    return a

print(f" gcd {20} {15} is {gcd(20,15)}")


