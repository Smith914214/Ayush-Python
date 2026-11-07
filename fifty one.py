class Student:
    name = "Ayush"
    
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


class Car:
    color = "blue"
    brand = "mercedes"
    
car1 = Car()
print(car1.color)
print(car1.brand)

# use Constructer

class Student:
    def __init__(self):
        print(self)
        print("adding new student in database..")
s1 = Student()
print(s1)

####

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")
s1 = Student("Rohit",99)
print(s1.name,s1.marks)

s2 = Student("Rajesh",75)
print(s2.name,s2.marks)