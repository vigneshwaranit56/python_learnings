

def prime_checker(n):

    is_prime = True
   
    for j in range(2,n):

        if(n % j ==0 ):
            is_prime = False

    return is_prime

print(f" prime number of 5 is {prime_checker(5)}")