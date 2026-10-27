# 💻 C Programming - Unit 2: Basics of C Programming

> **Course:** BCA - Semester 1  
> **Topic:** Data Types, Variables, Type Casting, Keywords & Constants  

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [Data Types in C](#-2-data-types-in-c)
3. [Floating-Point Numbers & Ranges](#-3-floating-point-numbers--ranges)
4. [Important C Programs (Line-by-Line)](#-4-important-c-programs-line-by-line)
5. [Type Conversion (Automatic)](#-5-type-conversion-automatic)
6. [Mixed-Mode Expressions](#-6-mixed-mode-expressions)
7. [Type Cast Operator (Explicit Conversion)](#-7-type-cast-operator-explicit-conversion)
8. [The `char` Data Type](#-8-the-char-data-type)
9. [Keywords in C](#-9-keywords-in-c)
10. [Concept of Integer & Variables](#-10-concept-of-integer--variables)
11. [Constants in C](#-11-constants-in-c)
12. [Summary & Q&A](#-12-summary--qa)

---

## 📌 1. Introduction & Objectives

C programming mein **Data Types** bahut important role play karte hain. Ye decide karte hain ki ek variable memory mein kis tarah ki value store karega aur us par kya operations honge.
*   **Objective:** Data types ka use karke data ko precisely represent karna aur program ko efficiently execute karna.
*   **Floating-point numbers:** Real numbers (decimal wale) store karne ke liye use hote hain.
*   **Type Casting:** Ek data type ko explicitly dusre data type mein convert karne ke liye.
*   **Variables:** Wo containers jahan hum program execution ke dauran data store karte hain.
*   **Constants:** Wo values jo program chalte waqt change nahi hoti.

---

## 📊 2. Data Types in C

C language mein mainly 4 core data types hote hain: `int`, `float`, `double`, aur `char`.
*   **Type Modifiers:** `short`, `long`, `signed`, `unsigned` ka use karke hum in data types ki range aur size ko modify kar sakte hain.
*   **Type Qualifiers:** `const` (value change nahi hogi) aur `volatile` ka use bhi hota hai.

### 3. Floating-Point Numbers (Decimal Numbers)
Floating point numbers ko C mein `float` keyword se define karte hain. Ye 32 bits (4 bytes) memory lete hain aur lagbhag 6 digits ki precision (accuracy) dete hain.
*   Agar `float` se zyada accuracy chahiye, toh **`double`** (64 bits, 14 digits precision) use karte hain.
*   Aur zyada precision ke liye **`long double`** (80 bits) use hota hai.

**Table: Floating point types on a 16-bit machine**

| Type | Size (bits) | Range |
| :--- | :--- | :--- |
| `float` | 32 | 3.4E-38 to 3.4E+38 |
| `double` | 64 | 1.7E-308 to 1.7E+308 |
| `long double` | 80 | 3.4E-4932 to 1.1E+4932 |

---

## 💻 4. Important C Programs (Line-by-Line)

### Program 1: Typical Declarations and Assignments
Ye program dikhata hai ki alag-alag data types mein values kaise store hoti hain.

```c
main()
{
    /* DECLARATIONS */
    float x, p;
    double y, q;
    unsigned k;
    
    /* DECLARATIONS AND ASSIGNMENTS */
    int m = 54321;
    long int n = 1234567890;

    /* ASSIGNMENTS */
    x = 1.234567890000;
    y = 9.87654321;
    k = 54321;
    p = q = 1.0;

    /* PRINTING */
    printf("m=%d\n", m);
    printf("n=%ld\n", n);
    printf("x=%.12lf\n", x);
    printf("x=%f\n", x);
    printf("y=%.12lf\n", y);
    printf("y=%lf\n", y);
    printf("k=%u p=%f q=%.12lf\n", k, p, q);
}
```
*   **`%.12lf`**: Ye format specifier batata hai ki `double` value ko 12 decimal places tak print karna hai. `lf` double ke liye use hota hai.

### Program 2: Calculate Average of N Numbers
```c
#define N 10  /* SYMBOLIC CONSTANT */
main()
{
    int count;  /* DECLARATION OF VARIABLES */
    float sum, average, number;
    
    sum = 0;    /* INITIALIZATION */
    count = 0;
    
    while (count < N)
    {
        scanf("%f", &number);
        sum = sum + number;
        count = count + 1;
    }
    
    average = sum / N;
    printf("N = %d Sum = %f", N, sum);
    printf("Average = %f", average);
}
```
*   **`#define N 10`**: Ye ek **macro** hai. `N` ko pure program mein `10` se replace kar diya jayega. Ise symbolic constant bhi kehte hain.
*   **`while (count < N)`**: Ye loop 10 baar chalega aur har baar user se number lekar `sum` mein add karega.

### Program 3: Roots of a Quadratic Equation
```c
#include <math.h>
main()
{
    float a, b, c, discriminant, root1, root2;
    printf("input the values of a, b and c\n");
    scanf("%f %f %f", &a, &b, &c);
    
    discriminant = b*b - 4*a*c;
    
    if (discriminant < 0)
        printf("roots are imaginary\n");
    else
    {
        root1 = (-b + sqrt(discriminant)) / (2*a);
        root2 = (-b - sqrt(discriminant)) / (2*a);
        printf("Root1 = %5.2f\n Root2 = %5.2f\n", root1, root2);
    }
}
```
*   **`#include <math.h>`**: `sqrt()` function use karne ke liye ye header file include karni padti hai.
*   **`%5.2f`**: Iska matlab hai total 5 characters ki jagah, jisme se 2 decimal ke baad honge.

---

## 🔄 5. Type Conversion (Automatic)

C language mein jab hum alag-alag data types ke variables ko ek expression mein use karte hain, toh compiler **strict rules** follow karta hai. Agar operands (values) alag types ke hain, toh **'lower' type automatically 'higher' type mein convert ho jata hai**.

**Rule of Thumb:** `char` ➡️ `int` ➡️ `long` ➡️ `float` ➡️ `double` ➡️ `long double` (Yani chhota dabba bade dabbe mein chala jata hai).

**Hierarchy of Conversion:**
1.  Agar ek operand `long double` hai, toh dusra bhi `long double` ban jayega.
2.  Warna agar ek `double` hai, toh dusra `double` ban jayega.
3.  Warna agar ek `float` hai, toh dusra `float` ban jayega.
4.  Warna agar ek `unsigned long int` hai, toh dusra bhi wahi banega.
5.  Warna agar ek `long int` aur dusra `unsigned int` hai, toh rules apply honge.
6.  Warna agar ek `long int` hai, toh dusra `long int` ban jayega.
7.  Warna agar ek `unsigned int` hai, toh dusra `unsigned int` ban jayega.

**Final Assignment ke waqt kya hota hai?**
Jab result ko left side wale variable mein assign karte hain, toh type change hota hai:
*   **`float` to `int`:** Decimal part truncate (cut) ho jata hai.
*   **`double` to `float`:** Digits round-off ho jati hain.
*   **`long int` to `int`:** Extra higher-order bits drop (delete) ho jate hain.

---

## 🧪 6. Mixed-Mode Expressions

Jab ek expression mein ek operand `real` (float/double) hota hai aur dusra `integer`, toh use **Mixed-Mode Expression** kehte hain. Isme result hamesha real number aata hai.

*   **Example 1:** `25 / 10.0 = 2.5` (Kyunki 10.0 real hai, toh division float mode mein hoga).
*   **Example 2:** `25 / 10 = 2` (Kyunki dono integer hain, decimal part cut ho jayega).

---

## 🛠️ 7. Type Cast Operator (Explicit Conversion)

Kabhi-kabhi humein automatic conversion ki zaroorat nahi hoti, humein forcefully conversion karna hota hai. Iske liye **Type Cast Operator** use hota hai.

**Syntax:** `(type-name) expression`

**Example:** Agar doctor aur engineer ki ratio nikalni hai, aur dono `int` hain, toh decimal part cut ho jayega. Isko solve karne ke liye:
`Ratio = (float)doctor_number / engineer_number;`

**Table: Use of Casts**

| Example | Action (Kya hota hai?) |
| :--- | :--- |
| `X = (int) 8.5` | 8.5 truncate hokar 8 ban jayega. |
| `A = (int) 21.3 / (int) 4.5` | Evaluate hoga `21 / 4` aur result hoga `5`. |
| `B = (double) sum/n` | Division floating-point mode mein hoga (decimal aayega). |
| `Y = (int) (a+b)` | Pehle `a+b` hoga, phir result integer mein convert hoga. |
| `Z = (int) a + b` | Pehle `a` integer banega, phir `b` se add hoga. |

*   **Rounding off:** Casting ka use round-off ke liye bhi kar sakte hain: `X = (int)(y + 0.5);` (Agar y = 37.7, toh 38.2 -> 38 ban jayega).

---

## 🔤 8. The `char` Data Type

Char data type ka use single character (jaise 'A', 'b', '5') store karne ke liye hota hai.
*   Size: 8 bits (1 byte).
*   **Signed char:** Range -128 to 127.
*   **Unsigned char:** Range 0 to 255.
*   Character constant single quotes (`' '`) ke andar likha jata hai, string double quotes (`" "`) ke andar.
*   `%c` format specifier character print karta hai, aur `%d` uski **ASCII value** print karta hai.

**Program to illustrate `char`:**
```c
#include <stdio.h>
main()
{
    char c = 'A';
    int a = 65;
    printf("%c\n", c); // Output: A
    printf("%d\n", c); // Output: 65 (ASCII value of A)
    printf("%c\n", a); // Output: A (65 ka character A hai)
}
```

---

## 🔑 9. Keywords in C

Keywords **reserved words** hote hain jinka matlab fixed hota hai aur unhe variable name ke roop mein use nahi kar sakte. Inhe hamesha **lowercase** mein likha jata hai.

**ANSI C Keywords (32 total):**
`auto`, `break`, `case`, `char`, `const`, `continue`, `default`, `do`, `double`, `else`, `enum`, `extern`, `float`, `for`, `goto`, `if`, `int`, `long`, `register`, `return`, `short`, `signed`, `sizeof`, `static`, `struct`, `switch`, `typedef`, `union`, `unsigned`, `void`, `volatile`, `while`.

---

## 📦 10. Concept of Integer & Variables

**Integer:** Whole numbers (bina decimal ke). Inka size machine par depend karta hai (16-bit par -32768 to 32767, 32-bit par bada).

**Variable:** Memory ka ek hissa (box) jiska ek naam hota hai, jahan hum value store karte hain.

**Rules for Naming Variables:**
1.  Naam letters (A-Z, a-z), digits (0-9), aur underscore (_) se bana hona chahiye.
2.  Naam **hamesha letter ya underscore** se shuru hona chahiye (digit se nahi).
3.  **Case Sensitive:** `sum`, `Sum`, aur `SUM` teeno alag variables hain.
4.  **Keywords ka use naam ke roop mein nahi kar sakte** (jaise `int` naam nahi rakh sakte).

**Declaring Variables:**
```c
int i;             // Ek variable declare kiya
long int i1, i2;   // Ek hi line mein do variables declare kiye
int a = 10;        // Declaration + Initialization
```

**Assignment Operator (`=`):**
`x = 1;` (x ko 1 bana diya).
`a = b;` (a ko b ki value de di).
`i = i + 1;` (i ki purani value mein 1 jod kar wapas i mein daal diya).
`c = a = b;` (Right to left chalta hai: pehle a ko b ki value mili, phir c ko a ki value mili).

---

## 🔒 11. Constants in C

Constants wo values hain jo program chalte waqt **change nahi hoti**.

### 4.1 Integer Constants
Numbers jo bina decimal ke hote hain. 3 types hote hain:
1.  **Decimal:** 0-9 (e.g., `12`, `-546`, `0`).
2.  **Octal:** 0-7, aur shuru mein `0` lagta hai (e.g., `045`, `0567`).
3.  **Hexadecimal:** 0-9 aur A-F, shuru mein `0x` ya `0X` (e.g., `0X6`, `0x5B`).

*   **Suffixes:** Badi values ke liye suffix lagate hain: `U` (unsigned), `L` (long), `UL` (unsigned long). E.g., `54637U`, `7685784L`.

### 4.2 Real Constants
Numbers jisme fractional part hota hai (e.g., `67.45`, `-8.5`).
*   **Exponential Notation:** `mantissa e exponent` (e.g., `7.5E9` ka matlab 7500000000). `e` lowercase ya uppercase ho sakta hai.

### 4.3 Character Constants
Single character single quotes mein (e.g., `'6'`, `'X'`, `';'`). Har character ki ek **ASCII value** hoti hai (jaise 'a' ki 97 hoti hai).

### 4.4 String Constants
Characters ka sequence double quotes mein (e.g., `"Hello!"`, `"1947"`, `"5+3"`).

### 4.5 Backslash Character Constants (Escape Sequences)
Ye special characters hain jo `\` se shuru hote hain aur output formatting ke kaam aate hain.

| Constant | Meaning (Matlab) |
| :--- | :--- |
| `\b` | Backspace |
| `\f` | Form feed |
| `\n` | New line (Enter) |
| `\r` | Carriage return |
| `\t` | Horizontal tab |
| `\v` | Vertical tab |
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |
| `\0` | Null |

---

## 📝 12. Summary & Q&A

### Summary
C programming mein data types, variables aur constants ka core foundation hota hai. `float`, `double`, `char` aur `int` ka range aur size samajhna zaroori hai. Automatic type conversion lower types ko higher types mein badalta hai, jabki Type Casting forcefully conversion karti hai. Variables ke naming rules aur constants ke types (Integer, Real, Character, String, Backslash) exam ke liye bahut important hain.

### Self-Assessment Questions (Quick Recap)
1.  **Float ki accuracy kam ho toh?** `double` ya `long double` use karein.
2.  **Automatic conversion?** Lower type higher type mein convert hota hai (True).
3.  **Casting round-off?** Haan, `(int)(y + 0.5)` se round off kar sakte hain.
4.  **`%c` vs `%d`?** `%c` character print karta hai, `%d` uski ASCII value.
5.  **Keywords lowercase?** Haan, hamesha.
6.  **`default` valid keyword?** Haan (True).
7.  **Size of `int`?** 16 bits (ya 32 bits machine par depend).
8.  **Variable case sensitive?** Haan (True).
9.  **Octal digits?** 0 se 7 tak.
10. **Hexadecimal prefix?** `0x` ya `0X`.

### Terminal Questions (Hints)
*   **Q: Signed vs Unsigned Integers?**
    *   *Ans:* Signed integer mein 1 bit sign (positive/negative) ke liye use hota hai (e.g., -32768 to 32767). Unsigned integer mein sirf positive values hoti hain (0 to 65535).
*   **Q: Rules for naming variables?**
    *   *Ans:* Letters, digits, underscore allowed; letter/underscore se start ho; no keywords; case-sensitive.
*   **Q: Different constants in C?**
    *   *Ans:* Integer (Decimal, Octal, Hex), Real (float, exponential), Character (single quote), String (double quote), Backslash (escape sequences).

---
> **💡 Bhai ka Gyan:** Exam mein "Type Casting" ka program (jaise average nikalna `(float)n` karke) aur "Escape sequences" (`\n`, `\t`) ka table zarur yaad karna. Ye questions pakke aate hain!
