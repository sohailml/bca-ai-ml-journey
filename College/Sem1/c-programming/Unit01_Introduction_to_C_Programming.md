# 💻 C Programming - Unit 1: Introduction to C Programming

> **Course:** BCA - Semester 1  
> **Topic:** Introduction, Features, Basic Structure & Simple C Programs

---

## 📑 Table of Contents
1. [Overview & History of C](#-1-overview--history-of-c)
2. [Features of C](#-2-features-of-c)
3. [Basic Structure of a C Program](#-3-basic-structure-of-a-c-program)
4. [Programming Style in C](#-4-programming-style-in-c)
5. [Simple C Programs (Line-by-Line Explanation)](#-5-simple-c-programs-line-by-line-explanation)
6. [Executing a C Program (Compilation)](#-6-executing-a-c-program-compilation)
7. [Summary & Q&A](#-7-summary--qa)

---

## 📜 1. Overview & History of C

### 1.1 Overview
C ek **general-purpose, structured programming language** hai. Iske instructions algebraic expressions (jaise maths ke equations) jaise dikhte hain, lekin isme English keywords (jaise `if`, `else`, `for`, `do`, `while`) ka use hota hai taaki code samajhna aasan ho.

**Variable Types ka Concept:** C mein variable ka "type" decide karta hai ki usme kya values aa sakti hain aur us par kya operations kiye ja sakte hain. (Jaise `int` mein sirf integers, `float` mein decimal numbers). 
*Note:* C mein data types ki values finite hoti hain (e.g., `int` finite integers hi store kar sakta hai). Agar tu kisi variable par koi operation kar raha hai, toh tujhe uske type ka dhyan rakhna padta hai (jaise binary operators floats par kaam nahi karte).

### 1.2 History and Evolution
*   C language ka janm **'Basic Combined Programming Language' (BCPL)** se hua, jise baad mein short karke **B** language kaha gaya (1960s mein Cambridge University mein bani).
*   **Dennis Ritchie** ne B language ko modify kiya aur 1972 mein **Bell Laboratories** mein implement kiya. Is naye language ka naam **C** rakha gaya.
*   C ko **UNIX operating system** ke saath develop kiya gaya tha (UNIX bhi Bell Labs mein bana tha aur usko mostly C mein hi code kiya gaya tha). Isiliye C ka UNIX ke saath bahut gehra connection hai.

---

## ✨ 2. Features of C

C language ki kuch sabse khaas baatein (features) hain:
1.  **Concise Programs:** C mein bahut kam lines mein lamba code likha ja sakta hai, kyunki isme operators ka ek bada set hota hai.
2.  **Small Instruction Set:** Iska core set chhota hai, lekin isme **library functions** ka ek bada collection hota hai jo kaam ko aasan banata hai.
3.  **User-Defined Functions:** C users ko apni khud ki library functions banane ki permission deta hai, jisse language ki capability ko extend kiya ja sakta hai.
4.  **Highly Portable:** C ke programs alag-alag computers par aasani se chal sakte hain (portability). Iski wajah ye hai ki C ne machine-dependent features ko library functions mein daal diya hai.
5.  **Efficient & Compact Compilers:** C ke compilers bahut chhote hote hain aur bahut efficient code generate karte hain (dusri high-level languages ke muqable).
6.  **Building Blocks (Functions):** Ek C program functions ka ek group hota hai. Har function ek specific kaam karta hai.

---

## 🏗️ 3. Basic Structure of a C Program

Ek C program 6 main sections se milkar banta hai. (Figure 1.1 ke according)

| Section Name | Kya Hota Hai? | Example / Details |
| :--- | :--- | :--- |
| **1. Documentation Section** | Ye comments (remarks) ka set hota hai. Isme program ka naam, author, aur logic likha jata hai. | `/* Program to add two numbers */` |
| **2. Link Section** | Compiler ko batata hai ki system library se kaunse functions link karne hain. | `#include <stdio.h>` |
| **3. Definition Section** | Isme symbolic constants define kiye jate hain. | `#define PI 3.14159` |
| **4. Global Declaration Section** | Wo variables jo ek se zyada functions mein use hote hain, yahan declare kiye jate hain. | `int a, b;` (outside functions) |
| **5. main() Function Section** | **Har C program mein ek main() function hona zaroori hai.** Yahan se execution shuru hota hai. Iske do parts hote hain: **Declaration part** (variables declare karna) aur **Executable part** (logic/statements). Ye `{` se shuru aur `}` par khatam hota hai. | `int main() { ... }` |
| **6. Subprogram Section** | Isme user-defined functions aate hain jo main() mein call kiye jate hain. | `void add() { ... }` |

> [!IMPORTANT]
> **Important Rules:**
> *   `main()` function section ke alawa, baaki saare sections optional hain (zaroorat ke hisaab se hata sakte hain).
> *   Har statement ke end mein **semicolon (;)** lagana zaroori hai (Sirf main() ke end wale closing brace ke baad nahi lagta).
> *   Comments `/* */` ke beech likhe jate hain aur compiler inhe ignore kar deta hai.

---

## 🖋️ 4. Programming Style in C

Programming style ka matlab hai code ko aise likhna ki wo readable (padhne layak) aur consistent ho.
*   **Meaningful Names:** Variables aur functions ke naam aise rakho jisse pata chale wo kya karte hain (jaise `radius` ki jagah `r` likhna bura style hai).
*   **Indentation:** Code ke andar spaces ya tabs (gaps) chhodo taaki block structure samajh aaye. 
*   **Consistency:** Ek jaisa coding convention follow karo. 
*   *Fayda:* Acha style code ki maintainability badhata hai aur dusre developers ko samajhna aasan hota hai.

---

## 💻 5. Simple C Programs (Line-by-Line Explanation)

### 5.1 Program 1: Hello World
```c
#include <stdio.h>
main()
{
    printf("Hello, world!\n");
    return 0;
}
```
*   **`#include <stdio.h>`**: Ye "Standard I/O Library" ko include karta hai, jisse `printf` function use karne ki permission milti hai.
*   **`main()`**: Ye function sabse pehle call hota hai jab program run hota hai. Empty `()` ka matlab hai ki ye koi arguments accept nahi karta.
*   **`{ }`**: Curly braces batate hain ki main function kahan se shuru aur kahan khatam ho raha hai.
*   **`printf("Hello, world!\n");`**: Ye ek library function hai jo screen par text print karta hai. `\n` ek special character hai jo new line (enter) ke liye use hota hai.
*   **`return 0;`**: Ye batata hai ki program successful raha. Agar `main` `0` return karta hai, toh OS ko pata chalta hai ki sab theek chala. Har function value return kar sakta hai, `main` bhi.

### 5.2 Program 2: Area of a Circle
```c
#include <stdio.h> /* Library file access */
/* program to calculate the area of a circle */
main() /* Function heading */
{
    float radius, area; /* Variable declarations */
    printf("Radius = ? "); /* Output statement (prompt) */
    scanf("%f", &radius); /* Input statement */
    area = 3.14159 * radius * radius; /* Assignment statement */
    printf("Area = %f", area); /* Output statement */
}
```
*   **`float radius, area;`**: Yahan humne do variables declare kiye jo decimal numbers store karenge.
*   **`scanf("%f", &radius);`**: Ye user se input lene ke liye hai. `%f` batata hai ki float format mein input aayega. `&radius` us variable ka memory address batata hai jahan value store hogi.
*   **`area = 3.14159 * radius * radius;`**: Ye calculation (logic) part hai (Area = πr²).
*   **`printf("Area = %f", area);`**: `%f` ki jagah `area` variable ki value print ho jayegi.

### 5.3 Program 3: Print a few numbers (Using Loop)
```c
#include <stdio.h>
/* print a few numbers, to illustrate a simple loop */
main()
{
    int i;
    for(i = 0; i < 10; i = i + 1) /* Looping statement */
        printf("i is %d\n", i);
    return 0;
}
```
*   **`for(i = 0; i < 10; i = i + 1)`**: Ye ek `for` loop hai. `i` 0 se shuru hoga, 10 se chhota hone tak chalega, aur har baar 1 badhega (0, 1, 2... 9).
*   **`printf("i is %d\n", i);`**: `%d` integer format ke liye hota hai. Loop chalne par ye `i` ki values print karega.

### 5.4 Program 4: Add Two Numbers
```c
#include <stdio.h>
main()
{
    int i, j, k; // Defining variables
    i = 6;       // Assign values
    j = 8;
    k = i + j;
    printf("sum of two numbers is %d \n", k); // Printing results
}
```
*   **`int i, j, k;`**: 3 integer variables declare kiye.
*   **`i = 6; j = 8;`**: Unme values daali.
*   **`k = i + j;`**: Dono ko plus karke `k` mein store kiya.
*   **`printf(...);`**: Result screen par print kiya.

---

## ⚙️ 6. Executing a C Program (Compilation)

C program (jo human-readable hai) ko computer direct nahi samajhta. Uske liye ek **Compilation Process** se guzarna padta hai:
1.  **Source Code:** Aap `.c` file mein code likhte ho.
2.  **Compilation:** Compiler (jaise **GCC - GNU Compiler Collection**) code ko machine-readable **Object Code** mein convert karta hai.
3.  **Executable File:** Fir object code ko link karke ek `.exe` (Windows) ya executable file banai jati hai.
4.  **Run:** User us executable file ko run karta hai.

---

## 📝 7. Summary & Q&A

### Summary
C (1972, Dennis Ritchie) ek powerful, structured aur portable language hai. Ye functions par based hai aur iska basic structure 6 sections mein divided hota hai (jisme `main()` sabse zaroori hai). Achi programming style aur proper compilation se hi ek efficient C program ban sakta hai.

### Self-Assessment Questions (SAQs)
1.  **Using C language programmers can write their own library functions. (True/False)**
    *   *Answer:* **True** (User-defined functions allow this).
2.  **C is a _____ level programming language.**
    *   *Answer:* **High** (Ya Middle-level, par PDF answer key mein High hai).
3.  **The documentation section contains a set of _____ lines.**
    *   *Answer:* **Comment**
4.  **Every C program must have one main() function. (True/False)**
    *   *Answer:* **True**
5.  **The information that needs to be passed in when a function is called is _____.**
    *   *Answer:* **Arguments**
6.  **The main() function doesn't return any value. (True/False)**
    *   *Answer:* **False** (It returns `0` on success).

### Terminal Questions (Short Answers)
*   **Q1. Explain the history of C language.**
    *   *Ans:* C was developed by Dennis Ritchie in 1972 at Bell Labs. It evolved from the B language (which came from BCPL) and was created alongside the UNIX operating system.
*   **Q2. What are the advantages of C language?**
    *   *Ans:* C is fast, efficient, highly portable, and structured. It allows user-defined functions and has a small but powerful instruction set with a rich library.
*   **Q3. What are the major components of a C program?**
    *   *Ans:* Documentation section, Link section, Definition section, Global declaration section, main() function section, and Subprogram section.
*   **Q4. What significance is attached to the function main?**
    *   *Ans:* The `main()` function is the entry point of the program. It is the first function that gets called when the program starts executing. Without it, a C program cannot run.

---
> **💡 Bhai ka Gyan:** Exams mein mostly `main()` function ka structure (Declaration + Executable part) aur code likhne ko bole jate hain (jaise Area of Circle ya Addition). In 4 programs ko ratne ki zaroorat nahi, bas unka logic aur syntax samajh lo, exam mein khud likh loge.
