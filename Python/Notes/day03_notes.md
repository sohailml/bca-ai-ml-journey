# 🐍 Python Basics — Day 3

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 3 — Lists & Tuples

---

## 📌 1. Lists in Python

List ek collection hoti hai jisme hum multiple values ek jagah store kar sakte hain.

```python
my_list = [1, 3, "sohail", 5]
```

👉 Jab bahut saara data hota hai, to list use karke sab ek jagah manage karte hain.

---

## 📌 2. Properties of List

* List **mutable** hoti hai → change kar sakte hain ✅  
* Square brackets `[]` me likhte hain  
* Different data types store kar sakte hain  

---

## 📌 3. Length of List

```python
my_list = [1, 3, "sohail", 5]
print(len(my_list))
```

👉 Output: `4`  
👉 Total elements count karta hai  

---

## 📌 4. Indexing & Slicing

```python
my_list = [10, 20, 30, 40]

print(my_list[0])    # 10
print(my_list[1:3])  # [20, 30]
```

👉 Indexing 0 se start hoti hai  
👉 Slicing me last index include nahi hota  

---

## 📌 5. List Methods

### ➕ append()

```python
my_list.append(100)
```

👉 List ke end me value add karta hai  

---

### 🔽 sort()

```python
my_list.sort()
```

👉 List ko ascending order me sort karta hai  

---

### 🔼 sort(reverse=True)

```python
my_list.sort(reverse=True)
```

👉 List ko descending order me sort karta hai  

---

### 📍 insert()

```python
my_list.insert(1, 50)
```

👉 Specific index par value add karta hai  

---

### 🔄 reverse()

```python
my_list.reverse()
```

👉 List ko ulta kar deta hai  

---

### ❌ pop()

```python
my_list.pop(2)
```

👉 Index ke basis par element delete karta hai  

---

### 🚫 remove()

```python
my_list.remove(3)
```

👉 Value ke basis par delete karta hai (first occurrence)  

---

### 📋 copy()

```python
new_list = my_list.copy()
```

👉 List ki copy bana deta hai  

---

## 📌 6. Tuples in Python

Tuple bhi list jaisa hota hai, lekin ek important difference hai.

```python
tup = (1, 2, 3, "sohail")
```

👉 Tuple **immutable** hota hai → change nahi kar sakte ❌  

---

## 📌 7. Properties of Tuple

* Parentheses `()` me likhte hain  
* Immutable hota hai  
* Fast aur safe hota hai  

---

## 📌 8. Indexing & Slicing in Tuple

```python
tup = (10, 20, 30, 40)

print(tup[1])    # 20
print(tup[1:3])  # (20, 30)
```

---

## 📌 9. Tuple Methods

### 🔍 index()

```python
tup = (1, 2, 3, 2)

print(tup.index(2))
```

👉 Output: `1` (first occurrence)

---

### 🔢 count()

```python
tup = (1, 2, 3, 2)

print(tup.count(2))
```

👉 Output: `2` (kitni baar value aayi)

---

# 🚀 Summary

* List → mutable hoti hai  
* Tuple → immutable hoti hai  
* List me zyada operations possible hain  
* Tuple safe aur fast hota hai  

---

# 📈 Progress

* [x] Day 1 Completed ✅  
* [x] Day 2 Completed ✅  
* [x] Day 3 Completed ✅  
* [ ] Day 4 Coming Soon 🚀  

---

# 🔥 #BuildInPublic
