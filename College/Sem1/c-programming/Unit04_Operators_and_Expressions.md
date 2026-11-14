# 💻 C Programming - Unit 4: Operators and Expressions

> **Course:** BCA - Semester 1  
> **Topic:** Arithmetic, Unary, Relational, Logical, Conditional, Bitwise, Increment/Decrement Operators, Library Functions, Precedence  
> **Format:** GitHub README Style (Ekdum aasan Hinglish mein, PDF ka saara content + Exam ke liye extra important topics)

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [Arithmetic Operators](#-2-arithmetic-operators)
3. [Unary Operators](#-3-unary-operators)
4. [Relational and Logical Operators](#-4-relational-and-logical-operators)
5. [The Conditional Operator (`?:`)](#-5-the-conditional-operator-)
6. [Library Functions](#-6-library-functions)
7. [Bitwise Operators](#-7-bitwise-operators)
8. [Increment and Decrement Operators](#-8-increment-and-decrement-operators)
9. [The `sizeof` Operator](#-9-the-sizeof-operator)
10. [Precedence and Associativity](#-10-precedence-and-associativity)
11. [Summary, Cheat Sheet & Q&A](#-11-summary-cheat-sheet--qa)

---

## 📌 1. Introduction & Objectives

C language mein **operators** wo symbols hote hain jo computer ko batate hain ki koi mathematical ya logical operation perform karna hai. Ye variables aur data ko manipulate karne ke liye use hote hain. Operators aur operands milkar **Expressions** banate hain.

**C mein Operators ki Categories:**
1.  Arithmetic Operators
2.  Unary Operators
3.  Relational Operators
4.  Logical Operators
5.  Conditional Operator
6.  Bitwise Operators
7.  Increment and Decrement Operators

**Objectives:**
*   Alag-alag categories ke operators ko explain karna.
*   Multiple operands par operators use karna.
*   Precedence aur Associativity ko samajhna.
*   Library functions aur unka use samajhna.
*   Alag-alag operators use karke chhote programs likhna.

---

## ➕ 2. Arithmetic Operators

Ye basic mathematical operations ke liye use hote hain.

| Operator | Name | Example |
| :--- | :--- | :--- |
| **`+`** | Addition | `a + b` |
| **`-`** | Subtraction | `a - b` |
| **`*`** | Multiplication | `a * b` |
| **`/`** | Division | `a / b` |
| **`%`** | Modulus (Remainder) | `a % b` |

> [!IMPORTANT]
> **Integer Division vs Float Division:**
> *   Jab dono operands **integers** hote hain, toh `/` operator remainder discard kar deta hai. (e.g., `1/2` is `0`, `7/4` is `1`).
> *   Jab koi ek operand **floating-point** ho, toh result float aata hai. (e.g., `1/2.0` is `0.5`, `7.0/4.0` is `1.75`).
> *   **Modulus (`%`)** sirf integers par apply hota hai. (`7.5 % 2` invalid hai).

**C mein Exponentiation (Power) Operator Nahi Hota:** Kisi number ka square/cube nikalna ho toh use khud se multiply karo (e.g., `a*a`) ya `pow()` library function use karo.

**Precedence:** Multiplication (`*`), Division (`/`), aur Modulus (`%`) ki precedence Addition (`+`) aur Subtraction (`-`) se zyada hoti hai. 
*   `1 + 2 * 3` = `1 + 6` = `7` (Not `9`).
*   Parentheses `()` use karke precedence change kar sakte hain: `(1 + 2) * 3` = `9`.

**Associativity:** Jab same precedence ke operators aate hain, toh evaluation **left to right** hoti hai.
*   `1 - 2 - 3` = `(1 - 2) - 3` = `-1 - 3` = `-4` (Not `+2`).

### Program 2.1: Convert Days to Months and Days
```c
#include <stdio.h>
int main() {
    int months, days;
    printf("Enter days\n");
    scanf("%d", &days);
    months = days / 30; // Integer division
    days = days % 30;   // Modulus
    printf("Months=%d Days=%d", months, days);
    return 0;
}
```
*   **Explanation:** Agar user 45 input karta hai, toh `45 / 30 = 1` month, aur `45 % 30 = 15` days.

---

## ➖ 3. Unary Operators

Unary operator wo hota hai jo **sirf ek operand** par kaam karta hai.

*   **Unary Minus (`-`):** Kisi positive number ko negative banane ke liye. C mein saare numeric constants positive hote hain, toh `-3` ka matlab hai positive `3` par unary minus lagana.
*   **Unary Plus (`+`):** Kisi number ko positive dikhane ke liye (usually ignore kiya jata hai, par valid hai).
*   **Note:** `++`, `--`, `!`, `~`, `sizeof` bhi unary operators hain, jo aage detail mein hain.

---

## ⚖️ 4. Relational and Logical Operators

### 4.1 Relational Operators
Ye do values ko compare karke **True (1)** ya **False (0)** return karte hain.

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| **`<`** | Less than | `1 < 2` → 1 (True) |
| **`<=`** | Less than or equal | `2 <= 2` → 1 (True) |
| **`>`** | Greater than | `3 > 4` → 0 (False) |
| **`>=`** | Greater than or equal | `4 >= 4` → 1 (True) |
| **`==`** | Equal to | `5 == 5` → 1 (True) |
| **`!=`** | Not equal to | `6 != 6` → 0 (False) |

> [!WARNING]
> **Common Mistake:** `==` (comparison) aur `=` (assignment) mein difference. 
> `if (a = 0)` galat hai. Ye `a` ko 0 assign karega aur condition hamesha false hogi. Sahi hai `if (a == 0)`.

### 4.2 Logical Operators (Boolean Operators)
Ye True/False values ko combine karte hain.

| Operator | Name | Description | Example |
| :--- | :--- | :--- | :--- |
| **`&&`** | AND | Dono operands true hone chahiye. | `(1 < 2) && (3 > 4)` → 1 && 0 → **0 (False)** |
| **`||`** | OR | Koi ek operand true hona chahiye. | `(1 < 2) || (3 > 4)` → 1 || 0 → **1 (True)** |
| **`!`** | NOT | True ko false, false ko true banata hai. | `!(1 < 2)` → !(1) → **0 (False)** |

**C mein True/False ka Representation:**
*   **False** = `0`
*   **True** = `Koi bhi non-zero value` (usually `1` use karte hain).

**Short-Circuit Evaluation (Exam Important):**
*   **`&&`**: Agar left side false hai, toh right side evaluate hi nahi hoti (kyunki result false hi rahega).
*   **`||`**: Agar left side true hai, toh right side evaluate hi nahi hoti (kyunki result true hi rahega).

**Wrong Condition Example:**
`if (1 < i < 10)` galat hai. Ye `(1 < i) < 10` ban jata hai. `(1 < i)` hamesha 0 ya 1 dega, aur 0 aur 1 dono 10 se chhote hain, toh ye hamesha true hoga.
**Sahi Tarika:** `if (i > 1 && i < 10)`.

---

## ❓ 5. The Conditional Operator (`?:`)

Ye **Ternary Operator** hai (3 operands leta hai). Ye `if-else` ka short form hai.

**Syntax:** `expr1 ? expr2 : expr3`
*   Agar `expr1` true hai, toh `expr2` evaluate hoga aur result banega.
*   Agar `expr1` false hai, toh `expr3` evaluate hoga aur result banega.

**Example:**
```c
int a = 100, b = 200, c;
c = (a > b) ? a : b; // Yahan a>b false hai, toh c ko b ki value (200) milegi.
```
**If-else Equivalent:**
```c
if (a > b) c = a;
else c = b;
```

---

## 📚 6. Library Functions

C language mein pehle se bani hui functions hoti hain jinhe **Library Functions** ya **Built-in Functions** kehte hain. Inke liye alag-alag header files include karni padti hain.

*   **`<stdio.h>`**: Input/Output functions (`printf`, `scanf`, `getchar`, `putchar`).
*   **`<ctype.h>`**: Character functions (`toupper`, `tolower`, `isupper`, `isdigit`).
*   **`<math.h>`**: Mathematical functions (`sqrt`, `pow`, `sin`, `cos`, `abs`, `ceil`, `floor`).

**Common Library Functions Table (Table 2.1):**

| Function | Purpose | Example (if a = 5.8, i = -10) |
| :--- | :--- | :--- |
| **`abs(i)`** | Integer ka absolute value (positive). | `abs(-10)` → 10 |
| **`fabs(d)`** | Float/Double ka absolute value. | `fabs(-5.5)` → 5.5 |
| **`ceil(d)`** | Round up (next integer). | `ceil(5.8)` → 6 |
| **`floor(d)`** | Round down (previous integer). | `floor(5.8)` → 5 |
| **`pow(d1, d2)`** | d1 raised to power d2. | `pow(2, 3)` → 8.0 |
| **`sqrt(d)`** | Square root. | `sqrt(16)` → 4.0 |
| **`toupper(c)`** | Lowercase to Uppercase. | `toupper('a')` → 'A' |
| **`tolower(c)`** | Uppercase to Lowercase. | `tolower('A')` → 'a' |

### Program 2.2: Lowercase to Uppercase
```c
#include <stdio.h>
#include <ctype.h>
int main() {
    int lower, upper;
    lower = getchar(); // Read a character
    upper = toupper(lower); // Convert to uppercase
    putchar(upper); // Print it
    return 0;
}
```

### Program 2.3: Math Library Functions
```c
#include <stdio.h>
#include <math.h>
int main() {
    int i = -10, e = 2, d = 10;
    float rad = 1.57;
    double d1 = 2.0, d2 = 3.0;
    printf("%d\n", abs(i));       // Output: 10
    printf("%f\n", sin(rad));     // Output: ~1.000000
    printf("%f\n", cos(rad));     // Output: ~0.000000
    printf("%f\n", exp(e));       // Output: e^2
    printf("%f\n", pow(d1, d2));  // Output: 8.000000
    return 0;
}
```

---

## 🔢 7. Bitwise Operators

Ye operators integers ke binary bits par kaam karte hain.

| Operator | Name | Description | Example (a=5 (0101), b=8 (1000)) |
| :--- | :--- | :--- | :--- |
| **`&`** | Bitwise AND | 1 agar dono bits 1 hon. | `a & b` = 0 (0000) |
| **`|`** | Bitwise OR | 1 agar koi ek bit 1 ho. | `a | b` = 13 (1101) |
| **`^`** | Bitwise XOR | 1 agar dono bits alag hon. | `a ^ b` = 13 (1101) |
| **`~`** | Bitwise NOT | Sab bits ulti kar do. | `~a` = -6 (1010 in 2's comp) |
| **`<<`** | Left Shift | Bits ko left shift karo (multiply by 2^n). | `a << 2` = 20 (010100) |
| **`>>`** | Right Shift | Bits ko right shift karo (divide by 2^n). | `a >> 2` = 1 (0001) |

**Common Use:** Integer ko set of flags ki tarah treat karna.
```c
#define VERBOSE 4 // 3rd bit (0100)
flags = flags | VERBOSE; // Turn on
flags = flags & ~VERBOSE; // Turn off
if (flags & VERBOSE) // Check if on
```

**Comma Operator (`,`):**
Do expressions ko link karta hai. Left se right execute hota hai. Sabse zyada `for` loop mein use hota hai.
```c
for (i = 0, j = 10; i < j; i++, j--);
```

---

## ➕ 8. Increment and Decrement Operators

Ye unary operators hain jo variable ki value ko 1 se badhate (`++`) ya ghataate (`--`) hain.

*   `++i` (Prefix): Pehle value badhao, phir use karo.
*   `i++` (Postfix): Pehle value use karo, phir badhao.
*   `--i` (Prefix): Pehle value ghatao, phir use karo.
*   `i--` (Postfix): Pehle value use karo, phir ghatao.

**Side Effects:** Ye operators variable ki value change kar dete hain, isliye inhe expression mein use karte waqt dhyan rakhna padta hai.

**Example:**
```c
int i = 5, k;
k = 2 * ++i; // i becomes 6, k becomes 12
// vs
i = 5;
k = 2 * i++; // k becomes 10, i becomes 6
```

> [!WARNING]
> **`i = i++` galat aur undefined behavior hai.** Iska result compiler par depend karta hai. Agar i ko 1 se badhana hai, toh `i++` ya `++i` ya `i += 1` likho.

**Shorthand Assignment:**
`v op= exp` ka matlab hai `v = v op (exp)`.
*   `x += y + 1` → `x = x + (y + 1)`
*   `a *= b` → `a = a * b`

---

## 📏 9. The `sizeof` Operator

Ye **compile-time** operator hai jo operand ka size **bytes** mein return karta hai.
*   Operand variable, constant, ya data type ho sakta hai.
*   Arrays aur structures ka size nikalne ke liye use hota hai.

**Example:**
```c
int i;
printf("%d", sizeof(i)); // Output: 2 (16-bit) ya 4 (32-bit)
printf("%d", sizeof(long int)); // Output: 4 ya 8
printf("%d", sizeof(235L)); // Output: 4 (long)
```

### Program 2.4: Sizeof Operator
```c
#include <stdio.h>
int main() {
    int i = 10;
    printf("integer: %d\n", sizeof(i));
    return 0;
}
```

---

## 📊 10. Precedence and Associativity

**Precedence** batati hai ki expression mein kaunsa operator pehle evaluate hoga.
**Associativity** batati hai ki jab same precedence ke operators hote hain, toh left-to-right jana hai ya right-to-left.

**Precedence Table (Table 2.2 - Highest to Lowest):**

| Operators | Associativity |
| :--- | :--- |
| `()` `[]` `->` `.` | Left to Right |
| `!` `~` `++` `--` `+` `-` `*` `&` `sizeof` (Unary) | Right to Left |
| `*` `/` `%` | Left to Right |
| `+` `-` | Left to Right |
| `<<` `>>` | Left to Right |
| `<` `<=` `>` `>=` | Left to Right |
| `==` `!=` | Left to Right |
| `&` | Left to Right |
| `^` | Left to Right |
| `|` | Left to Right |
| `&&` | Left to Right |
| `||` | Right to Left |
| `?:` | Right to Left |
| `=` `+=` `-=` `*=` `/=` `%=` | Right to Left |
| `,` (Comma) | Left to Right |

**Expression Evaluation Example:**
```c
float x = 20 + 2 / (3 + -23 * 4 - 1);
```
1.  `()` sabse pehle.
2.  `*` pehle `-23 * 4` = `-92`.
3.  `3 + (-92) - 1` = `-90`.
4.  `2 / -90` = `-0.0222`.
5.  `20 + (-0.0222)` = `19.9778`.

---

## 📝 11. Summary, Cheat Sheet & Q&A

### 11.1 Summary
*   **Arithmetic:** `+`, `-`, `*`, `/`, `%` (Modulus only for integers).
*   **Relational:** `<`, `<=`, `>`, `>=`, `==`, `!=` (Return 1 or 0).
*   **Logical:** `&&` (AND), `||` (OR), `!` (NOT). Short-circuiting hoti hai.
*   **Conditional (Ternary):** `expr1 ? expr2 : expr3`.
*   **Library Functions:** `math.h`, `ctype.h` etc. mein built-in functions.
*   **Bitwise:** `&`, `|`, `^`, `~`, `<<`, `>>` (Binary level operations).
*   **Increment/Decrement:** `++i` (prefix), `i++` (postfix). Side effects hote hain.
*   **Sizeof:** Memory size in bytes return karta hai.
*   **Precedence & Associativity:** Expression evaluation order decide karte hain.

### 11.2 Cheat Sheet

```markdown
| Category | Operators | Note |
|----------|-----------|------|
| Arithmetic | +, -, *, /, % | % only for int |
| Relational | <, <=, >, >=, ==, != | Returns 1 (true) or 0 (false) |
| Logical | &&, ||, ! | Short-circuit evaluation |
| Conditional | ?: | if-else short form |
| Bitwise | &, |, ^, ~, <<, >> | Operates on bits |
| Unary | ++, --, +, -, !, ~, sizeof | One operand |
| Assignment | =, +=, -=, *=, /=, %= | Right to left |
```

### 11.3 Self-Assessment Questions (PDF Answers)
1.  **Value of `14 % 3 + 7 % 2`:** `(2) + (1) = 3`. *(Ans: c)*
2.  **`%` (modulus) operator can be only applied to integers.**
3.  **Logical operators `&&` and `||` are used when we want to test more than one condition.**
4.  **`if(a<4<c)` statement is:** Incorrect.
5.  **Library functions** are built-in functions.
6.  **`floor(5.8)` = 5, `floor(-5.8)` = -6, `ceil(5.8)` = 6, `ceil(-5.8)` = -5.**
7.  **Bitwise operators** let you work with individual bits.
8.  **If flag1=5 (0101), flag2=8 (1000):** `flag1&flag2`=0, `flag1|flag2`=13, `~flag1`=10 (in 4-bit) or -6, `flag1^flag2`=13.

### 11.4 Terminal Questions (Hints)
1.  **`i=10, j=12`:**
    *   `i++` (i becomes 11)
    *   `c = j++ + i` → `c = 12 + 11 = 23` (j becomes 13)
    *   `d = ++i + j++` → `i` becomes 12, `d = 12 + 13 = 25` (j becomes 14)
    *   **Ans:** `c = 23, d = 25`.
2.  **`x *= -2 * (y + z) / 3` (x=2, y=3, z=4):**
    *   `x *= -2 * (7) / 3`
    *   `x *= -14 / 3` → `x *= -4` (integer division)
    *   `x = 2 * -4 = -8`.
3.  **`(i>=6) && (c=='w')` (i=7, c='w'):** True && True → **True (1)**.
4.  **`(i + f) % 4` (i=7, f=8.5):** `(15.5) % 4` → **Invalid** (Modulus float par nahi hota).
5.  **Associativity:** Order of evaluation jab same precedence ke operators hote hain (e.g., left-to-right for `+`).

### 11.5 Additional Practice Questions
1.  What is the difference between `=` and `==`?
2.  Explain short-circuit evaluation with an example.
3.  What is the output of `printf("%d", 10 > 9 > 8);`?
4.  Differentiate between `i++` and `++i`.
5.  What is the use of the `sizeof` operator?

---
> **💡 Bhai ka Gyan:** Exam mein Operator precedence ka table, `i++` vs `++i` ka difference, `&&`/`||` ka short-circuit, aur `%` (modulus) ka integer-only rule zarur aata hai. `sizeof` aur `?:` ke chhote programs bhi practice kar lena. All the best! 🚀
