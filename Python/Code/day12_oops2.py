#del keyword
class student:
    def __init__(self,name):
        self.name = name

s1 = student("sohail")
print(s1.name)
del s1.name
print(s1.name) #give error because del deleted s1.name


#private class and attribute
class account:
    def __init__(self,acc_no,acc_pswd):
        self.acc_no = acc_no
        self.__acc_pswd = acc_pswd # __ to make private

    def reset_pswd(self):
        print(self.__acc_pswd)

s1 = account(71008100005928,"sohail123")
print(s1.reset_pswd())

#inhheritance -single level inheritance
class car:
    colour = "black"
    @staticmethod
    def start():
        print("started")
    @staticmethod
    def stop():
        print("stop")

class bmw(car):
    def __init__(self,name):
        self.name = name

car1 = bmw("m5")
print(car1.name)
print(car1.stop())
print(car1.colour)

#multi level inheritance
class car:
    @staticmethod
    def start():
        print("started")
    @staticmethod
    def stop():
        print("stop")

class bmw(car):
    def __init__(self,brand):
        self.brand = brand

class model(bmw):
    def __init__(self, type):
        self.type = type

car1 = model("suv")
car1.start()
print(car1.type)
car.stop()


#multiple inheritance
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to C"

s1 = C()
print(s1.varA)
print(s1.varB)
print(s1.varC)


#super method
class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("started")
    @staticmethod
    def stop():
        print("stop")

class bmw(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name

car1 = bmw("m5","ev")
print(car1.name)
print(car1.type)
car1.start()

# class method
class person:
    name = "anonymous"
    # def change(self,name):
    #     self.name= name

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = person()
p1.changeName("sohail")
print(p1.name)
print(person.name)

#property decorators
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy+self.chem+self.math)/3) +"%"
s1 = student(98,97,96)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage)  #will show above percentage,
#we use property decorator so when will cahnge marks perecentage also change
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) +"%"
        
s1 = student(98,97,96)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage)


#polymorphism
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)
num1 = complex(1,3)
num1.showNumber()

num2 = complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

#if we do directly num3 = num1 + num2 so we will get error even if we write num3.showNumber()
#we use dunder function
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):  #for addition
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)

    def __sub__(self,num2):  #for subtraction
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal,newImg)
num1 = complex(1,3)
num1.showNumber()

num2 = complex(4,6)
num2.showNumber()

num3 = num1+num2
num3.showNumber()

num4 = num2-num1
num4.showNumber()