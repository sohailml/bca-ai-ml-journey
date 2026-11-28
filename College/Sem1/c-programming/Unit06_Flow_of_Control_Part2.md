# 🔄 C Programming - Unit 6: Flow of Control Part 2

> **Course:** BCA - Semester 1  
> **Topic:** Loops (while, do-while, for), Nesting, break & continue

---

## 📑 Table of Contents
1. [Introduction to Loops](#-1-introduction-to-loops)
2. [The `while` Loop (Entry-Controlled)](#-2-the-while-loop-entry-controlled)
3. [The `do-while` Loop (Exit-Controlled)](#-3-the-do-while-loop-exit-controlled)
4. [The `for` Loop (Fixed Iterations)](#-4-the-for-loop-fixed-iterations)
5. [Nesting of Loops](#-5-nesting-of-loops)
6. [The `break` Statement](#-6-the-break-statement)
7. [The `continue` Statement](#-7-the-continue-statement)
8. [Entry vs Exit Controlled Loops (Exam Important)](#-8-entry-vs-exit-controlled-loops-exam-important)
9. [Terminal Questions Solutions (PDF)](#-9-terminal-questions-solutions-pdf)
10. [Summary, Cheat Sheet & Q&A](#-10-summary-cheat-sheet--qa)

---

## 📌 1. Introduction to Loops

Loops ka use **repetitive tasks (baar-baar hone wale kaam)** ko automate karne ke liye hota hai. C mein 3 main loops hote hain:
1.  **`while`:** Jab iterations ki sankhya pata na ho (indefinite condition).
2.  **`for`:** Jab iterations ki sankhya pata ho (predetermined).
3.  **`do-while`:** Jab loop body kam se kam ek baar execute karni ho.

**Key Terms:**
*   **`break`:** Loop se poora bahar nikal jana.
*   **`continue`:** Current iteration skip karke next iteration par jana.

---

## 🔄 2. The `while` Loop (Entry-Controlled)

Ye sabse basic loop hai. Isme **condition pehle test hoti hai**, phir body execute hoti hai. Isliye ise **Entry-Controlled Loop** kehte hain.

**Syntax:**
```c
while (expression) {
    statement(s);
}
```

**Working:**
1.  Condition check hoti hai.
2.  Agar true hai, toh body execute hoti hai.
3.  Phir wapas condition check hoti hai.
4.  Agar condition false ho gayi, toh loop khatam.

> [!NOTE]
> **Boundary Condition:** Agar condition pehli baar mein hi false ho jaye, toh loop body **zero baar** execute hoti hai.

### Program 1: Doubling Numbers
```c
int x = 2;
while(x < 1000) {
    printf("%d\n", x);
    x = x * 2;
}
// Output: 2 4 8 16 32 64 128 256 512
```

### Program 2: Find Largest of N Numbers
```c
#include <stdio.h>
void main() {
    int num, large, n, i;
    printf("Enter number of numbers: ");
    scanf("%d", &n);
    large = 0;
    i = 0;
    while(i < n) {
        printf("\nEnter number: ");
        scanf("%d", &num);
        if(large < num)
            large = num;
        i++;
    }
    printf("\nLarge = %d", large);
}
```

### Program 3: Sine Series Evaluation
```c
#include <stdio.h>
#include <math.h>
void main() {
    int n, i=1, count;
    float acc, x, term, sum;
    printf("Enter the angle: ");
    scanf("%f", &x);
    x = x * 3.1416 / 180.0;
    printf("\nEnter the accuracy: ");
    scanf("%f", &acc);
    sum = x;
    term = x;
    while ((fabs(term)) > acc) {
        term = -term * x * x / ((2*i) * (2*i+1));
        sum += term;
        i++;
    }
    printf("\nSum of sine series is %f", sum);
}
```
*   **Explanation:** `fabs()` function absolute value deta hai. Loop tab tak chalta hai jab tak `term` ki value `acc` (accuracy) se badi hai.

---

## 🔄 3. The `do-while` Loop (Exit-Controlled)

Is loop mein **body pehle execute hoti hai**, phir condition test hoti hai. Isliye ise **Exit-Controlled Loop** kehte hain.

**Syntax:**
```c
do {
    statement(s);
} while (expression);
```

**Working:**
1.  Body execute hoti hai.
2.  Condition check hoti hai.
3.  Agar true, toh wapas body execute.
4.  Agar false, toh loop khatam.

> [!IMPORTANT]
> **Key Difference:** `do-while` loop ki body **kam se kam ek baar** zaroor execute hoti hai, chahe condition pehli baar mein hi false ho.

### Program 6.3: Multiplication Table (Nested do-while)
```c
void main() {
    int rowmax=10, colmax=10, row, col, x;
    printf("Multiplication table\n");
    printf("....................\n");
    row = 1;
    do {
        col = 1;
        do {
            x = row * col;
            printf("%4d", x);
            col = col + 1;
        } while (col <= colmax);
        printf("\n");
        row = row + 1;
    } while (row <= rowmax);
}
```
*   **Explanation:** Outer loop rows ke liye hai, inner loop columns ke liye. Har row ke liye 1 se 10 tak table print hota hai.

---

## 🔄 4. The `for` Loop (Fixed Iterations)

Jab humein pata ho ki loop kitni baar chalega, toh `for` loop use karte hain. Ye bhi **Entry-Controlled Loop** hai.

**Syntax:**
```c
for (expr1; expr2; expr3) {
    statement(s);
}
```
*   **`expr1` (Initialization):** Loop variable ko initialize karta hai (e.g., `i=0`).
*   **`expr2` (Condition):** Loop chalne ki condition (e.g., `i<10`).
*   **`expr3` (Update):** Har iteration ke baad variable ko update karta hai (e.g., `i=i+1`).

**Working Sequence:**
`expr1` → `expr2` (True) → Body → `expr3` → `expr2` (True) → Body → `expr3`... jab tak `expr2` false na ho jaye.

> [!TIP]
> **All expressions are optional:** `for(;;)` ek **infinite loop** banata hai.

### Program 3: Factorial of a Number
```c
#include <stdio.h>
void main() {
    int M, N;
    long int F = 1;
    printf("Enter the number: ");
    scanf("%d", &N);
    if(N <= 0)
        F = 1;
    else {
        for(M = 1; M <= N; M++)
            F *= M;
    }
    printf("The factorial of the number is %ld", F);
}
```

---

## 🔄 5. Nesting of Loops

Ek loop ke andar doosra loop. Outer loop jitni baar chalega, inner loop utni baar *poora* chalega.

**Example:**
```c
for(i = 1; i < 10; i++) {
    for(j = 1; j < 5; j++) {
        // Inner loop body
    }
}
```
*   **Total Iterations:** Outer (9 baar) * Inner (4 baar) = 36 iterations.

---

## 🛑 6. The `break` Statement

`break` statement loop (ya `switch`) se **turant bahar** nikal jata hai.

**Syntax:** `break;`

**Program 4: Break Illustration**
```c
void main() {
    int x;
    for (x = 1; x <= 10; x++) {
        if (x == 5)
            break; // x==5 hone par loop se bahar
        printf("%d", x);
    }
    printf("\nBroke out of loop at x = %d", x);
}
// Output: 1 2 3 4
// Broke out of loop at x = 5
```

> [!NOTE]
> **Nested Loops mein:** `break` sirf **inner loop** se bahar nikalta hai, outer loop nahi rukta.

---

## ⏭️ 7. The `continue` Statement

`continue` statement current iteration ke baaki code ko **skip** karke next iteration par chala jata hai.

**Syntax:** `continue;`

**Program 5: Continue Illustration**
```c
void main() {
    int x;
    for (x = 1; x <= 10; x++) {
        if (x == 5)
            continue; // x==5 par neeche ka printf skip
        printf("%d\n", x);
    }
}
// Output: 1 2 3 4 6 7 8 9 10 (5 skip ho gaya)
```

> [!WARNING]
> `continue` statement `switch` case mein use **nahi** hota (sirf loops mein).

---

## ⚖️ 8. Entry vs Exit Controlled Loops (Exam Important)

| Feature | Entry-Controlled Loop | Exit-Controlled Loop |
| :--- | :--- | :--- |
| **Loops** | `while`, `for` | `do-while` |
| **Condition Check** | Body execute hone se **pehle**. | Body execute hone ke **baad**. |
| **Minimum Executions** | 0 (zero) | 1 (at least once) |
| **Example** | `while (x < 10)` | `do { ... } while (x < 10);` |

---

## 🧠 9. Terminal Questions Solutions (PDF)

**Q1: Output of `while` loop?**
```c
int i=0, x=0;
while (i<20) {
    if (i%5 == 0) {
        x+=i;
        printf("%d\t", i);
    }
    i++;
}
printf("\nx=%d", x);
```
*   **Iterations:** `i=0, 5, 10, 15` (i%5==0 wale).
*   `x = 0 + 5 + 10 + 15 = 30`.
*   **Output:** `0 5 10 15 \n x=30`

**Q2: Output of `do-while` loop?**
```c
int i=0, x=0;
do {
    if (i%5 == 0) {
        x++;
        printf("%d\t", x);
    }
    ++i;
} while (i<20);
printf("\nx=%d", x);
```
*   **Iterations:** `i=0, 5, 10, 15`. Har baar `x++` hoga.
*   `x` ki value: 1, 2, 3, 4.
*   **Output:** `1 2 3 4 \n x=4`

---

## 📝 10. Summary, Cheat Sheet & Q&A

### 10.1 Summary
*   **`while`:** Entry-controlled, condition pehle.
*   **`do-while`:** Exit-controlled, body pehle, kam se kam ek baar.
*   **`for`:** Entry-controlled, fixed iterations (init; test; update).
*   **Nesting:** Loop inside loop.
*   **`break`:** Loop se bahar.
*   **`continue`:** Current iteration skip.

### 10.2 Cheat Sheet

```markdown
| Loop | Type | Condition Check | Min Runs |
|------|------|-----------------|----------|
| while | Entry | Before body | 0 |
| do-while | Exit | After body | 1 |
| for | Entry | Before body | 0 |

| Keyword | Purpose | Works in |
|---------|---------|----------|
| break | Exit loop/switch | loops, switch |
| continue | Skip to next iteration | loops only |
```

### 10.3 Self-Assessment Questions (PDF Answers)
1.  **A ____ loop starts out like an if statement.** `while`.
2.  **while is an entry-controlled loop. (True/False)** True.
3.  **On using the ____, the body of the loop is always executed at least once.** `do-while`.
4.  **do...while is an entry-controlled loop. (True/False)** False (Exit-controlled).
5.  **for loop is an exit-controlled loop. (True/False)** False (Entry-controlled).
6.  **The "control variable" of a for loop does not have to be an integer. (True/False)** True.

### 10.4 Extra Practice Questions (Exam Special)
1.  Write a program to print the sum of first 10 natural numbers using a `while` loop.
2.  Write a program to check if a number is prime using a `for` loop.
3.  What is an infinite loop? How can you create it using `for` and `while`?
4.  Predict the output:
    ```c
    int i = 0;
    while(i < 5) {
        printf("%d ", i);
        i += 2;
    }
    ```
    *Answer: `0 2 4`*
5.  Differentiate between `break` and `continue` with examples.

---
> **💡 Bhai ka Gyan:** Exam mein **Entry vs Exit Controlled Loops**, **`for` loop ka syntax**, aur **`break` vs `continue`** ke questions pakke aate hain. Terminal questions wale `while` aur `do-while` ke output predictions bhi practice kar lena. Nested loops ka execution count (outer * inner) samajh lo. All the best! 🚀
