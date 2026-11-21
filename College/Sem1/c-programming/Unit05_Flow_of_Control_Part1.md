# 🔀 C Programming - Unit 5: Flow of Control Part 1

> **Course:** BCA - Semester 1  
> **Topic:** goto, if, if-else, Nested if, Ternary Operator, switch-case

---

## 📑 Table of Contents
1. [Introduction to Flow of Control](#-1-introduction-to-flow-of-control)
2. [The `goto` Statement (Unconditional Branching)](#-2-the-goto-statement-unconditional-branching)
3. [The `if` Statement (Decision Making)](#-3-the-if-statement-decision-making)
4. [The `if-else` Statement (Two-Way Decision)](#-4-the-if-else-statement-two-way-decision)
5. [Nesting of `if` Statements (Multi-Path Decision)](#-5-nesting-of-if-statements-multi-path-decision)
6. [The Conditional (Ternary) Operator `?:`](#-6-the-conditional-ternary-operator-)
7. [The `switch` Statement (Multi-Way Decision)](#-7-the-switch-statement-multi-way-decision)
8. [`break` and `continue` (Extra Exam Topic)](#-8-break-and-continue-extra-exam-topic)
9. [Common Mistakes & Dangling Else Problem](#-9-common-mistakes--dangling-else-problem)
10. [Summary, Cheat Sheet & Q&A](#-10-summary-cheat-sheet--qa)

---

## 📌 1. Introduction to Flow of Control

Normal program execution mein statements **ek ke baad ek (sequentially)** execute hote hain. Lekin hum is flow ko change kar sakte hain **control flow constructs** use karke.

**C mein Decision Making Statements:**
1.  `if` statement
2.  `switch` statement
3.  `goto` statement
4.  Conditional Operator (`?:`)

**True/False in C:**
*   **False** = `0`
*   **True** = `Koi bhi non-zero value` (usually `1`)

**Objectives:**
*   Two-way aur multi-path decision lena.
*   Unconditional branching (`goto`) samajhna.
*   Conditional expressions evaluate karna.

---

## ↩️ 2. The `goto` Statement (Unconditional Branching)

`goto` statement program ko **unconditionally** ek point se dusre point par jump karne deta hai.

**Syntax:**
```c
goto label;
...
label:
    statement;
```

**Types of `goto` Jumps:**

| Type | Description | Example |
| :--- | :--- | :--- |
| **Forward Jump** | `goto` statement pehle, label baad mein. (Kuch statements skip ho jate hain) | `goto end; ... end: ...` |
| **Backward Jump** | Label pehle, `goto` baad mein. (Loop ban jata hai) | `read: ... goto read;` |

### Program 5.1: Unconditional Branching (Infinite Loop)
```c
#include <stdio.h>
#include <math.h>

int main() {
    double a, b;
    read:
    printf("Enter the value of a\n");
    scanf("%lf", &a);

    if (a < 0)
        goto read; // Negative number par dobara input

    b = sqrt(a);
    printf("%lf %lf \n", a, b);
    goto read; // Har baar wapas input par jata hai (Infinite Loop)
    return 0;
}
```

> [!WARNING]
> **Exam Important:** `goto` ka use structured programming mein avoid kiya jata hai kyunki isse program ka flow samajhna mushkil ho jata hai. Sirf specific situations mein (jaise nested loops se break karna) use karte hain.

---

## 🤔 3. The `if` Statement (Decision Making)

Sabse simple control flow statement. Ye condition true hone par hi code execute karta hai.

**Syntax:**
```c
if (expression)
    statement;
```

Agar ek se zyada statements execute karne hain, toh **curly braces `{}`** use karo:
```c
if (expression) {
    statement 1;
    statement 2;
    statement n;
}
```

### Program 5.2: Absolute Value of an Integer
```c
#include <stdio.h>
void main() {
    int number;
    printf("Type a number: ");
    scanf("%d", &number);

    if (number < 0)   // Check if negative
        number = -number; // Convert to positive

    printf("The absolute value is %d \n", number);
}
```

---

## ⚖️ 4. The `if-else` Statement (Two-Way Decision)

Condition true hone par **if block**, false hone par **else block** execute hota hai.

**Syntax:**
```c
if (expression)
    statement 1;
else
    statement 2;
```

*   Agar ek se zyada statements hain, toh `{}` use karo dono blocks mein.

### Program 5.3: Positive or Negative Number
```c
#include <stdio.h>
void main() {
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);

    if (num < 0)
        printf("The number is negative");
    else
        printf("The number is positive");
}
```

---

## 🎯 5. Nesting of `if` Statements (Multi-Path Decision)

Ek `if` statement ke andar doosra `if` statement. Isse multiple conditions check ki ja sakti hain.

### 5.1 Example: Quadrant Detection
```c
if (x > 0) {
    if (y > 0)
        printf("Northeast.\n");
    else
        printf("Southeast.\n");
}
else {
    if (y > 0)
        printf("Northwest.\n");
    else
        printf("Southwest.\n");
}
```

> [!TIP]
> **Indentation & Braces:** Nested if-else mein hamesha braces use karo aur proper indentation rakho, warna "dangling else" problem aa sakti hai.

### 5.2 Cascaded if-else if (Grade System)
```c
if (grade >= 90)
    printf("A");
else if (grade >= 80)
    printf("B");
else if (grade >= 70)
    printf("C");
else if (grade >= 60)
    printf("D");
else
    printf("F");
```
*   **Working:** Ye upar se neeche check karta hai. Jo pehli condition true hoti hai, wo execute hoti hai, baaki skip ho jati hain.

### Program 5.4: Largest of Three Numbers
```c
#include <stdio.h>
void main() {
    int a, b, c, big;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b) {
        if (a > c)
            big = a;
        else
            big = c;
    }
    else {
        if (b > c)
            big = b;
        else
            big = c;
    }
    printf("Largest of %d, %d & %d = %d", a, b, c, big);
}
```

---

## ❓ 6. The Conditional (Ternary) Operator `?:`

Ye **ternary operator** hai (3 operands). `if-else` ka short form.

**Syntax:**
```c
E1 ? E2 : E3
```
*   Agar `E1` true (non-zero) hai, toh `E2` evaluate hoga aur result banega.
*   Agar `E1` false (0) hai, toh `E3` evaluate hoga aur result banega.

**Associativity:** Right to left.

**Examples:**
```c
// Minimum of x and y
a = (x < y) ? x : y;

// Check odd/even
printf("%s", (num % 2 == 0) ? "Even" : "Odd");
```

> [!WARNING]
> **Exam Important:** Conditional operator **lvalue (assignable variable) nahi** produce karta. 
> `(a > b) ? a : b = 10;` **Invalid** hai.
> `a > b ? x : y = 10;` **Invalid** hai.

---

## 🎛️ 7. The `switch` Statement (Multi-Way Decision)

`switch` statement long `if-else` chains ka substitute hai. Ye ek variable ki value ko multiple **case** values se compare karta hai.

**Syntax:**
```c
switch (variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    ...
    default:
        // code
        break;
}
```

**Rules (Exam Important):**
1.  **`case` values constant integral expressions** honi chahiye. Variables allowed nahi hain.
    *   **Valid:** `case 1:`, `case 'A':`, `case 10+20:`
    *   **Invalid:** `case b:` (jahan `b` ek variable hai)
2.  **`break` keyword:** Har case ke end mein lagana zaroori hai, warna **fall-through** ho jayega (aage ke saare cases execute ho jayenge).
3.  **`default` case:** Optional, par unexpected inputs handle karne ke liye accha hai.
4.  **Duplicate case values:** Allowed nahi hain.

### Program: Simple Menu-Driven Program
```c
#include <stdio.h>

void playgame();
void loadgame();
void playmultiplayer();

int main() {
    int input;
    printf("1. Play game\n");
    printf("2. Load game\n");
    printf("3. Play multiplayer\n");
    printf("4. Exit\n");
    printf("Selection: ");
    scanf("%d", &input);

    switch (input) {
        case 1:
            playgame();
            break;
        case 2:
            loadgame();
            break;
        case 3:
            playmultiplayer();
            break;
        case 4:
            printf("Thanks for playing!\n");
            break;
        default:
            printf("Bad input, quitting!\n");
            break;
    }
    getchar();
    return 0;
}
```

### 7.1 Fall-Through Problem (Exam Important)
Agar `break` nahi lagate, toh matched case ke baad ke saare cases execute ho jate hain.

**Example:**
```c
int x = 2;
switch (x) {
    case 1: printf("One ");
    case 2: printf("Two ");
    case 3: printf("Three ");
    default: printf("Default");
}
// Output: Two Three Default (fall-through hua)
```

---

## 🔄 8. `break` and `continue` (Extra Exam Topic)

PDF mein `break` ka zikr switch mein hai. Exams mein `break` vs `continue` pucha jata hai.

| Feature | `break` | `continue` |
| :--- | :--- | :--- |
| **Kaam** | Loop ya switch se **poora bahar** nikal jata hai. | Loop ki **current iteration skip** karke next iteration par jata hai. |
| **Use** | `for`, `while`, `do-while`, `switch` | `for`, `while`, `do-while` (switch mein nahi) |
| **Example** | `if (x == 5) break;` → loop khatam | `if (x == 5) continue;` → x=5 skip, next iteration |

**Example:**
```c
// break
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    printf("%d ", i);
}
// Output: 0 1 2 3 4

// continue
for (int i = 0; i < 10; i++) {
    if (i == 5) continue;
    printf("%d ", i);
}
// Output: 0 1 2 3 4 6 7 8 9 (5 skip)
```

---

## ⚠️ 9. Common Mistakes & Dangling Else Problem

### 9.1 Dangling Else Problem (Exam Important)
Jab nested `if` mein braces nahi lagate, toh `else` kis `if` ke saath match karega, ye confusion hota hai. C rule: **`else` hamesha nearest unmatched `if` ke saath match karta hai.**

**Example:**
```c
if (a > 0)
    if (b > 0)
        printf("Both positive");
else
    printf("a is not positive"); // Ye else kis if ke saath hai?
```
*   **C Rule:** Ye `else` inner `if (b > 0)` ke saath match karega, outer `if (a > 0)` ke saath nahi.
*   **Solution:** Braces use karo.

### 9.2 Common Mistakes

| Mistake | Wrong | Correct |
| :--- | :--- | :--- |
| **Semicolon after if** | `if (x > 0);` | `if (x > 0)` (no semicolon) |
| **Assignment in condition** | `if (x = 5)` (assigns 5, always true) | `if (x == 5)` (compares) |
| **Missing braces** | `if (x > 0) printf("A"); printf("B");` (B always prints) | `if (x > 0) { printf("A"); printf("B"); }` |
| **Wrong case value** | `case x:` (variable) | `case 5:` (constant) |

---

## 📝 10. Summary, Cheat Sheet & Q&A

### 10.1 Summary
*   **Flow of Control:** Sequential execution ko modify karna.
*   **`goto`:** Unconditional jump (forward/backward). Avoid karna chahiye.
*   **`if`:** Condition true hone par execute.
*   **`if-else`:** Two-way decision.
*   **Nested `if`:** Multi-path decision (cascaded if-else if).
*   **Ternary (`?:`):** `if-else` ka short form. Lvalue nahi banata.
*   **`switch`:** Multi-way decision. Cases constant integral hone chahiye. `break` zaroori hai.
*   **`break` vs `continue`:** `break` loop se bahar, `continue` current iteration skip.
*   **Dangling Else:** `else` nearest `if` ke saath match karta hai.

### 10.2 Cheat Sheet

```markdown
| Statement | Syntax | Use |
|-----------|--------|-----|
| goto | `goto label;` | Unconditional jump |
| if | `if (cond) statement;` | True par execute |
| if-else | `if (cond) stmt1; else stmt2;` | Two-way decision |
| Ternary | `cond ? true_val : false_val;` | Short if-else |
| switch | `switch (var) { case val: ... break; }` | Multi-way decision |
| break | `break;` | Exit loop/switch |
| continue | `continue;` | Skip iteration |
```

### 10.3 Self-Assessment Questions (PDF Answers)
1.  **The goto requires a ______.** Label.
2.  **goto is an unconditional branching statement. (True/False)** True.
3.  **The series of statements enclosed by braces after expression in simple if statement is itself a simple expression statement. (True/False)** False.
4.  **In cascaded if/else/if/else chain, each else clause is another ______ statement.** `if`.
5.  **The conditional operator does not produce a lvalue. (True/False)** True.
6.  **The condition of a switch statement is a ______.** Value.
7.  **Switch statement is an unconditional branching statement. (True/False)** False (Ye conditional/multi-way branching hai).

### 10.4 Terminal Questions (Hints)
1.  **`x=1; y=1; if (n>0) x=x+1; y=y-1; printf("%d %d", x, y);`**
    *   **(a) n=1:** `if (n>0)` true, `x = 1+1 = 2`. `y = 1-1 = 0`. **Output: 2 0**
    *   **(b) n=0:** `if (n>0)` false, `x` remains 1. `y = 1-1 = 0`. **Output: 1 0**
    *   *(Note: `y=y-1` `if` ke bahar hai kyunki `if` mein braces nahi hain. Sirf `x=x+1` conditional hai.)*

2.  **Rewrite without compound relation:** `if (grade<=59 && grade>=50) second = second+1;`
    *   *Answer:*
        ```c
        if (grade >= 50)
            if (grade <= 59)
                second = second + 1;
        ```

3.  **Odd or Even Program:**
    *   *Answer:*
        ```c
        #include <stdio.h>
        void main() {
            int num;
            printf("Enter a number: ");
            scanf("%d", &num);
            if (num % 2 == 0)
                printf("%d is Even", num);
            else
                printf("%d is Odd", num);
        }
        ```

### 10.5 Extra Practice Questions (Exam Special)
1.  What is the difference between `if-else` and `switch`?
2.  Explain the fall-through problem in `switch` with an example.
3.  What is the "Dangling Else" problem? How to avoid it?
4.  Write a program using `switch` to create a simple calculator (+, -, *, /).
5.  What is the difference between `break` and `continue`?
6.  Predict the output:
    ```c
    int x = 3;
    switch (x) {
        case 1: printf("A");
        case 3: printf("C");
        case 4: printf("D");
        default: printf("E");
    }
    ```
    *Answer:* `CDE` (Fall-through hua kyunki break nahi hai)

---
> **💡 Bhai ka Gyan:** Exam mein **`switch` statement (fall-through, break, default)**, **Nested if-else (dangling else)**, aur **Ternary operator** ke questions pakke aate hain. `goto` ka forward/backward jump aur `break` vs `continue` ka difference bhi yaad rakhna. All the best! 🚀
