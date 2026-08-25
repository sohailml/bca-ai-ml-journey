# 🐍 Python Basics — Day 2

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 2 — Strings & Conditional Statements

---

## 📌 1. Strings in Python

Python me string ka use text (words / sentence / characters) store karne ke liye hota hai.

```python
str1 = 'sohail'
str2 = "sohail"
str3 = """sohail"""
```

👉 Jo bhi text quotes (`" "` ya `' '`) ke andar hota hai → wo string hota hai.

---

### ❓ Why Double / Triple Quotes?

Agar string ke andar apostrophe (`'`) use karna ho to error avoid karne ke liye double ya triple quotes use karte hain.

```python
str = "I'm Sohail"  # ✅ Correct
```

---

## 📌 2. Escape Characters

Special formatting ke liye use hote hain:

```python
print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab space
```

👉 `\n` → next line  
👉 `\t` → tab space

---

## 📌 3. String Concatenation

Concatenation ka matlab hota hai strings ko jodna.

```python
str1 = "Sohail"
str2 = "Ansari"

print(str1 + str2)        # SohailAnsari
print(str1 + " " + str2)  # Sohail Ansari
```

👉 Space automatically nahi aata, manually `" "` dena padta hai.

---

## 📌 4. Length of String

String ki length (characters count) nikalne ke liye `len()` use hota hai.

```python
str = "sohail"
print(len(str))  # 6

str1 = "soh ail"
print(len(str1))  # 7 (space bhi count hota hai)
```

---

## 📌 5. Indexing

Har character ka index hota hai (0 se start hota hai).

```python
str = "sohail"

print(str[2])   # h
print(str[-4])  # h (negative indexing)
```

👉 Positive index → left se start  
👉 Negative index → right se start

---

## 📌 6. Slicing

String ka ek part nikalne ke liye slicing use hoti hai.

```python
str = "sohail"

print(str[0:3])  # soh
print(str[:3])   # soh
print(str[1:])   # ohail
```

👉 Last index include nahi hota  
👉 Blank start = 0  
👉 Blank end = length

### 🔹 Negative Slicing

```python
print(str[-6:-3])  # soh
```

---

## 📌 7. String Functions

### 🔹 endswith()

Check karta hai string kis value pe end ho rahi hai.

```python
str = "sohail"
print(str.endswith("l"))  # True
```

---

### 🔹 capitalize()

First letter ko capital bana deta hai.

```python
print(str.capitalize())  # Sohail
```

---

### 🔹 replace()

Ek value ko dusri se replace karta hai.

```python
str = "i am learning html"
print(str.replace("html", "python"))
```

👉 Output: `i am learning python`

---

### 🔹 find()

Kisi value ka first index return karta hai.

```python
str = "sohail is learning"

print(str.find("l"))        # 5
print(str.find("learning")) # 10
print(str.find("xyz"))      # -1
```

👉 Agar value nahi mili → `-1`

---

### 🔹 count()

Count karta hai kitni baar value aayi hai.

```python
str = "arbaaz"
print(str.count("a"))  # 3
```

---

## 📌 8. Conditional Statements

Condition ke basis pe code run hota hai.

```python
age = 24

if (age >= 18):
    print("can vote")

elif (age == 17):
    print("can not vote but apply for pan card")

else:
    print("can not vote")
```

👉 Output: `can vote`

---

### 🔹 How it Works

* `if` → hamesha check hota hai
* `elif` → tab run hota hai jab upar wala false ho
* `else` → jab sab false ho

---

## 📌 9. Nesting in If

If ke andar ek aur if.

```python
a = 20

if (a > 0):
    if (a % 2 == 0):
        print("a is positive and even")
    else:
        print("a is positive and odd")

elif (a == 0):
    print("a is 0")

else:
    print("a is negative")
```

👉 Output: `a is positive and even`

---

# 🚀 Summary

* Strings → text store karte hain
* Escape characters → formatting ke liye
* Concatenation → strings ko jodta hai
* len() → length nikalta hai
* Indexing / Slicing → string access karne ke liye
* String functions → operations perform karte hain
* if-elif-else → condition handle karta hai
* Nested if → advanced condition

---

# 📈 Progress

* [x] Day 1 Completed ✅  
* [x] Day 2 Completed ✅  
* [ ] Day 3 Coming Soon 🚀  

---

# 🔥 #BuildInPublic