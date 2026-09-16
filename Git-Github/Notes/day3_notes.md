# 🐙 Git & GitHub — Day 3

> 🚀 Continuing my Git/GitHub Journey  
> 📅 Day 3 — Merge Conflict, Stashing, Tags & Rebase

---

## 📌 1. Creating & Switching Branch (Shortcut)

```bash
git switch -c branch_name
```

👉 Ye command **new branch create + switch** dono ka kaam ek sath karta hai  
👉 Same as:
```bash
git branch branch_name
git switch branch_name
```

---

## 📌 2. Merge Conflict

### ❓ Merge Conflict kya hota hai?

👉 Jab **same file ko 2 branches me edit kiya jata hai**  
👉 Aur phir unhe merge karte time conflict aa jata hai

### ⚠️ Example Situation:

* `main` branch → file edit
* `ui` branch → same file edit  
👉 Ab jab merge karenge → conflict ❌

---

### 🛠️ Solve kaise kare?

👉 File open karo → waha kuch aisa dikhega:

```text
<<<<<<< HEAD
main branch code
=======
ui branch code
>>>>>>> ui
```

👉 Ab decide karo:
- kya rakhna hai ✅
- kya delete karna hai ❌

👉 Fix karne ke baad:

```bash
git add .
git commit
```

---

## 📌 3. Git Stash

### ❓ Stashing kya hota hai?

👉 Temporary storage for your changes  
👉 Jab kaam incomplete ho aur turant dusra kaam karna ho

---

### 💡 Use Case:

👉 Tum kaam kar rahe ho  
👉 Suddenly urgent task aa gaya 😵  
👉 Code incomplete hai

👉 Solution:

```bash
git stash
```

---

### 📦 Important Commands

```bash
git stash list     # stash list dekhne ke liye
git stash pop      # stash wapas lane ke liye (remove ho jayega)
git stash apply    # stash apply karega but delete nahi karega
```

---

## 📌 4. Git Tags

### ❓ Tag kya hota hai?

👉 Commit ko **label dena** (versioning ke liye)

---

### 🔹 Types of Tags

#### 1. Annotated Tag (recommended)

```bash
git tag -a v1.0 -m "First version"
```

👉 Isme message + details hoti hain

---

#### 2. Lightweight Tag

```bash
git tag v2.0
```

👉 Simple tag, koi extra info nahi

---

### 📋 Check Tags

```bash
git tag
```

---

## 📌 5. Git Rebase

### ❓ Rebase kya hota hai?

👉 Branch history ko clean banane ke liye use hota hai  
👉 Merge commit avoid karta hai

---

### 🔥 Difference:

👉 Merge:
- extra commit banata hai ❌

👉 Rebase:
- direct linear history banata hai ✅

---

### 🛠️ Command

```bash
git rebase main
```

👉 Current branch ke commits → main ke upar shift ho jate hain

---

### ⚠️ Agar error aaye:

```bash
git rebase --continue   # continue after fix
git rebase --skip       # skip commit
git rebase --abort      # cancel rebase
```

---

## 📌 6. Useful Commands

```bash
git log --oneline -5   # last 5 commits
```

```bash
touch file.txt         # new file create
```

---

## 🧠 Extra Understanding (Important)

👉 Rebase history ko clean banata hai  
👉 But team projects me carefully use karo ⚠️  
👉 Public branch pe rebase avoid karte hain

---

## 🚀 Summary

* `git switch -c` → create + switch branch
* Merge conflict → same file edit hone par
* Stash → temporary save
* Tags → version naming
* Rebase → clean history

---

🔥 Learning Source: CodeWithHarry (YouTube)  
⌨️ Typing Practice: ~30 mins (consistency 🔥)

---

# 🔥 #BuildInPublic
