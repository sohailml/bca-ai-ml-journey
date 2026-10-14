# 🐍 AI/ML Journey — Day 48

> 🚀 Learn by Doing • Practice with Purpose • Improve Every Day

📅 **Date:** 14 October 2026  
🎯 **Focus:** Advanced Python Dictionaries & Sets Practice

---

## 📌 Today's Progress

Day 48 was focused on solving the advanced practice set for **Python Day 4 — Dictionaries & Sets**.

Today, I solved **32 questions**, from Question 1 to Question 32, and learned several important Python concepts along the way.

Instead of just solving questions, I also maintained a **Learning Notebook** to record new concepts and understand the reasoning behind them.

### ✅ Today's Checklist

- [x] Revised Python Dictionaries & Sets concepts
- [x] Solved advanced practice questions Q1–Q32
- [x] Documented new learnings in my Learning Notebook
- [x] Practiced typing
- [ ] Continue the remaining practice questions

---

## 🧠 Advanced Practice Set — Progress

| Detail | Progress |
|---|---|
| Topic | Dictionaries & Sets |
| Practice Set | Day 4 — Advanced |
| Questions Solved | 32 |
| Questions Completed | Q1–Q32 |
| Main Focus | Logic, concepts & problem-solving |

I'm gradually improving my understanding of Python by solving more challenging questions and learning from the concepts behind each solution.

---

## 📚 Learning Notebook

These are some of the important concepts I learned while solving today's questions.

### 🔹 Learning 1 — Why Dictionary Keys Must Be Hashable (Q20)

Python dictionaries use **hashing** to locate keys efficiently. A key must be hashable, meaning its hash value must remain stable during its lifetime.

If a key's hash value could change after insertion, Python might not be able to locate it in the expected place.

That's why mutable types such as lists and dictionaries cannot be used directly as dictionary keys, while suitable immutable types such as strings and integers can.

```python
# Valid dictionary keys
data = {
    "name": "Sohail",
    101: "Python"
}

# Invalid: a list cannot be used as a dictionary key
# data = {[1, 2]: "value"}
```

**Key takeaway:** Dictionary keys must be hashable, not simply immutable in every case.

### 🔹 Learning 2 — `dict.get()` vs `dict["key"]` (Q21)

Both approaches can retrieve dictionary values, but they behave differently when a key doesn't exist.

```python
student = {"name": "Sohail"}

print(student.get("age"))  # None
print(student["age"])      # KeyError
```

- `dict.get(key)` returns `None` by default if the key is missing. You can also provide a custom default value.
- `dict[key]` raises a `KeyError` if the key doesn't exist.

**Key takeaway:** Use `.get()` when a missing key is expected and should be handled gracefully.

### 🔹 Learning 3 — Finding the Key with the Maximum Value (Q27)

I learned how `max()` works with the `key` parameter.

```python
marks = {
    "Aman": 75,
    "Riya": 92,
    "Karan": 84
}

top_student = max(marks, key=marks.get)

print(top_student)  # Riya
```

Here:

- `max()` finds the maximum item.
- `key=marks.get` tells Python to compare dictionary keys using their associated values.
- The result is the **key with the highest value**, not the maximum value itself.

**Key takeaway:** `max(dictionary, key=dictionary.get)` is useful for finding the key associated with the largest dictionary value.

### 🔹 Learning 4 — `symmetric_difference()` (Q30)

I learned about the `symmetric_difference()` set method.

It returns a new set containing elements that appear in either set, but **not in both**.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.symmetric_difference(b)

print(result)  # {1, 2, 5, 6}
```

The elements `3` and `4` are excluded because they appear in both sets.

**Key takeaway:** Symmetric difference finds the elements unique to either set.

---

## ⌨️ Typing Practice

I also practiced typing today to keep improving my speed and accuracy.

My long-term targets remain:

- 🎯 **Speed:** 80+ WPM
- ✅ **Accuracy:** 97%+
- 🔁 **Approach:** Consistent practice without sacrificing accuracy

---

## 📅 Plan for Day 49

Tomorrow, I'll continue working on the advanced Dictionaries & Sets practice set.

- [ ] Continue from Question 33
- [ ] Understand the logic behind each question
- [ ] Add new concepts to the Learning Notebook
- [ ] Review mistakes and confusing concepts
- [ ] Continue typing practice

The goal is to strengthen my fundamentals before moving on to more advanced Python topics.

---

## 💭 Day 48 Reflection

Today, I completed 32 advanced Python practice questions and documented four important learnings.

The biggest benefit of this practice is that I'm not only learning *how* to write Python code, but also understanding *why* it works.

Every question gives me another opportunity to improve my logic, strengthen my fundamentals, and become a better problem solver.

> **Understand the concept. Solve the problem. Record the lesson. Repeat.** 🚀

---

**Day 48 — Completed ✅**
