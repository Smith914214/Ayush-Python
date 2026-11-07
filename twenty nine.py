## Print the element of the following list using a loop:
# [1,4,9,16,25.36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
    
## Search for a numberr x in this tuple using loop
# (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index",i)
    i += 1
