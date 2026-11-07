## Create a new file "practice.txt" using python. Add the following data in it:
#  Hi everyone
#  we are learning File I/O
#  using Java
#  I like proramming in Java

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O")
    f.write("using Java.\nI like proramming in Java")
    
    
## WAF that replace all occurrences of "java" with "python" in above file

with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
    
### Search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not Found")

## WAF to find in which line of the file does the word "learning" occur first. print -1 if word not found
def check_for_line():
    word = "proramming"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()