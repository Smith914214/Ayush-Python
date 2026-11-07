## WAF to print the length of a list.(list is the parameter)

cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["Hanuman","Ram","Shankar","Shaktiman"]

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)


## WAF to print the element of a list in a single line.(list is the parameter)

cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["Hanuman","Ram","Shankar","Shaktiman"]

def print_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item, end=" ")
        

print_list(heroes)
print_list(cities)
print()