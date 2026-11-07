## WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val,"INR")
    
converter(55)

### WAF 

def check_even_odd(num):
    """Check whether a number is even or odd"""
    if num %2==0:
        print(num, "is Even")
    else:
        print(num,"is odd")
number = int(input("Enter a number: "))
check_even_odd(number)