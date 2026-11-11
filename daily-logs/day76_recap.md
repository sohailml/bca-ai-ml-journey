# 🚀 Day 76 — AI/ML Learning Journey

📅 **Date:** 11 November 2026  
🎯 **Main Focus:** NumPy — Day 1  
📚 **Learning Source:** Chai aur Code — Hitesh Choudhary Sir  
💻 **Notebook:** `day01.ipynb`

---

## 📌 Today's Progress

Aaj finally NumPy learning start kar di!

Python fundamentals aur Dictionaries & Sets ka 100-question practice set complete karne ke baad ab NumPy ke saath numerical computing ki journey shuru ho gayi hai.

Aaj ka session mainly NumPy introduction, environment setup, array creation aur Python Lists vs NumPy Arrays ke differences par focused raha.

---

## 🧮 1. Introduction to NumPy Arrays

Sabse pehle NumPy arrays ke baare mein padha.

### 1D Array — Vector

Ek simple one-dimensional array ko vector bhi kaha jata hai.

```python
[1, 2, 3]
```

### 2D Array — Matrix

Jab multiple rows aur columns hote hain, toh use two-dimensional array ya matrix kehte hain.

```python
[
    [1, 2, 3],
    [4, 5, 6]
]
```

Ye concepts numerical computing aur Machine Learning mein kaafi important hain.

---

## ⚙️ 2. Virtual Environment Setup

NumPy start karne se pehle Python Virtual Environment create karna seekha.

### Create Virtual Environment

```bash
python -m venv venv
```

Agar hidden-style naming convention use karna ho, toh:

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Agar `.venv` folder banaya hai:

```bash
.venv\Scripts\activate
```

Virtual Environment ka main purpose project dependencies ko isolate rakhna hai, taaki different projects ke packages ek doosre ko affect na karein.

---

## 📦 3. Installing and Importing NumPy

Virtual Environment activate karne ke baad NumPy install kiya.

### Installation

```bash
pip install numpy
```

### Importing NumPy

```python
import numpy as np
```

Yahan `np` NumPy ka commonly used alias hai.

Technically, hum doosra alias bhi use kar sakte hain, lekin Python community mein `np` standard convention hai.

---

## 🔢 4. Creating Arrays Using `np.array()`

NumPy mein arrays create karne ke liye `np.array()` function use hota hai.

### Example: 1D Array

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

Output:

```text
[1 2 3]
```

### Example: 2D Array

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

**Important:** `np.array()` mein ek required positional argument hota hai — array banane ke liye input data. Iske alawa optional arguments bhi available hain.

---

## ⚡ 5. Python List vs NumPy Array Multiplication

Aaj ka ek important concept tha Python List aur NumPy Array ke multiplication behaviour ka difference.

### Python List Multiplication

Python List ko kisi integer se multiply karne par list repeat hoti hai.

```python
py_list = [1, 2, 3]

print("Python List Multiplication:", py_list * 2)
```

Output:

```text
Python List Multiplication: [1, 2, 3, 1, 2, 3]
```

Yahan list ke elements individually multiply nahi hote, balki poori list repeat hoti hai.

### NumPy Array Multiplication

NumPy Array mein multiplication element-wise hota hai.

```python
np_array = np.array([1, 2, 3])

print("NumPy Array Multiplication:", np_array * 2)
```

Output:

```text
NumPy Array Multiplication: [2 4 6]
```

Yahan har element ko 2 se multiply kiya gaya hai.

Is operation ko scalar multiplication bhi kehte hain.

---

## 📈 6. Creating Arrays Using `np.arange()`

Aaj `np.arange()` function ke baare mein bhi padha.

Iska use specified range ke andar evenly spaced values generate karne ke liye hota hai.

### Syntax

```python
np.arange(start, stop, step)
```

- `start`: Starting value.
- `stop`: Ending limit, excluded.
- `step`: Values ke beech ka interval.

### Example

```python
arr = np.arange(1, 10, 2)

print(arr)
```

Output:

```text
[1 3 5 7 9]
```

### Large Array Creation

```python
arr = np.arange(1000000)

print(arr)
```

Isse 0 se 999999 tak values ka array create hota hai.

---

## 🚀 7. Python List vs NumPy Performance Comparison

Aaj ek practical experiment bhi kiya jisse NumPy ki computational performance samajhne mein help mili.

Is experiment mein Python List aur NumPy Array dono se 1 million values ko 2 se multiply kiya.

### Python List Operation

```python
import time

start = time.time()

py_list = [i * 2 for i in range(1000000)]

print("\nList operation time:", time.time() - start)
```

### NumPy Array Operation

```python
start = time.time()

np_array = np.arange(1000000) * 2

print("\nNumPy operation time:", time.time() - start)
```

Dono operations ka execution time compare kiya.

**Observation:**

NumPy vectorized operations use karta hai, jisse numerical computations generally Python-level loops ke comparison mein kaafi fast ho sakte hain.

Actual execution time system aur environment par depend karta hai.

---

## 📂 8. GitHub Notebook Organization

Aaj NumPy ka first practical notebook create kiya.

**File Name:** `day01.ipynb`

**Location:**

```text
bca-ai-ml-journey/
│
└── numpy/
    │
    └── notes-code/
        │
        └── day01.ipynb
```

Aaj ke saare concepts aur code examples isi Jupyter Notebook mein maintain kiye hain.

---

## 📊 Today's Learning Summary

| Topic | Status |
|---|---|
| NumPy Introduction | ✅ Covered |
| 1D Arrays / Vectors | ✅ Covered |
| 2D Arrays / Matrices | ✅ Covered |
| Virtual Environment | ✅ Covered |
| NumPy Installation | ✅ Covered |
| `np.array()` | ✅ Covered |
| List vs Array Multiplication | ✅ Covered |
| `np.arange()` | ✅ Covered |
| Performance Comparison | ✅ Practiced |
| Jupyter Notebook | ✅ Created |

---

## 🎓 Andrew Ng's Machine Learning Course

Aaj Andrew Ng ke Supervised Machine Learning course ka sirf overview liya.

Course ki actual learning abhi start nahi ki.

Financial Aid approval ke baad ab plan hai ki NumPy ke saath is course ko bhi parallel mein cover karunga.

---

## 📅 Day 77 — Next Session Plan

### 🧮 NumPy

- [ ] Continue learning from Chai aur Code.
- [ ] Understand more NumPy array concepts.
- [ ] Practice array creation and operations.
- [ ] Update `day01.ipynb` with new concepts.

### 🎓 Coursera

- [ ] Start Andrew Ng's Supervised Machine Learning course.
- [ ] Begin with the first lesson.
- [ ] Maintain separate notes for important ML concepts.

---

## 💡 Day 76 Takeaway

Aaj finally NumPy learning start ho gayi!

Virtual Environment setup se lekar NumPy arrays, vectors, matrices, scalar multiplication aur `np.arange()` tak multiple concepts cover kiye.

Saath hi ek practical performance comparison bhi kiya, jisse NumPy ke vectorized operations ka advantage samajhne ko mila.

Ab next target NumPy ko practically strong banana aur Andrew Ng ke Machine Learning course ko parallel start karna hai.

**Day 76 Status:** NumPy Started | First Notebook Created | Core Array Concepts Introduced.

**Next Milestone:** NumPy + Andrew Ng's Machine Learning Course. 🚀
