n = 1234
result = 0
while( n!= 0):
    r = n% 10
    result = (result * 10)+ r
    n = n//10

print("the reverse number is " , result)