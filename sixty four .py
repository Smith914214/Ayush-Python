### MINI PROJECT RANDOM PASSWORD GENERATOR

import random
import string

#pass_len = 15
length = int(input("Enter the password length: "))
characters = string.ascii_letters + string.digits + string.punctuation

#list comprehension[function for i in range(n)]

#res = "".join([random.choice(charValues) for i in range(pass_len)])
#print(res)

password = ""
for i in range(length):
    password += random.choice(characters)

print("Your Random password is:", password)