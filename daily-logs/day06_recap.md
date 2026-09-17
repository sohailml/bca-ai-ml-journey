# 🐍 Python Basics — Day 6

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 6 — Functions & Recursion  

---

## 📌 1. Functions in Python

Function ek block of code hota hai jo ek specific task perform karta hai.

👉 Jab same kaam baar-baar karna ho, to function use karte hain  
👉 Code reusable ho jata hai (bar-bar likhne ki zarurat nahi)

---

### 🔹 Example: Average Function

```python
def avg(a, b, c):
    average = (a + b + c) / 3
    print(average)

avg(2, 5, 5)
```

👉 a, b, c → parameters kehte hain  
👉 2, 5, 5 → arguments kehte hain  
👉 Function call → `avg(2,5,5)`

---

## 📌 2. Return Keyword

Return keyword function ka result wapas deta hai.

```python
def avg(a, b, c):
    return (a + b + c) / 3

result = avg(2, 5, 5)
print(result)
```

👉 return value ko store bhi kar sakte hain

---

## 📌 3. Types of Functions

### 🔹 Built-in Functions

Python me pehle se defined hote hain:

```python
print()
len()
range()
type()
```

### 🔹 User-defined Functions

User khud banata hai:

```python
def greet():
    print("Hello")
```

---

## 📌 4. Default Parameters

Agar function call me argument na diya jaye to default value use hoti hai.

```python
def sum(a=1, b=4):
    print(a + b)

sum()
```

👉 Output: 5

---

## 📌 5. Practice Questions

- WAF to print elements of a list  
- WAF to find factorial of n  
- WAF to print length of a list  
- WAF to convert USD to INR  

👉 In sabhi ke solutions mere GitHub ke **practice folder** me available hain

---

## 📌 6. Factorial using Loops

### 🔹 While Loop

```python
def facto(n):
    fact = 1
    i = 1

    while i <= n:
        fact *= i
        i += 1

    print(fact)

facto(6)
```

### 🔹 For Loop

```python
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print(fact)

factorial(5)
```

---

## 📌 7. Recursion

Recursion ek technique hai jisme function khud ko hi call karta hai.

👉 Jo kaam loop se ho sakta hai, wo recursion se bhi ho sakta hai  
👉 Kabhi-kabhi recursion short aur simple hota hai  

---

### 🔹 Example

```python
def show(n):
    if n == 0:
        return

    print(n)
    show(n - 1)

show(5)
```

👉 Output: 5 se 1 tak print hoga

---

## 📌 8. Base Case (Important ⚠️)

👉 Recursion me base case zaruri hota hai  
👉 Warna infinite loop ho jayega  

```python
if n == 0:
    return
```

---

## 📌 9. Recursion Flow (Understanding)

👉 Pehle n = 5 print hota hai  
👉 Fir show(4), show(3)...  
👉 Jab n = 0 → function stop  

---

### 🔹 Extra Example

```python
def show(n):
    if n == 0:
        return

    print(n)
    show(n - 1)
    print("end")

show(5)
```

👉 "end" 5 baar print hoga

---

## 📌 10. Call Stack

👉 Har function call ek stack layer banata hai  
👉 Jaise n = 5 → 4 → 3 → 2 → 1  
👉 Base case ke baad stack reverse me return hota hai  

---

## 📌 11. Factorial using Recursion

```python
def fact(n):
    if n == 0 or n == 1:
        return 1

    return fact(n - 1) * n

print(fact(4))
```

---

## 📌 12. Recursion Practice Questions

- Sum of first n natural numbers (recursion)  
- Print all elements of a list (recursion)  

### 🔹 List Print using Recursion

```python
def ele(lst, idx=0):
    if idx == len(lst):
        return

    print(lst[idx])
    ele(lst, idx + 1)

ele(["mango", 4, "sohail"])
```

👉 Ye question thoda tricky tha  

👉 Baaki sab solutions GitHub ke **practice repo** me available hain

---

# 🚀 Summary

- Function → reusable code block  
- Parameters & Arguments → input dene ke liye  
- Return → output dene ke liye  
- Recursion → function calling itself  
- Base case → recursion stop karne ke liye  

---

# 📈 Progress

- [x] Day 1 Completed ✅  
- [x] Day 2 Completed ✅  
- [x] Day 3 Completed ✅  
- [x] Day 4 Completed ✅  
- [x] Day 5 Completed ✅  
- [x] Day 6 Completed ✅  
- [ ] Day 7 Coming Soon 🚀  

---

# 🔥 #BuildInPublic
