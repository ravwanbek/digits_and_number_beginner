#Find the sum of digits in an integer
def get_sum_digits(num):
    
    
       
    x1=num%10
    num//=10

    x2=num%10
    num//=10

    x3=num%10
    num//=10

    x4=num%10
    num//=10

    x5=num%10
    num//=10

    x6=num%10
    num//=10    
    s=x1+x2+x3+x4+x5

    # return number of digits in integer
    return s

x=get_sum_digits(44)
print(x)

    