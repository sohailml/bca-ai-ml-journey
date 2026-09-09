# 🐍 Python Basics — Day 1

> 🚀 Start of my AI/ML Journey  
> 📅 Day 1 — Python Fundamentals

---

## 📌 1. First Program

Python me `print()` function ka use output show karne ke liye hota hai.

```python
print("Hello World")
````

👉 Jo bhi text quotes (`" "` ya `' '`) ke andar hota hai, wahi output me print hota hai.

---

## 📌 2. Variables

Variable ek container hota hai jisme hum data store karte hain.

```python
name = "Sohail"
num = 52
```

### ⚠️ Rules for Variable Names

* Number se start nahi ho sakta ❌ (e.g. `5name`)
* Special symbols allowed nahi ❌ (`#`, `$`, `%`)
* Case-sensitive hote hain
  👉 `name` aur `Name` alag variables hain

---

## 📌 3. Data Types

### 🔹 String (`str`)

Quotes ke andar likha hua data string hota hai

```python
name = "Sohail"
num = "22"
```

---

### 🔹 Integer (`int`)

Whole numbers (without decimal)

```python
num = 4
```

---

### 🔹 Float (`float`)

Decimal numbers

```python
price = 50.22
```

---

### 🔹 Boolean (`bool`)

True ya False values

```python
a = True
print(type(a))  # bool
```

---

### 🔹 None

Empty / no value

```python
a = None
```

---

## ⚠️ Important

* `True`, `False`, `None` → capital letter se start hote hain
* Python case-sensitive language hai

---

## 📌 4. Keywords

Keywords reserved words hote hain (inko variable name nahi bana sakte)

```text
and, or, not, if, else, for, while, break, continue,
True, False, None, def, return, class, try, except
```

---

## 📌 5. Comments

Code me explanation ya notes likhne ke liye use hote hain.

### Single-line comment

```python
# This is a comment
```

### Shortcut

```
Ctrl + /
```

---

## 📌 6. Basic Operation

```python
a = 96
b = 4
print(a + b)
```

👉 Output: `100`
👉 Python BODMAS rule follow karta hai

---

## 📌 7. Operators

### ➕ Arithmetic

```
+, -, *, /, %, **
```

### 🔍 Comparison

```
==, !=, >, <, >=, <=
```

### 📝 Assignment

```
=, +=, -=, *=, /=, %=, **=
```

### 🧠 Logical

```
and, or, not
```

---

## 📌 8. Type Conversion (Automatic)

```python
a, b = 1, 2.0
print(a + b)  # 3.0
```

---

## ❌ Error Example

```python
a, b = 1, "2"
print(a + b)  # TypeError
```

---

## 📌 9. Type Casting (Manual)

```python
a, b = 1, "2"
c = int(b)
print(a + c)  # 3
```

---

## 📌 10. Input in Python

```python
name = input("Enter your name: ")
```

👉 Default input string hota hai

### Convert Input

```python
num = int(input("Enter number: "))
price = float(input("Enter price: "))
```

---

# 🚀 Summary

* `print()` → output show karta hai
* Variables → data store karte hain
* Data Types → str, int, float, bool, None
* Python case-sensitive hai
* Operators → operations perform karte hain
* Type casting → data convert karta hai
* `input()` → user input leta hai

---

# 📈 Progress

* [x] Day 1 Completed ✅
* [ ] Day 2 Coming Soon 🚀

---

# 🔥 #BuildInPublic
