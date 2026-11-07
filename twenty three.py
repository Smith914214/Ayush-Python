## WAP to enter masrks of 3 subject from the user and store them in a dictionary. start with an empty dictionary & add one by one. use subject name as key & marks as value

marks = {}

x = int(input("enter phy :"))
marks.update({"phy" : x})

x = int(input("enter math :"))
marks.update({"math" : x})

x = int(input("enter chem :"))
marks.update({"chem" : x})

print(marks)