# oops
# class and object
class Student:
    name = "sohail"

# #creating of object(instance or instance of class)
s1 = Student()
print(s1)
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    colour = "black"
    model = "BMW"

car1 = Car()
print(car1.colour)
print(car1.model)

#constructor
class Student:
    name = "sohail"
    def __init__(self):
        print(self)
        print("adding new students to database...")
s1 = Student()
print(s1)
print(s1.name)

class Student:
    college = "manipal university"   #class attributes
    name = "anonymous"
    def __init__(self,fullname,marks):
        self.name = fullname       #object attributes  
        self.marks = marks
        print("adding new students to database...")
s1 = Student("sohail",98)
print(s1.name, s1.marks)
s2 =Student("golden",100)
print(s2.name,s2.marks)
print(s1.college)

#methods
class Student:
    college = "manipal university"   #class attributes
    def __init__(self,fullname,marks):
        self.name = fullname       #object attributes  
        self.marks = marks
    def welcome(self):
        print("welcome",self.name)
s1 = Student("sohail",98)
print(s1.name, s1.marks)
s1.welcome()
s2 = Student("karan",34)
s2.welcome()

#static method
class Student:
    college = "manipal university"   #class attributes
    def __init__(self,fullname,marks):
        self.name = fullname       #object attributes  
        self.marks = marks
    def welcome(self):
        print("welcome",self.name)
    @staticmethod
    def hell():
        print("hello")

s1 = Student("sohail",98)
print(s1.name)
s1.hell()

#Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.

#Encapsulation
#wrapping data and function in single unit(object)