# 🐍 Python Basics — Day 4

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 4 — Dictionary & Set

---

## 📌 1. Dictionary in Python

Dictionary ek data structure hai jisme data **key : value pair** me store hota hai.

```python
my_dict = {
    "name": "sohail",
    "age": 18,
    "marks": 90
}
```

👉 Har key unique hoti hai  
👉 Value repeat ho sakti hai  

---

## 📌 2. Properties of Dictionary

* Dictionary **mutable** hoti hai → change kar sakte hain ✅  
* Curly braces `{}` me likhte hain  
* Key : Value format me data store hota hai  
* Unordered hoti hai  
* Har type ka data store kar sakte hain (int, float, string, list, tuple, dict)

---

## 📌 3. Nested Dictionary

Dictionary ke andar dictionary ho sakti hai

```python
student = {
    "name": "sohail",
    "marks": {
        "math": 90,
        "science": 85
    }
}
```

👉 Isko nested dictionary bolte hain  

---

## 📌 4. Dictionary Methods

### 🔑 keys()

```python
print(my_dict.keys())
```

👉 Saari keys return karta hai  

---

### 📦 values()

```python
print(my_dict.values())
```

👉 Saari values return karta hai  

---

### 🔄 update()

```python
my_dict.update({"city": "Delhi"})
```

👉 New key-value add karta hai ya update karta hai  

---

### 📋 items()

```python
print(my_dict.items())
```

👉 Key-value pairs ko tuple form me return karta hai  

---

### 🔍 get()

```python
print(my_dict.get("name"))
```

👉 Key ke through value return karta hai  

---

## 📌 5. Set in Python

Set bhi ek collection hota hai, lekin isme **duplicate values allowed nahi hoti**

```python
my_set = {1, 2, 3, 3, 4}
```

👉 Output: `{1, 2, 3, 4}`  

---

## 📌 6. Properties of Set

* Curly braces `{}` me likhte hain  
* Set **mutable** hota hai (but elements immutable hote hain)  
* Unordered hota hai  
* Duplicate values automatically remove ho jati hain  
* List aur dictionary store nahi kar sakte (kyunki wo mutable hote hain)

---

## 📌 7. Set Methods

### ➕ add()

```python
my_set.add(5)
```

👉 Set me element add karta hai  

---

### ❌ remove()

```python
my_set.remove(2)
```

👉 Specific value remove karta hai  

---

### 🧹 clear()

```python
my_set.clear()
```

👉 Pure set ko empty kar deta hai  

---

### 🎲 pop()

```python
my_set.pop()
```

👉 Random element remove karta hai  

---

### 🔗 union()

```python
set1 = {1, 2}
set2 = {2, 3}

print(set1.union(set2))
```

👉 Dono sets ko combine karta hai  

---

### 🤝 intersection()

```python
print(set1.intersection(set2))
```

👉 Common elements return karta hai  

---

# 🚀 Summary

* Dictionary → key-value pair me data store karta hai  
* Keys unique hoti hain  
* Set → duplicate values allow nahi karta  
* Set unordered hota hai  
* Dono powerful data structures hain  

---

# 📈 Progress

* [x] Day 1 Completed ✅  
* [x] Day 2 Completed ✅  
* [x] Day 3 Completed ✅  
* [x] Day 4 Completed ✅  
* [ ] Day 5 Coming Soon 🚀  

---

# 🔥 #BuildInPublic