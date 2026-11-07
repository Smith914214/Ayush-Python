    #WAP to find the greatest of 3 number entered by the user

a = int(input("enter first number: "))
b = int(input("enter Sceond number: "))
c = int(input("enter third number: "))

if(a>=b and a>=c):
    print("first number is larger", a)
elif(b>=c):
    print("second number is larger",b)
else:
    print("third number is larger",c)
