# 🚀 Day 84 — AI/ML Learning Journey

📅 **Date:** 19 November 2026  
🎯 **Main Focus:** Andrew Ng Machine Learning — Day 6 + Week 1 Completion  
📚 **Learning Source:** Andrew Ng — Supervised Machine Learning: Regression and Classification  
💻 **Notebook:** `andrew-ng/day04.ipynb` (Day 5 Practice) | `andrew-ng/day05.ipynb` (Day 6 Learning)

---

## 📖 1. Previous Learning — Day 5 Practice

Aaj sabse pehle kal ke Gradient Descent concepts ki practical practice ki.

Previous day mein jo concepts seekhe the, unhe code aur implementation ke through revise kiya.

Main focus tha:

- Gradient Descent ka working mechanism.
- Cost Function aur uske derivatives.
- Learning Rate ka effect.
- `w` aur `b` ka simultaneous update.
- Gradient Descent ke through minimum Cost Function find karna.

Is practice ka purpose sirf formulas yaad karna nahi, balki algorithm ka actual working samajhna tha.

---

## 🤖 2. Andrew Ng — Day 6: Derivatives for Gradient Descent

Aaj course mein Gradient Descent ke liye derivatives calculate karna seekha.

Linear Regression ka Cost Function:

\[
J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}
(f_{w,b}(x^{(i)})-y^{(i)})^2
\]

Gradient Descent ko parameters update karne ke liye Cost Function ke derivatives ki zaroorat hoti hai.

### 📐 1. Derivative Formulas

**Derivative with respect to weight (`w`):**

\[
\frac{\partial J(w,b)}{\partial w}
=
\frac{1}{m}\sum_{i=1}^{m}
(f_{w,b}(x^{(i)})-y^{(i)})x^{(i)}
\]

**Derivative with respect to bias (`b`):**

\[
\frac{\partial J(w,b)}{\partial b}
=
\frac{1}{m}\sum_{i=1}^{m}
(f_{w,b}(x^{(i)})-y^{(i)})
\]

Yahan:

\[
Error = Prediction - Actual
\]

### 🔍 2. Difference Between Both Derivatives

Dono derivatives mein ek important difference hai:

- `w` ke derivative mein Error ko `x` se multiply karte hain.
- `b` ke derivative mein sirf Error use hota hai.

**Aisa kyun?**

Linear Regression model:

\[
f_{w,b}(x)=wx+b
\]

- `w`, input `x` ke saath multiply hota hai.
- `b` directly add hota hai.

Isi wajah se weight derivative mein `x` ka factor aata hai, jabki bias derivative mein nahi.

### 🧮 3. Calculus Behind the Formula

Derivative derive karne ke liye mainly do calculus rules use hote hain:

- Chain Rule
- Power Rule

Power Rule ki wajah se squared error differentiate karne par `2` aata hai.

Cost Function mein pehle se `1/2` present hota hai, isliye derivative mein ye 2 cancel ho jaata hai.

**Why 1/2 in Cost Function?**

\[
\frac{1}{2}\times 2=1
\]

Isse derivative ka formula cleaner ho jaata hai. `1/2` hone ya na hone se minimum point change nahi hota.

Full calculus derivation optional hai, lekin formulas aur unka meaning samajhna important hai.

### 🧪 4. Three Numerical Examples

Aaj teen different parameter combinations ke through derivatives aur Gradient Descent ko verify kiya.

| Case | Weight (`w`) | Bias (`b`) | Purpose |
|---|---:|---:|---|
| Case 1 | 100 | 100 | Poor fit |
| Case 2 | 200 | 100 | Perfect fit |
| Case 3 | 0 | 0 | Zero initialization |

In examples ko code ke through verify kiya aur samjha ki different starting parameters Cost Function aur gradients ko kaise affect karte hain.

### 🔄 5. Simultaneous Update

Gradient Descent mein dono derivatives purane `w` aur `b` values se calculate hone chahiye.

Uske baad dono parameters simultaneously update karne hain.

```python
temp_w = w - alpha * dj_dw
temp_b = b - alpha * dj_db

w = temp_w
b = temp_b
```

Isse dono updates same iteration ke original parameter values par based rehte hain.

### 🥣 6. Convexity

Linear Regression ka squared-error Cost Function convex bowl shape hota hai.

Iska important property:

- Ismein ek Global Minimum hota hai.
- Multiple competing local minima nahi hote.
- Gradient Descent suitable conditions mein Global Minimum tak converge kar sakta hai.

---

## 📉 3. Gradient Descent in Action — Batch Gradient Descent

Is lecture mein Gradient Descent ko actual example ke through run karke dekha.

### 🎬 1. Live Demonstration

Starting parameters:

```python
w = -0.1
b = 900
```

Starting point se Gradient Descent repeatedly parameters update karta hai.

Har iteration mein:

1. Predictions calculate hoti hain.
2. Cost Function calculate hota hai.
3. Derivatives calculate hote hain.
4. `w` aur `b` update hote hain.
5. Cost gradually decrease hoti hai.

Eventually model ki prediction line training data ke saath better fit hone lagti hai.

### 🏠 2. Final Prediction

Demo ke end mein 1250 sqft house ke liye approximate prediction:

\[
\text{Predicted Price} \approx \$250,000
\]

Ye model ke learned parameters se generate hui prediction thi.

### 📚 3. Batch Gradient Descent

**Batch Gradient Descent** mein har iteration ke andar complete training dataset ke saare examples use hote hain.

Mathematically:

\[
\sum_{i=1}^{m}
\]

Matlab har update se pehle saare `m` training examples ka contribution calculate hota hai.

**Key Points:**

- Har iteration mein complete training dataset use hota hai.
- Cost aur gradients all training examples par calculate hote hain.
- Ye Linear Regression ke Gradient Descent implementation ka standard approach hai.

### ⚖️ 4. Batch vs Mini-batch vs Stochastic Gradient Descent

| Type | Data Used Per Update |
|---|---|
| Batch Gradient Descent | Complete training dataset |
| Mini-batch Gradient Descent | Small batch of training examples |
| Stochastic Gradient Descent | One training example |

In teeno approaches ka main difference ye hai ki har parameter update ke liye kitne training examples use hote hain.

---

## 💻 4. Practical Lab — Three Important Functions

Aaj ke practical lab mein Gradient Descent implementation ke liye 3 important functions cover kiye.

### 1. `compute_cost()`

Is function ka kaam Cost Function calculate karna hai.

\[
J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}
(f_{w,b}(x^{(i)})-y^{(i)})^2
\]

Ye model ki total prediction error measure karta hai.

### 2. `compute_gradient()`

Is function ka kaam weight aur bias ke derivatives calculate karna hai.

\[
dj\_dw=\frac{1}{m}\sum Error \times x
\]

\[
dj\_db=\frac{1}{m}\sum Error
\]

Ye batata hai ki parameters ko kis direction mein update karna chahiye.

### 3. `gradient_descent()`

Ye main optimization function hai.

Iska workflow:

1. Current `w` aur `b` se gradients calculate karna.
2. Dono parameters simultaneously update karna.
3. Cost history save karna.
4. Repeated iterations execute karna.
5. Final optimized parameters return karna.

### 🔁 Complete Workflow

```text
Training Data
     |
     v
 compute_cost()
     |
     v
 compute_gradient()
     |
     v
 Update w and b
     |
     v
 Save Cost History
     |
     v
 Repeat Iterations
     |
     v
 Optimized Parameters
```

### ✨ Automatic Braking

Ek important observation ye thi ki fixed Learning Rate hone ke baad bhi minimum ke paas steps automatically chhote ho jaate hain.

**Reason:** Minimum ke paas derivative ki value zero ke close hoti jaati hai.

Isliye parameter updates bhi chhote ho jaate hain.

Learning Rate fixed hai, lekin derivative change hota rehta hai.

---

## ⚠️ 5. Learning Rate Experiment — Divergence

Aaj ek important experiment bhi dekha:

```python
alpha = 0.8
```

Is example mein Learning Rate bahut large tha.

**Result:**

- Parameter updates bahut bade ho gaye.
- Cost increase hone lagi.
- Weight `w` oscillate karne laga.
- Algorithm minimum ke paas converge karne ke bajaye usse door jaane laga.

Is process ko **Divergence** kehte hain.

### Convergence vs Divergence

| Convergence | Divergence |
|---|---|
| Cost decrease hoti hai | Cost increase ya unstable hoti hai |
| Parameters minimum ki taraf move karte hain | Parameters minimum se door ja sakte hain |
| Suitable Learning Rate | Learning Rate bahut large ho sakta hai |

---

## 📊 6. Four Visualizations

Aaj Gradient Descent ko visualize karne ke liye 4 important visualizations cover kiye.

### 1. Cost vs Iteration

- X-axis → Iterations
- Y-axis → Cost
- Is graph se pata chalta hai ki iterations ke saath Cost Function kaise decrease hota hai.
- Log scale par cost ki changes ko visualize karna easier hota hai.

### 2. Contour Plot + Gradient Descent Path

Contour Plot par Gradient Descent ka path show hota hai.

- Starting point se algorithm start hota hai.
- Har iteration mein parameters update hote hain.
- Path minimum point ki taraf move karta hai.

### 3. Divergence Demonstration

Large Learning Rate (`α = 0.8`) use karne par algorithm ka unstable behaviour visualize kiya.

### 4. ASCII Convergence Plot

Text-based graph ke through bhi Cost Function ki decreasing trend ko understand kiya.

---

## 🎉 7. Week 1 Completion — Andrew Ng Course

Aaj ke lectures aur practical lab complete karne ke baad Andrew Ng ke Machine Learning course ka **Week 1 complete** ho gaya!

Week 1 mein cover kiye gaye major topics:

- Introduction to Machine Learning
- Supervised Learning
- Unsupervised Learning
- Regression
- Classification
- Linear Regression
- Model Representation
- Cost Function
- Cost Function Visualization
- Gradient Descent
- Derivatives for Gradient Descent
- Batch Gradient Descent
- Practical Python Labs

Ye first week Machine Learning ke fundamentals samajhne ke liye important foundation raha.

## 🔭 8. Next Week Preview

Course ke next week mein ye topics aane wale hain:

- Multiple Features
- Non-linear Curves
- Practical Tips for Machine Learning

---

## 📊 9. Day 84 Progress Summary

| Task | Status |
|---|---|
| Day 5 Gradient Descent Practice | ✅ Completed |
| Derivatives for Gradient Descent | ✅ Completed |
| Gradient Descent in Action | ✅ Completed |
| Batch Gradient Descent | ✅ Completed |
| Three Practical Functions | ✅ Completed |
| Four Visualizations | ✅ Covered |
| Andrew Ng Week 1 | 🎉 Completed |
| NumPy Day 6 | ⏸️ Not Continued |

---

**Day 84 Completed!** 🚀

Aaj Andrew Ng course ka first week successfully complete kiya. Ab Linear Regression, Cost Function aur Gradient Descent ke fundamentals ke saath practical implementation ka bhi experience hai.

Kal se next learning session mein aage badhenge.
