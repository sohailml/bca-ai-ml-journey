# 🐙 Git & GitHub Basics — Day 2

> 🚀 Continuing my Version Control Journey  
> 📅 Day 2 — .gitignore, Branching & Workflow

---

## 📌 1. Ignoring Files (.gitignore)

Kabhi-kabhi project me kuch files ya folders hote hain jo hum GitHub par upload nahi karna chahte.

👉 Jaise:
- Temporary files
- API keys / secrets
- node_modules (web projects me)
- system files

Iske liye hum `.gitignore` file ka use karte hain.

### 🔹 Example

```bash
node_modules/
.env
*.log
```

👉 Jo bhi file/folder `.gitignore` me likh dete hain, Git unhe track nahi karta.

---

## 📌 2. Tracking Empty Folders (.gitkeep)

Git by default **empty folders ko track nahi karta** ❌

👉 Agar hume empty folder ko repo me rakhna ho, to uske andar ek file bana dete hain:

```
.gitkeep
```

👉 Isse Git us folder ko track karne lagta hai ✅

---

## 📌 3. Branching in Git

Branching Git ka ek powerful feature hai 🔥

👉 Iska use tab hota hai jab:
- Hum main code ko disturb nahi karna chahte
- New feature ya experiment karna ho

👉 Branch ek **separate copy** hoti hai project ki

---

### 🔹 Default Branch

- Git (local) → `master`
- GitHub → `main`

---

## 📌 4. Create a New Branch

```bash
git branch ui
```

👉 Ye `ui` naam ki new branch create karega

---

## 📌 5. Check All Branches

```bash
git branch
```

👉 Ye sabhi available branches dikha deta hai

---

## 📌 6. Switch Between Branches

```bash
git switch ui
```

👉 Isse hum ek branch se dusri branch par switch kar sakte hain

---

## 📌 7. Merge Branch

Jab hum apna kaam complete kar lete hain, to us branch ko main branch me merge kar dete hain

```bash
git merge ui
```

👉 Isse `ui` branch ka code main branch me add ho jayega

---

## 📌 8. Deleting Branch

Jab hum apna kaam complete kar lete hain, and hame vo purani branch delete karni ho to us branch ko delete kiya ja sakta hai

```bash
git branch -d ui
```

👉 Isse `ui` branch delete ho jayega

---

## 📌 9. Why Branching is Important 🤔

👉 Safe development (main code safe rehta hai)  
👉 Multiple features ek sath develop kar sakte hain  
👉 Team work me useful hota hai  

---

## 📌 10. Practice & Workflow

👉 Aaj maine:
- `.gitignore` use karna seekha  
- `.gitkeep` ka concept samjha  
- Branching create, switch aur merge ki practice ki  
- Typing practice bhi ki  

👉 Jo bhi files create ki aur commands run kiye:
➡️ Sab project ke folder me available hain

---

## 📌 11. What’s Next 🚀

👉 Next topics:
- Merge Conflicts  
- Stashing  
- Tags  
- Rebase  

---

# 🚀 Summary

* `.gitignore` → unwanted files ko ignore karta hai  
* `.gitkeep` → empty folder track karne ke liye  
* Branching → safe development ke liye  
* `git branch` → branch create/check  
* `git switch` → branch change  
* `git merge` → branch combine  

---

# 🔥 #BuildInPublic
