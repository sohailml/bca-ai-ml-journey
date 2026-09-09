# 🐍 Python Basics — Day 10

> 🚀 Continuing my AI/ML Journey  
> 📅 Day 10 — File Handling (File I/O)

---

## 📌 1. File I/O in Python

Aaj maine **File Input/Output (File I/O)** ke bare me padha.

👉 Python ki help se hum files ko **read aur write** kar sakte hain  

---

## 📌 2. Types of Files

### 🔹 Text Files

👉 Jo data readable form me hota hai  

Examples:  
`.txt`, `.docx`, `.log`

---

### 🔹 Binary Files

👉 Jo data readable text form me nahi hota  

Examples:  
`.png`, `.jpeg`, `.mp4`, `.mov`

---

## 📌 3. Opening a File

File ko open karne ka syntax:

```python
f = open("filename", "mode")
```

Example:

```python
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()
```

👉 `filename` → kaunsi file open karni hai  
👉 `mode` → kya operation karna hai (read/write)

---

## 📌 4. File Modes

Python me mainly 6 modes hote hain:

```
r, w, a, r+, w+, a+
```

---

### 🔹 `r` (Read)

👉 Sirf file read karne ke liye  
👉 Pointer end tak chala jata hai  

---

### 🔹 `w` (Write)

👉 File me likhne ke liye  
👉 Purana data **delete (truncate)** ho jata hai  
👉 File exist nahi karti to new file create ho jati hai  
👉 Pointer start par hota hai  

---

### 🔹 `a` (Append)

👉 File me data add karta hai (end me)  
👉 Purana data delete nahi hota  

---

### 🔹 `r+` (Read + Write)

👉 Read aur write dono kar sakte hain  
👉 Data delete nahi hota (overwrite hota hai starting se)  

---

### 🔹 `w+` (Write + Read)

👉 Read aur write dono  
👉 Purana data delete ho jata hai  
👉 Write ke baad read karoge to blank mil sakta hai  

---

### 🔹 `a+` (Append + Read)

👉 Read aur write dono  
👉 Data delete nahi hota  
👉 End me add hota hai  

---

## 📌 5. Reading Methods

```python
f.read()       # Puri file read karta hai
f.readline()   # Ek line read karta hai
```

---

## 📌 6. Using `with` (Best Practice ✅)

`with` use karne se file automatically close ho jati hai.

```python
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
```

👉 `f.close()` manually likhne ki zarurat nahi hoti  

---

## 📌 7. Deleting a File

File delete karne ke liye **os module** use hota hai:

```python
import os

os.remove("demo.txt")
```

👉 `os` ek module hai (pre-written code) jo file operations me help karta hai  

---

## 📌 8. Practice Work

👉 Aaj maine File Handling par kuch practice questions solve kiye  

👉 Unke **solutions mere GitHub ke practice folder me available hain** ✅  

---

# 🚀 Summary

- File I/O → file read & write karna  
- Text vs Binary files → data type difference  
- `open()` → file open karta hai  
- Modes → r, w, a, r+, w+, a+  
- `with` → best practice (auto close)  
- `os.remove()` → file delete karta hai  

---

# 📈 Progress

- [x] Day 1 Completed ✅  
- [x] Day 2 Completed ✅  
- [x] Day 3 Completed ✅  
- [x] Day 4 Completed ✅  
- [x] Day 5 Completed ✅  
- [x] Day 6 Completed ✅  
- [x] Day 7 Completed ✅  
- [x] Day 8 Completed ✅
- [x] Day 9 Completed ✅
- [x] Day 10 Completed ✅  
- [ ] Day 11 Coming Soon 🚀  

---

# 🔥 #BuildInPublic
