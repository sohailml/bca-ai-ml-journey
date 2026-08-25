# 🐍 Python Basics — Day 2 Notes

---

📌 Continuing my AI/ML Journey  
📅 Day 2 — Strings & Conditional Statements

---

## 📌 1. Strings in Python

Python me string ka use text (words / sentence / characters) store karne ke liye hota hai.

```python
str1 = 'sohail'
str2 = "sohail"
str3 = """sohail"""

👉 Jo bhi text quotes (" " ya ' ' ya """ """) ke andar hota hai, wo string hota hai.
---
###🔹 Types of Quotes
Single quotes → ' '
Double quotes → " "
Triple quotes → """ """
###❓ Why Double / Triple Quotes?

Agar string ke andar apostrophe (') use karna ho to error aata hai.

str = "I'm Sohail"  # ✅ Correct

👉 Isliye double ya triple quotes use karte hain.

##📌 2. Escape Characters

Special formatting ke liye use hote hain:

print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab space

👉 \n → next line
👉 \t → tab space

##📌 3. String Concatenation

Concatenation ka matlab hota hai strings ko jodna.

str1 = "Sohail"
str2 = "Ansari"

print(str1 + str2)        # SohailAnsari
print(str1 + " " + str2)  # Sohail Ansari

👉 Space automatically nahi aata, manually " " dena padta hai.

##📌 4. Length of String

len() function se string ki length pata karte hain.

str = "sohail"
print(len(str))   # 6

str1 = "soh ail"
print(len(str1))  # 7 (space bhi count hota hai)
##📌 5. Indexing in String

String ke har character ka index hota hai (0 se start hota hai).

str = "sohail"

print(str[0])   # s
print(str[2])   # h
###🔹 Negative Indexing

Piche se count hota hai:

print(str[-1])  # l
print(str[-6])  # s
##📌 6. String Slicing

String ka ek part nikalne ke liye use hota hai.

str = "sohail"

print(str[0:3])  # soh
print(str[:3])   # soh
print(str[1:])   # ohail

👉 Last index include nahi hota
👉 Default start = 0
👉 Default end = len(str)

###🔹 Negative Slicing
print(str[-6:-3])  # soh
##📌 7. String Functions
###🔹 endswith()

Check karta hai string kis value pe end ho rahi hai:

str = "sohail"
print(str.endswith("l"))  # True
###🔹 capitalize()

First character capital kar deta hai:

str = "sohail"
print(str.capitalize())  # Sohail
###🔹 replace()

Kisi word ko replace karta hai:

str = "i am learning html"
print(str.replace("html", "python"))
# i am learning python
###🔹 find()

First occurrence ka index batata hai:

str = "sohail is learning"

print(str.find("l"))        # 5
print(str.find("learning")) # 10
print(str.find("xyz"))      # -1

👉 Agar value nahi mile to -1 return karta hai.

###🔹 count()

Kitni baar value aayi hai:

str = "arbaaz"
print(str.count("a"))  # 3
##📌 8. Conditional Statements

Condition ke basis pe decision lene ke liye use hota hai.

###🔹 if - elif - else
age = 24

if (age >= 18):
    print("can vote")

elif (age == 17):
    print("can apply")

else:
    print("can not vote")

👉 if → har baar check hota hai
👉 elif → tab chalega jab upar false ho
👉 else → jab sab false ho

##📌 9. Nesting in If

If ke andar ek aur if use karna:

a = 20

if (a > 0):
    if (a % 2 == 0):
        print("a is positive and even")
    else:
        print("a is positive and odd")

elif (a == 0):
    print("a is 0")

else:
    print("a is negative")

👉 Output: a is positive and even

🔥 Day 2 Complete
🚀 Consistency = Real Growth
#BuildInPublic
