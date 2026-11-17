# 🚀 Day 81 — AI/ML Learning Journey

📅 **Date:** 16 November 2026  
🎯 **Main Focus:** NumPy — Day 3 + Andrew Ng Machine Learning — Day 3  
📚 **Learning Sources:** Chai aur Code — Hitesh Choudhary Sir | Andrew Ng — Supervised Machine Learning: Regression and Classification  
💻 **Notebooks:** `numpy/notes-code/day03.ipynb` | `andrew-ng/day03.ipynb`

---

## 🔢 1. NumPy — Array Properties & Reshaping

Aaj NumPy mein arrays ki kuch important properties aur reshaping operations ke baare mein seekha.

### 📌 Array Properties

**1. `.shape`**

Is property se array ka shape pata chalta hai, yaani kitni rows aur columns hain.

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)
# Output: (2, 3)
```

Yahan `2` rows aur `3` columns hain.

**2. `.ndim`**

Isse pata chalta hai ki array kitne dimensions ka hai — 1D, 2D, 3D, etc.

```python
print(arr.ndim)
# Output: 2
```

**3. `.size`**

Array ke andar total kitne elements hain, ye batata hai.

```python
print(arr.size)
# Output: 6
```

**4. `.dtype`**

Array ke elements ka data type batata hai.

```python
print(arr.dtype)
```

### 🔄 Array Reshaping

Reshaping ka matlab array ka shape change karna hai, bina uske elements ko change kiye.

**1. `reshape()`**

Is method se array ko required rows aur columns mein convert kar sakte hain.

```python
arr = np.arange(12)

print(arr)
# [0 1 2 3 4 5 6 7 8 9 10 11]

reshaped = arr.reshape(3, 4)

print(reshaped)
```

Output:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

**2. `flatten()`**

Is method se multidimensional array ko 1D array mein convert karte hain. Ye ek copy return karta hai.

```python
flat = reshaped.flatten()
```

**3. `ravel()`**

Ye bhi multidimensional array ko 1D form mein convert karta hai, lekin generally view return karta hai, agar possible ho.

```python
flat = reshaped.ravel()
```

### 🔁 Transpose

Transpose operation mein rows columns ban jaati hain aur columns rows.

Example: 2×3 array transpose hokar 3×2 ban jaata hai.

```python
transposed = reshaped.T
```

---

## 🤖 2. Andrew Ng — Linear Regression & Notation

Aaj Andrew Ng ke course mein Linear Regression ka introduction aur uski mathematical notation samjhi.

### 🏠 Linear Regression — House Price Prediction

House price prediction ka example use karke samjha ki Linear Regression kaise kaam karta hai.

- **X-axis:** House size (input)
- **Y-axis:** House price (output)
- Graph par training data ke points plot kiye jaate hain.
- Model ek straight line fit karta hai.
- Us line ki help se naye house ka price predict kiya jaata hai.

### 📚 Important Notations

| Symbol | Meaning |
|---|---|
| `x` | Input feature |
| `y` | Actual output / Target value |
| `m` | Total number of training examples |
| `(x⁽ⁱ⁾, y⁽ⁱ⁾)` | i-th training example |
| `f(x)` | Prediction function |
| `ŷ` | Predicted output (Y-hat) |

**Important:** `i` training example ka index hota hai, exponent ya power nahi.

### ⚙️ Supervised Learning Kaise Work Karta Hai?

Supervised Learning ka basic process:

1. Training dataset provide kiya jaata hai — `(X, Y)`.
2. Learning algorithm training data ko use karta hai.
3. Algorithm ek prediction function `f` learn karta hai.
4. New input dene par function output predict karta hai — `ŷ`.

### 📐 Linear Regression Formula

Univariate Linear Regression ka formula:

\[
f_{w,b}(x) = wx + b
\]

Yahan:

- `w` = Slope / Weight
- `b` = Y-intercept / Bias
- `x` = Input
- `f(x)` = Predicted output

**Slope (`w`):** Jab `x` mein 1 unit increase hota hai, toh predicted `y` kitna change hota hai, ye slope batata hai.

**Intercept (`b`):** Jab `x = 0` hota hai, tab model ki predicted `y` value intercept hoti hai.

**Univariate:** `Uni` ka matlab one aur `variate` ka matlab variable. Isliye Univariate Linear Regression mein ek input feature hota hai.

---

## 📉 3. Cost Function — Model Ki Performance Measure Karna

Aaj ka ek important concept tha **Cost Function**.

Cost Function measure karta hai ki model ki predictions actual values se kitni different hain.

- Cost high = Model ki prediction errors zyada hain.
- Cost low = Model ki prediction errors kam hain.
- Goal = Cost ko minimize karna.

### 🧮 Cost Function Calculate Kaise Karte Hain?

1. Prediction aur actual value ka difference calculate karo.
2. Error ka square karo.
3. Sabhi training examples ke squared errors ko add karo.
4. Total ko `m` se divide karo.
5. Phir `2` se divide karo.

Formula:

\[
J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}
\left(f_{w,b}(x^{(i)})-y^{(i)}\right)^2
\]

Yahan:

- `J(w,b)` = Cost Function
- `m` = Number of training examples
- `f(x)` = Predicted value
- `y` = Actual value

**Main Goal:** Aise `w` aur `b` find karna jisse Cost Function ki value minimum ho.

---

## 🧠 4. Cost Function — Intuition (Lecture 12)

Is lecture mein Cost Function ko visually samajhne ke liye Andrew Ng ne model ko simplify kiya.

### Simplification: `b = 0`

Original model:

\[
f(x) = wx+b
\]

Simplified model:

\[
f(x) = wx
\]

Yahan `b = 0` kar diya, taaki sirf ek parameter `w` ko change karke cost ka effect 2D graph par samajh sakein.

Ye sirf visualization ke liye simplification hai. Actual Linear Regression mein `w` aur `b` dono parameters hote hain.

### 📊 Training Data Example

| x (Input) | y (Actual) |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

Ab alag-alag `w` values try karte hain.

| w | Model | Cost (J) | Result |
|---|---|---:|---|
| 1 | `f(x) = x` | 0 | Perfect fit |
| 0.5 | `f(x) = 0.5x` | 0.58 | Line data ke neeche |
| 0 | `f(x) = 0` | 2.33 | Horizontal line |
| -0.5 | `f(x) = -0.5x` | 5.25 | Negative slope |

**Observation:**

- `w = 1` par model ki prediction actual values ke equal hai.
- Isliye cost `0` hai.
- `w` ko change karne par prediction line change hoti hai.
- Line jitni data se door hogi, cost utni zyada ho sakti hai.

### 🎯 Cost Function Ka Main Goal

\[
\boxed{\text{Minimize } J(w,b)}
\]

Matlab aise parameters find karna jisse model ki prediction error minimum ho.

Simplified version mein `J(w)` ka graph 2D hota hai. Full version mein `J(w,b)` ko visualize karne ke liye 3D graph use kar sakte hain.

---

## 💻 5. Lab — Model Representation (Python Implementation)

Aaj Andrew Ng course ka Model Representation lab bhi complete kiya.

### Lab Goal

Python mein Linear Regression model implement karna:

\[
f_{w,b}(x) = wx+b
\]

Is lab mein NumPy aur Matplotlib ka use kiya.

### Dataset

| House Size (1000 sqft) | Price (1000s of $) |
|---|---:|
| 1.0 | 300 |
| 2.0 | 500 |

```python
x_train = [1.0, 2.0]
y_train = [300, 500]
```

Total training examples:

```python
m = 2
```

### Model Function

```python
def compute_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)

    for i in range(m):
        f_wb[i] = w * x[i] + b

    return f_wb
```

Ye function har training example ke liye prediction calculate karta hai.

### Different Parameters Try Karna

**Case 1: `w = 100, b = 100`**

- Prediction line data se door thi.
- Isliye fit achha nahi tha.

**Case 2: `w = 200, b = 100`**

- Dono training points ke through line pass hoti hai.
- Is dataset ke liye perfect fit milta hai.

### 🔮 New Prediction

Agar house size `1.2` ho, yaani 1200 sqft:

\[
f(1.2) = 200(1.2)+100
\]

\[
f(1.2) = 340
\]

Result: **340 thousand dollars = $340,000**

### Lab Se Kya Samjha?

- Linear Regression function ko Python mein implement karna.
- NumPy arrays ke saath work karna.
- `w` aur `b` change karke predictions dekhna.
- Model ki line training data par kaise fit hoti hai, ye samajhna.

---

## 📚 6. Day 81 Quick Revision

| Topic | Main Learning |
|---|---|
| NumPy Array Properties | `.shape`, `.ndim`, `.size`, `.dtype` |
| Reshaping | `reshape()`, `flatten()`, `ravel()` |
| Transpose | `.T` |
| Linear Regression | House price prediction |
| Notation | `x`, `y`, `m`, `ŷ`, `f(x)` |
| Supervised Learning | Training data se prediction function learn karna |
| Linear Regression Formula | `f(x) = wx + b` |
| Cost Function | Model ki prediction error measure karna |
| Cost Function Intuition | Cost minimize karna |
| Model Representation Lab | Python mein Linear Regression implement karna |

---

## ⏳ 7. Pending Revision

Aaj Andrew Ng course ke kuch additional concepts aur notes bhi dekhe, lekin unka proper revision nahi kiya.

Isliye unhe aaj ke completed revision recap mein include nahi kiya. Kal un topics ko revise karne ka plan hai.

---

**Day 81 Completed!** 🚀

Aaj NumPy ke array operations aur Machine Learning ke Linear Regression fundamentals par kaam kiya. Ab focus concepts ko revise karne aur unki practical understanding strong karne par rahega.
