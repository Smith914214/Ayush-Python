# printthe element of the following list using a loop:
 # [1,4,9,16,25,36,49,64,81,100]
 
nums = [1,4,9,16,25,36,49,64,81,100]
for el in nums:
     print(el)
     
     
# Search for a number X in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
x = 64

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1