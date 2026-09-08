# 🐍 Python Basics — Day 12

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 12 — OOP (Object Oriented Programming)

---

## 📌 1. `del` Keyword

`del` ka use object ya uske attribute ko delete karne ke liye hota hai.

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("sohail")
print(s1.name)

del s1.name
print(s1.name)  # ❌ Error (attribute delete ho chuka hai)
```

👉 `del` ke baad wo value exist nahi karti

---

## 📌 2. Private Attributes

Private attributes banane ke liye `__` (double underscore) use karte hain.

```python
class Account:
    def __init__(self, acc_no, acc_pswd):
        self.acc_no = acc_no
        self.__acc_pswd = acc_pswd

    def reset_pswd(self):
        print(self.__acc_pswd)

s1 = Account(71008100005928, "sohail123")
s1.reset_pswd()
```

---

## 📌 3. Inheritance

### 🔹 Single Level Inheritance

```python
class Car:
    colour = "black"

    @staticmethod
    def start():
        print("started")

    @staticmethod
    def stop():
        print("stop")


class BMW(Car):
    def __init__(self, name):
        self.name = name


car1 = BMW("m5")
print(car1.name)
car1.stop()
print(car1.colour)
```

---

### 🔹 Multi-Level Inheritance

```python
class Car:
    @staticmethod
    def start():
        print("started")

    @staticmethod
    def stop():
        print("stop")


class BMW(Car):
    def __init__(self, brand):
        self.brand = brand


class Model(BMW):
    def __init__(self, type):
        self.type = type


car1 = Model("suv")
car1.start()
print(car1.type)
```

---

### 🔹 Multiple Inheritance

```python
class A:
    varA = "welcome to class A"


class B:
    varB = "welcome to class B"


class C(A, B):
    varC = "welcome to C"


s1 = C()
print(s1.varA)
print(s1.varB)
print(s1.varC)
```

---

## 📌 4. `super()` Method

Parent class ke constructor ko call karne ke liye use hota hai.

```python
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("started")


class BMW(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name


car1 = BMW("m5", "ev")
print(car1.name)
print(car1.type)
car1.start()
```

---

## 📌 5. Class Method

Class variable ko modify karne ke liye use hota hai.

```python
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("sohail")

print(p1.name)
print(Person.name)
```

---

## 📌 6. Property Decorator

Dynamic value update karne ke liye use hota hai.

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


s1 = Student(98, 97, 96)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)
```

👉 Value change hone par percentage automatically update hota hai

---

## 📌 7. Polymorphism

Same operation different ways me perform hota hai.

```python
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        return Complex(self.real + num2.real, self.img + num2.img)

    def __sub__(self, num2):
        return Complex(self.real - num2.real, self.img - num2.img)


num1 = Complex(1, 3)
num2 = Complex(4, 6)

num3 = num1 + num2
num3.showNumber()

num4 = num2 - num1
num4.showNumber()
```

---

# 🚀 Summary

* `del` → delete object/attribute  
* Private → `__` se secure data  
* Inheritance → code reuse  
* `super()` → parent constructor call  
* Class Method → class data modify  
* Property → dynamic calculation  
* Polymorphism → same operation, different behavior  

---

# 📈 Progress

* [x] Day 1 Completed ✅  
* [x] Day 2 Completed ✅  
* [x] Day 3 Completed ✅  
* [x] Day 4 Completed ✅  
* [x] Day 5 Completed ✅  
* [x] Day 6 Completed ✅  
* [x] Day 7 Completed ✅  
* [x] Day 8 Completed ✅  
* [x] Day 9 Completed ✅  
* [x] Day 10 Completed ✅  
* [x] Day 11 Completed ✅  
* [x] Day 12 Completed ✅  
* [ ] Day 13 Coming Soon 🚀  

---

# 🔥 #BuildInPublic
