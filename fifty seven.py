####  Del keywords

class Student:
    def __init__(self, name):
        self.name = name
        
s1= Student("shradha")
print(s1.nmae)
del s1.name
print(s1.name)

### public Attributes

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
        
acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.acc_pass)

### Private Attributes

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.__acc_pass)