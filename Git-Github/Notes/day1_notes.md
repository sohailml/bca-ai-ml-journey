# 🐙 Git & GitHub Basics — Notes (Day 1)

> 🚀 Learning Git from Scratch  
> 📅 Topic: Version Control + Basic Commands  

---

## 📌 1. Git kya hai?

Git ek **Version Control System (VCS)** hai

👉 iska use hota hai:

- code ke changes track karne ke liye  
- team me kaam karne ke liye  
- purane version wapas lane ke liye  

👉 Git ko **Linus Torvalds** ne banaya

---

## 📌 2. Version Control System Types

### 🔹 Centralized VCS

- ek hi server hota hai  
- sab log usi pe depend hote hain  
- ❌ server down → sabka kaam band  

---

### 🔹 Distributed VCS (Git)

- har user ka apna copy hota hai  
- local + remote dono hote hain  
- ✅ safe + fast + flexible  

---

## 📌 3. Git vs GitHub

- **Git** → local tool  
- **GitHub** → online platform  

👉 GitHub pe hum apna code (repository) store karte hain

---

## 📌 4. Git Working Areas

### 🔹 1. Working Directory

👉 jaha actual files hoti hain  

### 🔹 2. Staging Area

👉 jaha selected changes ready hote hain commit ke liye  

---

## 📌 5. Important Commands

### 🔹 Check Version

```bash
git --version
```

---

### 🔹 Initialize Repository

```bash
git init
```

---

### 🔹 Set Username & Email

```bash
git config --global user.name "Your Name"
git config --global user.email "Your Email"
```

---

### 🔹 Check Status

```bash
git status
```

---

### 🔹 Add Files

```bash
git add filename
git add .
```

---

### 🔹 Commit Changes

```bash
git commit -m "Your message"
```

---

### 🔹 View History

```bash
git log
git log --oneline
```

---

### 🔹 Undo Staging

```bash
git restore --staged filename
```

---

## 📌 6. Summary

- Git → version control system  
- GitHub → code hosting platform  
- Working → Staging → Commit flow  
- Commands → project manage karne ke liye use hote hain  

---

# 🔥 #BuildInPublic 🚀
