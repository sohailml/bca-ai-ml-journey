# 🚀 Day 83 — AI/ML Learning Journey

📅 **Date:** 18 November 2026  
🎯 **Main Focus:** NumPy — Day 5 + Andrew Ng Machine Learning — Day 5  
📚 **Learning Sources:** Chai aur Code — Hitesh Choudhary Sir | Andrew Ng — Supervised Machine Learning: Regression and Classification  
💻 **Notebooks:** `numpy/notes-code/day05.ipynb` | `andrew-ng/day05.ipynb`

---

## 🔢 1. NumPy — Array Manipulation

Aaj NumPy mein Conditional Arrays, Array Concatenation, Array Compatibility, Stacking aur Deleting Elements ke baare mein seekha.

### 🎯 1. Conditional Array — `np.where()`

Python ke `if-else` ki tarah NumPy mein bhi conditions ke basis par values select ya modify kar sakte hain.

Syntax:

```python
np.where(condition, value_if_true, value_if_false)
```

Ismein 3 parameters hote hain:

- **First:** Condition check hoti hai.
- **Second:** Agar condition `True` hai toh ye value return hogi.
- **Third:** Agar condition `False` hai toh ye value return hogi.

Example:

```python
numbers = np.arange(1, 11)

result = np.where(numbers > 5, numbers * 2, numbers)

print(result)
```

Output:

```text
[ 1  2  3  4  5 12 14 16 18 20]
```

Yahan:
- Numbers greater than 5 ko 2 se multiply kiya.
- Baaki numbers same rakhe.

### 🔗 2. Combining / Merging Arrays — `np.concatenate()`

Multiple arrays ko combine karne ke liye `np.concatenate()` use karte hain.

Syntax:

```python
np.concatenate((array1, array2))
```

Example:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.concatenate((arr1, arr2))

print(result)
```

Output:

```text
[1 2 3 4 5 6]
```

**Important:** Arrays ko tuple ke andar pass karte hain. Multidimensional arrays combine karte waqt selected axis ke alawa baaki dimensions compatible hone chahiye.

### ⚖️ 3. Array Compatibility

Do arrays par operations perform karne se pehle check karna hota hai ki unke shapes compatible hain ya nahi.

Ye concept especially important hai:

- Addition
- Subtraction
- Multiplication
- Concatenation
- Stacking

For example, element-wise addition mein same shape wale arrays directly add kiye ja sakte hain. NumPy broadcasting ke through kuch different shapes wale arrays par bhi operations possible hote hain.

**Key Learning:** Har array combination ya operation ke liye dimensions aur shape compatibility samajhna zaroori hai.

### 🧱 4. Adding Arrays — `vstack()` and `hstack()`

NumPy mein arrays ko vertically aur horizontally stack kar sakte hain.

**A. `np.vstack()` — Vertical Stacking**

Arrays ko row-wise, yaani ek ke neeche ek add karta hai.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))

print(result)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

**B. `np.hstack()` — Horizontal Stacking**

Arrays ko horizontally combine karta hai.

```python
result = np.hstack((arr1, arr2))

print(result)
```

Output:

```text
[1 2 3 4 5 6]
```

**Remember:**
- `vstack()` → Vertical stacking.
- `hstack()` → Horizontal stacking.

In dono functions mein arrays ko tuple ke andar pass karte hain.

### 🗑️ 5. Deleting Elements — `np.delete()`

Array se kisi particular element ya index ko remove karne ke liye `np.delete()` use karte hain.

Syntax:

```python
np.delete(array, index)
```

Example:

```python
numbers = np.array([10, 20, 30, 40, 50])

result = np.delete(numbers, 2)

print(result)
```

Output:

```text
[10 20 40 50]
```

Yahan index `2` par present element `30` remove ho gaya.

**Important:** `np.delete()` original array ko modify nahi karta. Ye deleted element ke bina ek new array return karta hai.

---

## 🤖 2. Andrew Ng — Gradient Descent

Aaj Andrew Ng course mein ek bahut important Machine Learning optimization algorithm padha: **Gradient Descent**.

### 🎯 What is Gradient Descent?

Gradient Descent ek optimization algorithm hai jo Cost Function ki minimum value find karne ke liye parameters ko repeatedly update karta hai.

Iska main objective:

\[
\text{Minimize } J(w,b)
\]

Iska use bahut saare Machine Learning aur Deep Learning models ki training mein hota hai.

Examples:
- Linear Regression
- Neural Networks
- Deep Learning

### ⛰️ 1. Local Minimum vs Global Minimum

**Local Minimum:**

Kisi particular surrounding area mein sabse low point ko Local Minimum kehte hain.

**Global Minimum:**

Poore function ke domain mein sabse low point Global Minimum hota hai.

Linear Regression ka squared-error Cost Function convex bowl shape ka hota hai. Is case mein ek Global Minimum hota hai.

### 📐 2. Gradient Descent Formula

Gradient Descent mein parameters ko repeatedly update kiya jaata hai.

$$\text{Repeat until convergence: } \begin{cases} w := w - \alpha \frac{\partial}{\partial w} J(w,b) \\ b := b - \alpha \frac{\partial}{\partial b} J(w,b) \end{cases}$$

**Formula mein symbols ka meaning:**

| Symbol | Meaning |
|---|---|
| `w` | Weight parameter |
| `b` | Bias parameter |
| `α` (alpha) | Learning Rate |
| `J(w,b)` | Cost Function |
| `∂J/∂w` | Cost ka derivative with respect to w |
| `∂J/∂b` | Cost ka derivative with respect to b |
| `:=` | Assignment / Update operation |

Derivative batata hai ki kisi particular point par Cost Function ka slope kya hai aur kis direction mein change ho raha hai.

### 📉 3. Learning Rate — Alpha (α)

Learning Rate decide karta hai ki har iteration mein parameters kitne bade steps lenge.

Matlab Gradient Descent mein hum minimum ki taraf move karte hain, aur alpha step ka size control karta hai.

**Case 1: Learning Rate Bahut Small**

Example:

\[
\alpha = 0.000001
\]

- Har step bahut chhota hoga.
- Cost decrease ho sakti hai.
- Minimum tak pahunchne mein bahut zyada iterations lag sakte hain.

**Case 2: Learning Rate Bahut Large**

- Har step bahut bada hoga.
- Algorithm minimum point ko overshoot kar sakta hai.
- Cost increase ya fluctuate ho sakti hai.
- Algorithm converge karne mein fail bhi ho sakta hai.

**Key Learning:** Learning Rate ko carefully choose karna important hai.

### 🧭 4. Derivative — Direction and Slope

Derivative Cost Function ke current point par slope batata hai.

**Case 1: Positive Slope**

Agar slope positive hai:

\[
w := w-\alpha(\text{positive value})
\]

Toh `w` decrease hoga.

Isse algorithm left direction mein move karega.

**Case 2: Negative Slope**

Agar slope negative hai:

\[
w := w-\alpha(\text{negative value})
\]

Toh `w` increase hoga.

Isse algorithm right direction mein move karega.

**Main Concept:** Gradient Descent derivative ki help se decide karta hai ki parameters ko kis direction mein update karna hai.

### ✨ 5. Magic of Gradient Descent — Minimum Ke Paas Kya Hota Hai?

Jab algorithm minimum ke paas pahunchta hai, toh Cost Function ka slope approximately zero ho jaata hai.

Is wajah se parameter updates bhi chhote hone lagte hain, even when learning rate fixed ho.

Matlab:
- Minimum se door → Slope generally larger.
- Minimum ke paas → Slope generally smaller.
- Minimum par → Derivative zero (smooth differentiable function ke case mein).

Isliye algorithm minimum ke paas automatically smaller steps leta hai.

### 🔄 6. Simultaneous Update — Very Important!

Gradient Descent mein `w` aur `b` ko simultaneously update karna hota hai.

Iska matlab dono updates ke liye purane `w` aur `b` se derivatives calculate karne hain.

Correct approach:

```python
temp_w = w - alpha * dj_dw
temp_b = b - alpha * dj_db

w = temp_w
b = temp_b
```

Yahan dono temporary variables calculate hone ke baad original parameters update hote hain.

**Incorrect approach:** Pehle `w` update kar dena aur phir naye `w` ka use karke `b` update karna.

Aisa karne se simultaneous update rule follow nahi hota.

### ✅ DO vs ❌ DON'T

| ✅ DO | ❌ DON'T |
|---|---|
| `w` aur `b` simultaneously update karo | Sequential update mat karo |
| Derivatives purane `w`, `b` se calculate karo | Updated `w` se `b` ka derivative calculate mat karo |
| Temporary variables use karo | Pehle parameter update karke doosre ko calculate mat karo |
| Learning Rate carefully choose karo | Bahut large ya bahut small alpha blindly use mat karo |

---

## 🧠 3. Day 83 — Concept Mind Map

```text
Day 83
│
├── NumPy
│   ├── Conditional Arrays
│   │   └── np.where()
│   │
│   ├── Combining Arrays
│   │   └── np.concatenate()
│   │
│   ├── Array Compatibility
│   │   └── Shape & Dimensions
│   │
│   ├── Stacking
│   │   ├── np.vstack()
│   │   └── np.hstack()
│   │
│   └── Deleting
│       └── np.delete()
│
└── Andrew Ng — Gradient Descent
    │
    ├── Minimum
    │   ├── Local Minimum
    │   └── Global Minimum
    │
    ├── Gradient Descent Formula
    │   ├── Weight Update
    │   └── Bias Update
    │
    ├── Learning Rate (α)
    │   ├── Too Small
    │   └── Too Large
    │
    ├── Derivative
    │   ├── Positive Slope
    │   └── Negative Slope
    │
    └── Simultaneous Update
        ├── temp_w
        └── temp_b
```

---

## 📚 4. Day 83 — Quick Revision

| Topic | What I Learned |
|---|---|
| `np.where()` | Condition-based values select karna |
| `np.concatenate()` | Multiple arrays combine karna |
| Array Compatibility | Shapes aur dimensions check karna |
| `np.vstack()` | Vertical stacking |
| `np.hstack()` | Horizontal stacking |
| `np.delete()` | Array se elements remove karna |
| Gradient Descent | Cost Function minimize karna |
| Local Minimum | Local area ka lowest point |
| Global Minimum | Entire function ka lowest point |
| Learning Rate | Step size control karna |
| Derivative | Slope aur update direction samajhna |
| Simultaneous Update | `w` aur `b` ko ek saath update karna |

---

## 🎯 5. Next Plan

Aaj ke liye itna hi study kiya.

Kal NumPy aur Andrew Ng Machine Learning course ko continue karunga.

**Day 83 Completed!** 🚀

Aaj NumPy mein array manipulation aur Machine Learning mein Gradient Descent ke fundamentals cover kiye. Ab focus in concepts ko revise karne aur practical implementation samajhne par rahega.
