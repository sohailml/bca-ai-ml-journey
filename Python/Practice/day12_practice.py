"""Q1: Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle"""
# class Circle:
#     def __init__(self,r):
#         self.r = r

#     def area(self):
#         print("The area of circle is",(22/7)*self.r*self.r,"cm²")
#     def perimeter(self):
#         print("The perimeter of circle is",2*(22/7)*self.r,"cm")

# circle1 =Circle(7)
# circle1.area()
# circle1.perimeter()


"""Q2: Define an Employee class with attributes role, department & salary.
This class should also have a showDetails() method.Create an Engineer class 
that inherits properties from Employee & has additional attributes: name & age."""
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("role =",self.role)
#         print("department =",self.department)
#         print("salary =",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("engineer","it","56,000")

# emp1 = Employee("hr","it","46,600")
# emp1.showDetails()

# eng1 = Engineer("sohail",18)
# eng1.showDetails()


"""Q3: Create a class called Order which stores item & its price.
Use Dunder function __gt__() to convey that: order1 > order2 if price of order1 > price of order2"""
