# 🚀 Day 62 — AI/ML Learning Journey

📅 **Day:** 62  
🎯 **Main Focus:** Python Practice — Dictionaries & Sets  
💻 **Practice Set:** Day 4 — Advanced Questions

---

## 📌 Today's Progress

Aaj learning journey mein zyada kuch nahi kiya, lekin Python practice set par kaam continue rakha.

- ✅ Solved **15 questions (Q58–Q72)**
- ✅ Learned about shallow copy and deep copy
- ✅ Learned the difference between `set` and `frozenset`
- 📝 Documented the important concepts learned while solving questions

### 📊 Practice Set Progress

| Metric | Progress |
|---|---:|
| Total Questions | 100 |
| Previously Completed | 57 |
| Today's Questions | 15 |
| **Total Completed** | **72/100** |
| Remaining Questions | 28 |
| Completion | 72% |

---

## 🧠 Learning Notebook

### 🔹 Learning 10 — Shallow Copy vs Deep Copy (Q66)

**Shallow Copy:**
- Creates a new outer container.
- Nested objects can still be shared between the original and copied containers.
- Changes to shared nested objects may affect both containers.

**Deep Copy:**
- Creates an independent copy of the objects inside the container as well.
- Nested objects are copied recursively, so changes to them generally do not affect the original.

**Important Note:** Simple sets containing only integers usually show the same observable behaviour with shallow and deep copies because integers are immutable and sets cannot directly contain nested sets. The difference becomes more relevant when working with nested mutable objects inside containers such as lists and dictionaries.

### 🔹 Learning 11 — `set` vs `frozenset` (Q67)

Both `set` and `frozenset` store unique elements, but the main difference is mutability.

| Feature | `set` | `frozenset` |
|---|---|---|
| Mutable | Yes | No |
| Add/remove elements | Allowed | Not allowed |
| Stores unique elements | Yes | Yes |
| Can be a dictionary key | No | Yes, if its elements satisfy hashability requirements |
| Can be an element of another set | No | Yes, if hashable |

**Example:**

```python
numbers = {1, 2, 3}
numbers.add(4)

print(numbers)
# {1, 2, 3, 4}
```

A `frozenset` cannot be modified after creation:

```python
numbers = frozenset({1, 2, 3})

print(numbers)
# frozenset({1, 2, 3})
```

**Key Takeaway:** Use a regular `set` when you need to add or remove elements. Use a `frozenset` when you need an immutable set that can also be used as a dictionary key or as an element of another set.

---

## 🎯 Today's Summary

Aaj ka session mainly Python problem-solving par focused tha. Q58 se Q72 tak solve kiye aur questions ke through concepts ko samajhne ke saath important learnings bhi document ki.

Progress ab **72% complete** ho chuki hai. Ab practice set ke sirf **28 questions remaining** hain.

## 📅 Next Session Plan

- [ ] Continue the Python practice set from **Q73**
- [ ] Focus on understanding the logic behind each question
- [ ] Document any new concepts or mistakes in the Learning Notebook
- [ ] Work towards completing the remaining 28 questions

---

**Day 62 Status:** Consistent progress — 15 questions solved! 🚀
