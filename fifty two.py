class Student:
    college_name = "ABC College"
    name = "anonymous"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("Rohit",99)
print(s1.name)

######

class Student:
    college_name = "ABC College"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student",self.name)
        
        def get_marks(self):
            return self.marks
        
s1 = Student("Rohit",99)
s1.welcome()
print(s1.get_marks())


class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    # Move this out to the same level as 'welcome'
    def get_marks(self):
        return self.marks

s1 = Student("Rohit", 99)
s1.welcome()
print(s1.get_marks())