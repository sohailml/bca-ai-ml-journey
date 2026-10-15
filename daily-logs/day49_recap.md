# 🐍 AI/ML Journey — Day 49

> 🚀 Learn by Doing • Understand the Logic • Improve Every Day

📅 **Date:** 15 October 2026  
🎯 **Focus:** Advanced Python Dictionaries & Sets Practice

---

## 📌 Today's Progress

Today, I continued solving my **Day 4 Advanced Practice Set — Dictionaries & Sets**.

I solved questions **Q33 to Q48**, completing another 16 questions. While solving them, I came across a few concepts that were new to me, so I researched them and added my learnings to my Learning Notebook.

I couldn't do typing practice today, but I focused on Python problem-solving and understanding new concepts.

### ✅ Today's Checklist

- [x] Solved advanced practice questions Q33–Q48
- [x] Learned new concepts while solving problems
- [x] Updated the Learning Notebook with Learning 5–8
- [ ] Typing practice — not completed today
- [ ] Continue the remaining practice questions

---

## 🧠 Advanced Practice Set — Progress

| Detail | Progress |
|---|---|
| Topic | Python Dictionaries & Sets |
| Practice Set | Day 4 — Advanced |
| Questions Solved Today | 16 |
| Today's Questions | Q33–Q48 |
| Total Questions Solved | 48 |
| Questions Remaining | 52 |

**Progress: 48/100 questions completed — 48%**

<box gap={1}>
  <row align="center" justify="between">
    <text color="secondary" size="sm">Practice set completion</text>
    <text weight="medium" size="sm">48%</text>
  </row>
  <box background="surface-tertiary" radius="full" height="8px" clip>
    <box background="#16A34A" radius="full" height="8px" width="48%" />
  </box>
</box>

---

## 📚 Learning Notebook

These are the new concepts I learned while solving today's questions.

### 🔹 Learning 5 — Sets Are Unordered (Q42)

A Python set is an **unordered collection of unique elements**. This means the elements don't have a guaranteed position or fixed order, so we cannot access them using indexing like `my_set[0]`.

Sets automatically eliminate duplicate values, making them useful when we need to store unique items.

```python
students = {"Aman", "Riya", "Sohail", "Aman"}

print(students)
# Contains only unique names

# Indexing is not supported:
# print(students[0])  # TypeError
```

**Real-world example:** If I want to store unique student names without duplicates, I can use a set instead of a list.

**Key takeaway:** Use sets for uniqueness and membership checks, not when you need positional indexing or a guaranteed order.

### 🔹 Learning 6 — Set Elements Must Be Hashable (Q44)

Every element stored inside a set must be **hashable**.

Lists are mutable and unhashable, so they cannot be added directly to a set. Tuples can be added if all their elements are hashable.

```python
# A list cannot be a set element
# items = {[1, 2, 3]}  # TypeError

# A tuple of hashable elements can be a set element
items = {(1, 2), (3, 4)}

print(items)
```

However, a tuple containing an unhashable element, such as a list, cannot be added to a set either.

```python
# This also raises a TypeError:
# items = {(1, [2, 3])}
```

**Key takeaway:** A tuple is not automatically hashable just because it is immutable. Its contents must also be hashable.

### 🔹 Learning 7 — `discard()` Method (Q46)

The `discard()` method removes an element from a set if it exists. If the element is not present, it doesn't raise an error.

```python
numbers = {10, 20, 30, 40}

numbers.discard(20)
numbers.discard(100)

print(numbers)  # {10, 30, 40}
```

Here, `20` is removed, while trying to discard `100` does nothing because it isn't in the set.

**Key takeaway:** `discard()` is useful when an element may or may not exist in a set.

### 🔹 Learning 8 — Dictionary Comprehension (Q47)

I came across this expression:

```python
{word: len(word) for word in words}
```

This is an example of **dictionary comprehension**. It creates a new dictionary in a concise way.

- `for word in words` iterates over each word.
- `word` becomes the dictionary key.
- `len(word)` becomes the value associated with that key.

Example:

```python
words = ["python", "AI", "coding"]

word_lengths = {
    word: len(word)
    for word in words
}

print(word_lengths)
# {'python': 6, 'AI': 2, 'coding': 6}
```

**Key takeaway:** Dictionary comprehension is a concise way to build dictionaries from iterable data.

---

## ⌨️ Typing Practice

I couldn't complete typing practice today.

That's okay — one missed session doesn't erase previous progress. I'll aim to return to my regular routine tomorrow.

- 🎯 **Target Speed:** 80+ WPM
- ✅ **Target Accuracy:** 97%+
- 🔁 **Next Step:** Resume regular typing practice

---

## 📅 Plan for Day 50

Tomorrow, I'll continue with the remaining advanced practice questions.

- [ ] Start from Question 49
- [ ] Continue solving the Dictionaries & Sets practice set
- [ ] Record new concepts in the Learning Notebook
- [ ] Review confusing questions and mistakes
- [ ] Resume typing practice

The priority is to understand the logic behind each solution rather than rushing through the questions.

---

## 💭 Day 49 Reflection

Today, I solved 16 more questions and reached **48 out of 100** in my advanced practice set.

I also learned more about set behavior, hashability, the `discard()` method, and dictionary comprehension.

Some questions introduce concepts I haven't studied deeply before. Instead of skipping them, I'm researching those concepts and documenting what I learn.

This habit will help me build stronger fundamentals and make revision easier in the future.

> **Don't just solve the question. Understand the concept behind it.** 🚀

---

**Day 49 — Completed ✅**
