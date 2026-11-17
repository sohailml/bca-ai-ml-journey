# 🚀 Day 82 — AI/ML Learning Journey

📅 **Date:** 17 November 2026  
🎯 **Main Focus:** NumPy — Day 4 + Andrew Ng Machine Learning — Day 4  
📚 **Learning Sources:** Chai aur Code — Hitesh Choudhary Sir | Andrew Ng — Supervised Machine Learning: Regression and Classification  
💻 **Notebooks:** `numpy/notes-code/day04.ipynb` | `andrew-ng/day04.ipynb`

---

## 🔢 1. NumPy — Array Operations

Aaj NumPy mein Array Indexing, Slicing, Sorting aur Filtering ke baare mein seekha.

### 📌 1. Array Indexing and Slicing

Python lists ki tarah NumPy arrays mein bhi indexing aur slicing use hoti hai.

**1D Array:** Normal Python indexing ki tarah elements access kar sakte hain.

**2D Array:** Ismein do arguments provide karte hain:
- First argument: Row index
- Second argument: Column index

```python
arr_2d[1, 2]
```

Iska matlab second row aur third column ka element access karna.

**Complete Row Access Karna:**

```python
arr_2d[1]
```

Ye second row return karega.

**Complete Column Access Karna:**

```python
arr_2d[:, 1]
```

Yahan `:` ka matlab sabhi rows aur `1` ka matlab second column hai.

### 🔃 2. Array Sorting

NumPy mein array ko sort karne ke liye `np.sort()` use karte hain.

**1D Array Sorting:**

```python
sorted_array = np.sort(unsorted_array)
```

**2D Array Sorting:**

2D array mein `axis` specify karke sorting kar sakte hain.

```python
# Column-wise sorting
np.sort(unsorted_array, axis=0)

# Row-wise sorting
np.sort(unsorted_array, axis=1)
```

- `axis=0` → Har column ke elements sort honge.
- `axis=1` → Har row ke elements sort honge.

### 🎯 3. Array Filtering

Filtering ka matlab kisi condition ko satisfy karne wale elements ko select karna hai.

Example: 1 se 10 tak numbers mein se even numbers find karna.

```python
numbers = np.arange(1, 11)

even = numbers[numbers % 2 == 0]

print("Even numbers:", even)
```

Output:

```text
Even numbers: [ 2  4  6  8 10]
```

### 🎭 4. Filtering with Mask

Mask basically ek condition-based Boolean array hota hai.

Example:

```python
mask = numbers % 2 == 0

print(mask)
```

Ye har element ke liye `True` ya `False` return karta hai. Is Boolean mask ko array indexing ke saath use karke required elements filter kar sakte hain.

### 🔍 5. Fancy Indexing vs np.where()

**Fancy Indexing**

Ismein hum manually indices ki list provide karte hain, jin elements ko access karna hai.

```python
indices = [0, 2, 4]

print(numbers[indices])
```

Ye index 0, 2 aur 4 ke elements return karega.

**np.where()**

Iska use condition ke basis par elements ke indices find karne ke liye kiya ja sakta hai.

```python
even_indices = np.where(numbers % 2 == 0)

print(even_indices)
```

Ye condition satisfy karne wale elements ke indices return karega.

---

## 🤖 2. Andrew Ng — Cost Function Visualization

Aaj Andrew Ng course mein Cost Function ki visualization par focus kiya. Ismein do important concepts cover kiye:

### 🥣 1. 3D Surface Plot

Pichhle lecture mein humne simplified model use kiya tha:

\[
f(x) = wx
\]

Lekin ab original model use kiya:

\[
f(x) = wx+b
\]

Yahan `w` aur `b` dono parameters hain.

3D Surface Plot mein:

- X-axis → `w`
- Y-axis → `b`
- Z-axis → Cost Function `J(w,b)`

Jab different `w` aur `b` values try karte hain, toh har combination ke liye alag cost milti hai.

In values ko visualize karne par graph ek bowl ya hammock jaisa shape banata hai.

**Important Points:**
- Bowl ke top par cost high hoti hai.
- Bowl ke bottom par cost minimum hoti hai.
- Bottom point best `w` aur `b` values represent karta hai.

### 🗺️ 2. Contour Plot

Contour Plot basically 3D bowl ka top-view hota hai.

Ismein:
- Horizontal axis → `w`
- Vertical axis → `b`
- Elliptical curves → Same cost value wale points.

Jaise mountain map mein contour lines same height represent karti hain, waise hi Cost Function ke contour plot mein har ellipse ek particular cost level represent karti hai.

**Main Concept:**

Sabse chhoti ellipse ke center ke paas Cost Function ka minimum point hota hai.

---

## 💻 3. Lab — Cost Function Implementation

Aaj course mein Cost Function ko Python mein implement karne wala lab bhi kiya.

### 🎯 Lab Goal

Python function `compute_cost()` implement karna, jo training data, weight `w` aur bias `b` use karke total cost calculate karta hai.

### Python Code

```python
def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost_sum = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum = cost_sum + cost

    total_cost = (1 / (2 * m)) * cost_sum

    return total_cost
```

### 🔍 Line-by-Line Breakdown

**Step 1: Number of Training Examples**

```python
m = x.shape[0]
```

`x.shape[0]` se training examples ki total count milti hai.

**Step 2: Cost Sum Initialize Karna**

```python
cost_sum = 0
```

Ek accumulator variable banaya jo sabhi examples ke squared errors ko add karega.

**Step 3: Har Training Example Par Loop**

```python
for i in range(m):
```

Loop har training example par execute hoga.

**Step 4: Prediction Calculate Karna**

```python
f_wb = w * x[i] + b
```

Linear Regression formula use karke prediction calculate hoti hai.

\[
f(x) = wx+b
\]

**Step 5: Squared Error Calculate Karna**

```python
cost = (f_wb - y[i]) ** 2
```

Prediction aur actual value ka difference lekar uska square karte hain.

**Step 6: Total Cost Mein Add Karna**

```python
cost_sum = cost_sum + cost
```

Har example ka squared error total sum mein add hota hai.

**Step 7: Final Cost Calculate Karna**

```python
total_cost = (1 / (2 * m)) * cost_sum
```

Ye Cost Function ka formula implement karta hai:

\[
J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}
(f_{w,b}(x^{(i)})-y^{(i)})^2
\]

**Step 8: Final Result Return Karna**

```python
return total_cost
```

Calculated Cost Function ki value return hoti hai.

---

## 🧠 4. Day 82 — Concept Mind Map

```text
NumPy
│
├── Indexing & Slicing
│   ├── 2D Indexing
│   ├── Row Access
│   └── Column Access
│
├── Sorting
│   ├── np.sort()
│   ├── axis=0 → Column-wise
│   └── axis=1 → Row-wise
│
├── Filtering
│   ├── Boolean Mask
│   ├── Fancy Indexing
│   └── np.where()
│
└── Andrew Ng — Cost Function
    │
    ├── 3D Surface Plot
    │   ├── w
    │   ├── b
    │   └── J(w,b)
    │
    ├── Contour Plot
    │   ├── Top View
    │   ├── Elliptical Curves
    │   └── Minimum Cost
    │
    └── Python Lab
        └── compute_cost()
```

---

## 📚 5. Day 82 Quick Revision

| Topic | What I Learned |
|---|---|
| NumPy Indexing | 2D arrays mein rows aur columns access karna |
| NumPy Slicing | Required rows aur columns select karna |
| Sorting | `np.sort()` with axis |
| Filtering | Conditions ke basis par elements select karna |
| Boolean Mask | True/False condition-based selection |
| Fancy Indexing | Multiple indices se elements access karna |
| `np.where()` | Condition ke basis par indices find karna |
| 3D Surface Plot | Cost Function ko visualize karna |
| Contour Plot | Cost Function ka top view |
| Cost Function Lab | Python mein `compute_cost()` implement karna |

---

**Day 82 Completed!** 🚀

Aaj NumPy ke array operations aur Machine Learning ke Cost Function visualization aur implementation par kaam kiya.
