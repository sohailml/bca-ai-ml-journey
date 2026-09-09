# 🐍 Python Basics — Day 11

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 11 — OOP (Object Oriented Programming)

---

## 📌 1. Class & Object

Aaj maine OOP ka basic concept padha — **Class aur Object**

👉 Class ek blueprint hota hai  
👉 Object us class ka instance hota hai  

---

### 🔹 Example

```python
class Student:
    name = "sohail"

s1 = Student()
print(s1)
print(s1.name)

s2 = Student()
print(s2.name)
```

👉 `Student` → class hai  
👉 `s1`, `s2` → objects hain  
👉 Sab objects same class ke attributes use kar sakte hain  

---

### 🔹 Another Example

```python
class Car:
    colour = "black"
    model = "BMW"

car1 = Car()
print(car1.colour)
print(car1.model)
```

👉 Class ke andar jo variables hote hain unhe attributes kehte hain  

---

## 📌 2. Constructor (`__init__`)

Constructor automatically run hota hai jab object create hota hai  

```python
class Student:
    name = "sohail"

    def __init__(self):
        print(self)
        print("adding new students to database...")

s1 = Student()
print(s1)
print(s1.name)
```

👉 `__init__()` ek special function hai  
👉 Object create hote hi automatically call hota hai  

---

## 📌 3. Class Attributes vs Object Attributes

```python
class Student:
    college = "manipal university"   # class attribute
    name = "anonymous"

    def __init__(self, fullname, marks):
        self.name = fullname        # object attribute
        self.marks = marks
        print("adding new students to database...")

s1 = Student("sohail", 98)
print(s1.name, s1.marks)

s2 = Student("golden", 100)
print(s2.name, s2.marks)

print(s1.college)
```

👉 Class attribute → sab objects ke liye same  
👉 Object attribute → har object ke liye alag  

---

## 📌 4. Methods

Method ek function hota hai jo class ke andar likha jata hai  

```python
class Student:
    college = "manipal university"

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("welcome", self.name)

s1 = Student("sohail", 98)
print(s1.name, s1.marks)
s1.welcome()

s2 = Student("karan", 34)
s2.welcome()
```

👉 Method ke andar `self` use hota hai  
👉 `self` current object ko represent karta hai  

---

## 📌 5. Static Method

Static method class se related hota hai, object se nahi  

```python
class Student:
    college = "manipal university"

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("welcome", self.name)

    @staticmethod
    def hell():
        print("hello")

s1 = Student("sohail", 98)
print(s1.name)
s1.hell()
```

👉 `@staticmethod` me `self` nahi hota  
👉 Ye directly class se related hota hai  

---

## 📌 6. Abstraction

👉 Implementation details ko hide karna  
👉 Sirf important cheeze user ko dikhana  

---

## 📌 7. Encapsulation

👉 Data + functions ko ek unit (object) me pack karna  

---

# 🚀 Summary

- Class → blueprint  
- Object → class ka instance  
- Constructor → object create hote hi run hota hai  
- Class vs Object attributes → shared vs unique  
- Methods → class ke functions  
- Static method → object-independent  
- Abstraction → hide details  
- Encapsulation → wrap data + functions  

---

# 📈 Progress

- [x] Day 1 Completed ✅  
- [x] Day 2 Completed ✅  
- [x] Day 3 Completed ✅  
- [x] Day 4 Completed ✅  
- [x] Day 5 Completed ✅  
- [x] Day 6 Completed ✅  
- [x] Day 7 Completed ✅
- [x] Day 8 Completed ✅
- [x] Day 9 Completed ✅  
- [x] Day 10 Completed ✅  
- [x] Day 11 Completed ✅  
- [ ] Day 12 Coming Soon 🚀  

---

# 🔥 #BuildInPublic
