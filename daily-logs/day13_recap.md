# 📘 Day 13 Log — AI/ML Journey

> 🚀 Building in Public  
> 📅 Day 13 — Python Basics Completed

---

## 🧠 Aaj maine kya kiya

aaj mera day 13 tha  
aur aaj maine apna python course complete kar liya (basic level)  

last video OOPs ke topics pe tha — inheritance aur polymorphism  
uske baad maine 2 mini projects banaye  

---

## 💻 Practice / Kaam

### 🔹 Project 1: Random Number Guess Game

isme maine `random` module use kiya  

```python
import random
```

👉 `random.randint(start, end)`  
ye random number generate karta hai given range ke andar  

example:
```python
random.randint(1, 100)
```

is project me:
- user se input liya
- ek random target number generate kiya
- jab tak user sahi guess nahi kare → loop chalta raha

👉 ye project maine `python/projects` section me dala hai  

---

### 🔹 Project 2: Random Password Generator

is project me maine `random` and `string` module use kiya  

```python
import string
```

👉 important cheezein jo use ki:
- `string.ascii_letters` → small + capital alphabets  
- `string.digits` → numbers (0–9)  
- `string.punctuation` → special characters  

👉 fir random password generate kiya using:

```python
"".join([random.choice(chars) for i in range(8)])
```

---

### 🔹 New Concept: List Comprehension

👉 ek line me loop ka kaam kar deta hai  

```python
[expression for item in iterable]
```

👉 fast + clean way hai list banane ka  

---

## 🧠 Mujhe kya samajh aaya

- python ka basic flow clear ho gaya  
- random module ka real use samajh aaya  
- string module ka use karke real world project bana sakte hain  
- list comprehension kaafi powerful cheez hai (short me kaam ho jata hai)  

---

## ⚠️ Problem / Confusion

- list comprehension thoda confusing laga start me  
- password generator logic samajhne me thoda time laga  

---

## 🚀 Next Plan

- kal apna roadmap dubara dekhunga  
- decide karunga next kya start karna hai (DSA / NumPy / kuch aur)  
- GitHub update karunga (README improve karna hai, look better banana hai)  

---

## 💭 Personal Note

aaj acha laga ki python ka basic complete ho gaya  
abhi advance nahi aata but ek strong start ho gaya hai  

ab thoda clear feel ho raha hai ki aage kaise move karna hai  
bas consistency maintain rakhni hai 🔥  

---

# 🔥 #BuildInPublic