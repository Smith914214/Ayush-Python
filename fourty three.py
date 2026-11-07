## WAF to find the factorial of N.(N is the parameter)

n = 6

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
cal_fact(6)