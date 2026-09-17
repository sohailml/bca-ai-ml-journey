# 🔧 Git & GitHub — Day 1

> 🚀 Start of my Git/GitHub Journey  
> 📅 Day 1 — Introduction & Basic Commands

---

## 📌 1. What is Git?

Git ek **Version Control System (VCS)** hai.

👉 Simple words me:
Git help karta hai track karne me ki **code me kya changes hue, kab hue, aur kisne kiye**

### 🤔 Why Git was Created?

Pehle problem kya thi:
- Code me changes track karna mushkil ❌  
- Team me kaun kya change kar raha hai → pata nahi ❌  
- Old version wapas lana difficult ❌  

👉 Is problem ko solve karne ke liye **Linus Torvalds** ne Git banaya.

---

## 📌 2. Types of Version Control System

### 🔹 Centralized VCS

- Ek hi central server hota hai
- Sab log usi server pe depend karte hain  
- Agar server down → sabka kaam ruk jata hai ❌

---

### 🔹 Distributed VCS (Git)

- Har developer ke paas **poora code (repo)** hota hai  
- Internet ke bina bhi kaam kar sakte ho ✅  
- Safe + fast + flexible  

👉 Git ek **Distributed VCS** hai (ye important hai 🔥)

---

## 📌 3. What is GitHub?

GitHub ek **online platform** hai jahan hum apna code store karte hain.

👉 Simple analogy:
- YouTube → videos store karta hai  
- GitHub → code (repositories) store karta hai  

👉 Git = tool (local machine pe)  
👉 GitHub = cloud storage (online)

---

## 📌 4. Git Workflow (How Git Works)

Git ka basic flow 3 steps me hota hai:

### 🔹 1. Working Directory
👉 Jaha tum code likhte ho (your project folder)

---

### 🔹 2. Staging Area
👉 Jaha tum files ko ready karte ho commit ke liye  
👉 (Matlab “ye changes save karne wale hain”)

---

### 🔹 3. Repository (Commit)
👉 Final save point  
👉 Yaha changes permanently store hote hain

---

## 📌 5. Basic Git Commands

### 🔹 Check Git Version

```bash
git --version
```

👉 Installed Git ka version batata hai

---

### 🔹 Initialize Git Repository

```bash
git init
```

👉 Folder ko Git repository bana deta hai  
👉 Hidden `.git` folder create hota hai

---

### 🔹 Set Username

```bash
git config --global user.name "Your Name"
```

👉 Ye naam har commit ke sath show hota hai

---

### 🔹 Set Email

```bash
git config --global user.email "your@email.com"
```

👉 Ye email bhi commit ke sath attach hoti hai

---

### 🔹 Check Status

```bash
git status
```

👉 Batata hai:
- Kaunsi files modified hain  
- Kaunsi staged hain  
- Kaunsi commit hui hain  

---

### 🔹 Add File to Staging Area

```bash
git add filename
```

👉 Specific file add karta hai

```bash
git add index.txt style.css
```

👉 Multiple files add

```bash
git add .
```

👉 Sab files ek sath add

---

### 🔹 Commit Changes

```bash
git commit -m "your message"
```

👉 Changes ko save karta hai with message

📌 Example:
```bash
git commit -m "Added login page"
```

---

### 🔹 View Commit History

```bash
git log
```

👉 Full history dikhata hai

```bash
git log --oneline
```

👉 Short history (one line per commit)

---

### 🔹 Remove File from Staging

```bash
git restore --staged filename
```

👉 Agar galti se file add ho gayi ho to use staging se hata sakte ho

---

## 📌 6. Important Concepts (Must Know)

### 🔸 Repository (Repo)
👉 Project ka folder jisme Git initialized ho

---

### 🔸 Commit
👉 Code ka snapshot (save point)

---

### 🔸 Staging Area
👉 Temporary area before commit

---

## 📌 7. Best Practices (🔥 Pro Tips)

- Har meaningful change ke baad commit karo  
- Clear message likho (e.g. "fixed bug", "added feature")  
- `git add .` use karne se pehle check karo (`git status`)  

---

## 📌 8. Learning Source

👉 Maine Git & GitHub **CodeWithHarry (YouTube)** se padha  

👉 Mere notes & practice:
- `git-github/notes` → detailed notes  
- `git-github/code` → commands & practice  

---

# 🚀 Summary

- Git → version control system  
- GitHub → code hosting platform  
- Git workflow → Working → Staging → Commit  
- Important commands → init, add, commit, status, log  

---

# 🔥 #BuildInPublic
