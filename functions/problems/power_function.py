

def power(a,b):

    result = 1;

    for i in range(1,b+1):

        result *=a

    return result

print(f" power of 2 , 5  is {power(2,5)}")