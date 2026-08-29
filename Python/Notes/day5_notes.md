# 🐍 Python Basics — Day 5

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 5 — Loops in Python

---

## 📌 1. While Loop

While loop tab tak chalta hai jab tak condition true hoti hai.

👉 Jab hame same kaam baar-baar karna ho (repetition), tab loop use karte hain  
👉 Ye manual repetition ko automatic bana deta hai  

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

👉 Output: `1` se `10` tak print hoga  
👉 `i` ko iterator kehte hain  
👉 Process ko iteration kehte hain  

---

## 📌 2. Practice Questions (While Loop)

```text
Q1: Print numbers from 1 to 100  
Q2: Print numbers from 100 to 1  
Q3: Print multiplication table of a number n  
Q4: Print elements of a list using a loop  
Q5: Search a number in a tuple using loop  
```

👉 In sabhi questions ke solutions mere GitHub ke **practice repo/folder** me available hain  

---

## 📌 3. Break & Continue

### ❌ break

Break statement loop ko turant stop kar deta hai  
Jahan condition true hoti hai, wahi loop khatam ho jata hai

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

---

### 🔁 continue

Continue statement current iteration ko skip karta hai  
Baaki loop normally chalta rehta hai

```python
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
```

---

## 📌 4. For Loop

For loop ka use sequence (list, tuple, string) ko traverse karne ke liye hota hai

```python
my_list = [1, 2, 4, 6, 9, 3, 5, 2]

for val in my_list:
    print(val)
```

👉 Har element ek-ek karke print hoga  

---

## 📌 5. For Loop with Else

Loop complete hone ke baad `else` block run hota hai

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

👉 Jab loop properly finish hota hai tab hi `else` chalega  

---

## 📌 6. Range Function

Range function numbers ka sequence generate karta hai

```python
for i in range(1, 11):
    print(i)
```

👉 `range(start, stop, step)`  
👉 Stop value include nahi hoti (1 kam hoti hai)  
👉 Default start = 0  
👉 Default step = 1  

---

### 🔹 Even Numbers Example

```python
for i in range(2, 101, 2):
    print(i)
```

👉 Even numbers print karega  

---

## 📌 7. Practice Questions (For Loop)

```text
Q6: Print elements of list using for loop  
Q7: Search number in tuple using for loop  
```

👉 Inke solutions bhi GitHub practice folder me available hain  

---

## 📌 8. Pass Statement

Pass statement empty block ke liye use hota hai  
Jab hum abhi code nahi likhna chahte lekin structure maintain karna hai

```python
for i in range(6):
    pass

if i > 5:
    pass

print("end")
```

👉 Ye error ko avoid karta hai  

---

## 📌 9. More Practice Questions

```text
Q8: Find sum of first n numbers (using while)  
Q9: Find factorial of n (using for loop)  
```

👉 In sabhi questions ke solutions mere GitHub ke practice repo me hain  

---

# 🚀 Summary

* While loop → condition based repetition  
* For loop → sequence traversal  
* Break → loop ko turant stop karta hai  
* Continue → iteration skip karta hai  
* Range → number sequence generate karta hai  
* Pass → empty block handle karta hai  

---

# 📈 Progress

* [x] Day 1 Completed ✅  
* [x] Day 2 Completed ✅  
* [x] Day 3 Completed ✅  
* [x] Day 4 Completed ✅  
* [x] Day 5 Completed ✅  
* [ ] Day 6 Coming Soon 🚀  

---

# 🔥 #BuildInPublic
