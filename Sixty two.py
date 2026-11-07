### Define a circle class to create a circle with radius r using the constructer
### DEfine an Area() method of the class which calculate the area of the circle.
### Define a parimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7)*self.radius**2
    
    def perimeter(self):
        return 2*(22/7)*self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

### Define a Employee class with attributes role, department & salary.This class also showDetail() method
### create an engineer class that inherits properties from employee & 

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        super().__init__("Engineer","IT","750000")
        
engg1 = Engineer("Jack maa","60")
engg1.showDetails()