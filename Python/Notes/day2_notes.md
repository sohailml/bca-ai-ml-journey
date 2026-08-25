# 🐍 Python Basics — Day 2

> 🚀 Continuing my AI/ML Journey  
> 📅 Focus: **Strings & Conditional Statements**  
> 💡 Goal: Concepts clear + GitHub consistency

---

## 📖 What I Learned Today

- Strings in Python
- Escape Characters
- String Operations
- String Functions
- Conditional Statements (if-elif-else)
- Nested Conditions

---

## 🧵 1. Strings in Python

Strings ka use text (words / sentence) store karne ke liye hota hai.

```python
str1 = 'sohail'
str2 = "sohail"
str3 = """sohail"""
💡 Rule:
Jo bhi text quotes ke andar hota hai → wo string hota hai.
✨ Types of Quotes
Type
Example
Single
'hello'
Double
"hello"
Triple
"""hello"""
❓ Why Double / Triple Quotes?
Agar string ke andar ' (apostrophe) use karna ho:
str = "I'm Sohail"  # ✅ Correct
👉 Single quotes me error aata hai, isliye double/triple use karte hain.
🔤 2. Escape Characters
Formatting ke liye use hote hain:
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab space
Symbol
Meaning
\n
New Line
\t
Tab Space
🔗 3. String Concatenation
Strings ko jodna:
str1 = "Sohail"
str2 = "Ansari"

print(str1 + str2)        # SohailAnsari
print(str1 + " " + str2)  # Sohail Ansari
⚠️ Space manually dena padta hai.
📏 4. Length of String
str = "sohail"
print(len(str))   # 6

str1 = "soh ail"
print(len(str1))  # 7 (space bhi count hota hai)
🔍 5. Indexing
str = "sohail"

print(str[0])  # s
print(str[2])  # h
🔄 Negative Indexing
print(str[-1])  # l
print(str[-6])  # s
✂️ 6. String Slicing
str = "sohail"

print(str[0:3])  # soh
print(str[:3])   # soh
print(str[1:])   # ohail
💡 Last index include nahi hota.
⚙️ 7. String Functions
🔹 endswith()
str = "sohail"
print(str.endswith("l"))  # True
🔹 capitalize()
print("sohail".capitalize())  # Sohail
🔹 replace()
print("i am learning html".replace("html", "python"))
🔹 find()
str = "sohail is learning"

print(str.find("l"))        # 5
print(str.find("learning")) # 10
print(str.find("xyz"))      # -1
🔹 count()
print("arbaaz".count("a"))  # 3
🔀 8. Conditional Statements
age = 24

if (age >= 18):
    print("can vote")

elif (age == 17):
    print("can apply")

else:
    print("can not vote")
⚡ Logic
if → first check
elif → alternative condition
else → final fallback
🧠 9. Nested If
a = 20

if (a > 0):
    if (a % 2 == 0):
        print("positive and even")
    else:
        print("positive and odd")

elif (a == 0):
    print("zero")

else:
    print("negative")
🎯 Day 2 Summary
Strings strong ho gaye 💪
Basic operations clear 👍
Conditions samajh aa gayi 🧠
🚀 Progress Tracker
Day
Topic
Status
Day 1
Basics
✅ Done
Day 2
Strings + Conditions
✅ Done
Day 3
Loops
🔜 Next
🔥 Keep Going
Consistency > Motivation
Daily thoda bhi kar = big result 📈
#BuildInPublic 🚀