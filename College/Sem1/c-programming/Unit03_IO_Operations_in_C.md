# 💻 C Programming - Unit 3: I/O Operations in C

> **Course:** BCA - Semester 1  
> **Topic:** Formatted Input (`scanf`) & Output (`printf`), Interactive Programming  

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [Formatted Input: `scanf()`](#-2-formatted-input-scanf)
3. [Formatted Output: `printf()`](#-3-formatted-output-printf)
4. [Interactive Programming (Question-Answer Style)](#-4-interactive-programming-question-answer-style)
5. [Summary & Q&A](#-5-summary--qa)

---

## 📌 1. Introduction & Objectives

C programming mein **Input** aur **Output** operations ke liye do functions sabse zyada use hote hain: **`printf()`** (output ke liye) aur **`scanf()`** (input ke liye).

*   **`printf()`:** Formatted output print karta hai, format specifiers (jaise `%d`, `%s`) use karke.
*   **`scanf()`:** Formatted input read karta hai, variables ke addresses arguments ke roop mein maangta hai (jaise `scanf("%d", &num);`).

> [!IMPORTANT]
> **Security Note:** Input handling careful honi chahiye taaki buffer overflows jaise security risks se bacha ja sake. `printf` aur `scanf` mein specifiers ka alignment (match) hona bahut zaroori hai.

**Other Functions:**
*   `gets()` aur `puts()`: Strings ke input/output ke liye.
*   Ye saare functions `stdio.h` header file include karne ke baad hi use ho sakte hain.

**Objectives:**
*   `printf` function ko formatted output ke liye samajhna aur implement karna.
*   `scanf` function ko formatted input ke liye proficiently use karna.

---

## ⌨️ 2. Formatted Input: `scanf()`

`scanf()` function standard input device (keyboard) se data enter karne ke liye use hota hai. Ye numerical values, single character, aur strings—sab enter kar sakta hai.

**Syntax:**
```c
scanf(control string, arg1, arg2, ...argn);
```
*   **Control String:** Ye string batati hai ki kaunsa data type enter karna hai (formatting information).
*   **Arguments (arg1, arg2...):** Ye **pointers** hote hain jo memory mein data items ke addresses indicate karte hain. (Isliye `&` operator use karte hain).

**Control String ke Parts:**
1.  **Control Characters:** `%` sign se preceded hote hain (jaise `%d`, `%f`).
2.  **Whitespace Characters:** Tabs, spaces, etc. (scanf inhe skip kar deta hai).
3.  **Non-whitespace Characters:** Match hone ke baad discard ho jate hain.

### 2.1 Control Characters Table (Table 3.1.1)

| Control Character | Explanation (Kya Karta Hai?) |
| :--- | :--- |
| **`%c`** | Ek single character read karta hai. |
| **`%d`** | Ek decimal integer read karta hai. |
| **`%i`** | Ek integer read karta hai (decimal, octal, ya hex). |
| **`%e`, `%f`, `%g`** | Ek floating-point number read karta hai. |
| **`%o`** | Ek octal number read karta hai. |
| **`%s`** | Ek string read karta hai. |
| **`%x`** | Ek hexadecimal number read karta hai. |
| **`%p`** | Ek pointer read karta hai. |
| **`%n`** | Ab tak read kiye gaye characters ki count store karta hai. |
| **`%u`** | Ek unsigned integer read karta hai. |
| **`%[]`** | Characters ka ek set read karta hai. |
| **`%%`** | Ek percent sign (`%`) read karta hai. |

**Working of `scanf()`:**
*   Input read karta hai aur format se match karta hai.
*   Jab control character aata hai, toh value next variable mein daal deta hai.
*   Whitespace (tabs, spaces) skip ho jate hain.
*   **Number between % and control char:** Agar `%` aur control character ke beech koi number aata hai (jaise `%5d`), toh sirf utne hi characters enter honge.
*   **`%[]` ka use:** Brackets ke andar jo characters hain, sirf wahi read honge.
*   **Return Value:** `scanf()` successfully assign hue variables ki count return karta hai. Error par `EOF` return karta hai.

### 2.2 Program: Reading Integers, Floats, Characters, and Strings

```c
#include <stdio.h>
int main() {
    int i;
    float f;
    char c;
    char str[10];

    // Input
    scanf("%d %f %c %s", &i, &f, &c, str);

    // Output
    printf("%d %f %c %s", i, f, c, str);
    return 0;
}
```

> [!NOTE]
> **Address (`&`) ka Rule:**
> *   `int`, `float`, `char` ke liye `scanf` mein `&` (address operator) lagana padta hai (jaise `&i`, `&f`, `&c`).
> *   **String variables** ke liye `&` nahi lagta, kyunki string ka naam khud hi address hota hai (jaise `str`).

### 2.3 Reading Strings with Whitespace

`%s` control character sirf ek word (bina space ke) read karta hai. Agar string mein spaces hain, toh `%s` sirf pehla word read karega.

**Solutions:**
1.  **`getchar()` in Loop:** Ek loop mein `getchar()` use karke characters read karo.
2.  **`gets()` Function:** Ye whitespace ke saath poori string read karta hai.
3.  **`%[...]` Control Character:** `%s` ki jagah square brackets mein characters ki list do.

**Example (Uppercase letters and spaces):**
```c
#include <stdio.h>
int main() {
    char str[80];
    scanf("%[ABCDEFGHIJKLMNOPQRST]", str); // Sirf uppercase aur space read karega
    return 0;
}
```
> [!TIP]
> Agar lowercase letters bhi allow karne hain, toh list mein `a-z` bhi add karna padega.

---

## 🖨️ 3. Formatted Output: `printf()`

`printf()` function standard output device (screen) par formatted output likhne ke liye use hota hai.

**Syntax:**
```c
printf(control string, arg1, arg2, ...argn);
```

### 3.1 Format Specifiers for `printf()` (Table 3.1.2)

| Format Specifier | Explanation (Kya Print Karta Hai?) |
| :--- | :--- |
| **`%d`** | Ek `int` argument decimal mein print karta hai. |
| **`%ld`** | Ek `long int` argument decimal mein print karta hai. |
| **`%c`** | Ek character print karta hai. |
| **`%s`** | Ek string print karta hai. |
| **`%f`** | Ek `float` ya `double` argument print karta hai. |
| **`%e`** | `%f` jaisa, par exponential notation mein. |
| **`%g`** | `%e` ya `%f`, jo bhi better ho. |
| **`%o`** | Ek `int` argument ko octal (base 8) mein print karta hai. |
| **`%x`** | Ek `int` argument ko hexadecimal (base 16) mein print karta hai. |
| **`%%`** | Ek single `%` sign print karta hai. |

### 3.2 Width and Precision (Field Width)

Aap print hone wale numbers/strings ki **width** aur **precision** (decimal places) specify kar sakte hain.

*   **`%3d`:** Ek `int` ko kam se kam 3 spaces wide field mein print karega.
*   **`%5.2f`:** Ek `float`/`double` ko kam se kam 5 spaces wide field mein print karega, jisme **2 decimal places** hongi.

**Examples:**

```c
// Example 1: Mixed format specifiers
printf("%c %d %f %e %s %d%%\n", '3', 4, 3.24, 66000000, "nine", 8);
// Output: 3 4 3.240000 6.600000e+07 nine 8%

// Example 2: Decimal, Octal, Hex
printf("%d %o %x\n", 100, 100, 100);
// Output: 100 144 64

// Example 3: Multiple printf calls build output sequentially
printf("Hello, ");
printf("world!\n");
// Output: Hello, world!
```

### 3.3 `%c` vs `%d` (Character vs Integer)

C mein characters internally small integers (ASCII values) hote hain. `printf` mein `%d` aur `%c` se hum decide karte hain ki integer ko kaise interpret karna hai.

```c
char c = 'A';
int i = 97;

// Case 1: Print character as character, integer as integer
printf("c = %c, i = %d\n", c, i);
// Output: c = A, i = 97

// Case 2: Print character as integer (ASCII), integer as character
printf("c = %d, i = %c\n", c, i);
// Output: c = 65, i = a
```

> [!WARNING]
> **Careful with `printf()`:**
> *   `printf` ko nahi pata ki kitne arguments pass hue hain ya unka type kya hai. Wo sirf format string mein specifiers dekh kar kaam karta hai.
> *   Agar specifiers aur arguments match nahi karte (jaise `%d` ko float pass karna), toh `printf` **nonsense numbers** print kar sakta hai.
> *   **Type Matching Rules:**
>     *   `%c` aur `%d` ke liye argument `char` ya `int` ho sakta hai.
>     *   `%s` ke liye string constant, char array, ya char pointer ho sakta hai.
>     *   `%e`, `%f`, `%g` ke liye `float` ya `double` ho sakta hai.
>     *   **`%d` long int, float, double ke liye kaam nahi karta.**
>     *   **`%f` int ke liye kaam nahi karta.**

---

## 💬 4. Interactive Programming (Question-Answer Style)

Interactive programming mein computer aur user ke beech question-answer dialog hota hai. C mein ye `scanf()` aur `printf()` ke alternate use se banaya jata hai.

### 4.1 Program: Calculate Simple Interest

```c
#include <stdio.h>
int main() {
    /* Sample interactive program */
    float principle, rate, time, interest;

    // Questions (Prompts)
    printf("Please enter the principle amount: ");
    scanf("%f", &principle);

    printf("Please enter the rate of interest: ");
    scanf("%f", &rate);

    printf("Please enter the period of deposit: ");
    scanf("%f", &time);

    // Calculation
    interest = principle * rate * time / 100.0;

    // Formatted Output (Width and Precision)
    printf("Principle = %7.2f\n", principle);
    printf("Rate of interest = %5.2f\n", rate);
    printf("Period of deposit = %5.2f\n", time);
    printf("Interest = %7.2f\n", interest);
    return 0;
}
```

**Example Input:**
```
Please enter the principle amount: 1000
Please enter the rate of interest: 5
Please enter the period of deposit: 2
```

**Corresponding Output:**
```
Principle = 1000.00
Rate of interest = 5.00
Period of deposit = 2.00
Interest = 100.00
```

> [!TIP]
> `%7.2f` ka matlab: Total 7 characters wide, jisme 2 decimal places (jaise `1000.00` 7 characters ka hai). `%5.2f` ka matlab: Total 5 characters wide, 2 decimal places (jaise ` 5.00` mein ek space hai).

---

## 📝 5. Summary & Q&A

### Summary
*   **`scanf()`:** Formatted input ke liye. Syntax: `scanf("format", &var1, &var2, ...)`. Variables ke addresses (`&`) arguments ke roop mein maangta hai (strings ke alawa).
*   **`printf()`:** Formatted output ke liye. Syntax: `printf("format", var1, var2, ...)`.
*   **Format Specifiers:** `%d` (int), `%f` (float/double), `%c` (char), `%s` (string), `%o` (octal), `%x` (hex), etc.
*   **Width and Precision:** `%3d` (min 3 spaces), `%5.2f` (min 5 spaces, 2 decimals).
*   **Interactive Programming:** `printf` se prompt dikhana, `scanf` se input lena, aur phir `printf` se output dikhana.
*   **Specifier Alignment:** `printf` aur `scanf` mein specifiers ka match hona bahut zaroori hai, warna galat output ya program crash ho sakta hai.

### Self-Assessment Questions (Quick Answers)
1.  **`______` string consists of control characters, whitespace characters, and non-whitespace characters.**
    *   *Answer:* **Control**
2.  **The control string used to read a hexadecimal character is `______`.**
    *   *Answer:* **`%x`**
3.  **`scanf()` functions needs address of the data item to be read as the argument. (True/False)**
    *   *Answer:* **True**
4.  **The output of `printf("%d %o %x\n", 64, 10, 75);` is `______`.**
    *   *Answer:* **64 12 4B** (64 decimal, 10 octal, 75 hex)
5.  **To print an int argument in octal, you can use `______` format string.**
    *   *Answer:* **`%o`**
6.  **The output of `int a=97; printf("%c", a);` is `______`.**
    *   *Answer:* **a** (97 ki ASCII value 'a' hai)

### Terminal Questions (Hints)
*   **Q1: Role of format specifiers in `printf`?**
    *   *Ans:* Format specifiers batate hain ki argument ko kaise interpret aur print karna hai (e.g., `%d` for integer, `%f` for float). Bina specifier ke `printf` ko type nahi pata.
*   **Q2: How is `scanf` used for input? Importance of correct specifiers?**
    *   *Ans:* `scanf` control string aur variables ke addresses leta hai. Correct specifier (`%d` for int, `%f` for float) batana zaroori hai taaki input sahi memory location par sahi type ke saath store ho. Galat specifier se garbage value aa sakti hai.
*   **Q3: Significance of `&` (ampersand) in `scanf`?**
    *   *Ans:* `&` operator variable ka memory address deta hai. `scanf` ko address chahiye hota hai taaki wo us location par value store kar sake. Strings ke liye `&` nahi lagta kyunki string ka naam hi address hota hai.

---
> **💡 Bhai ka Gyan:** Exam mein `printf` aur `scanf` ke format specifiers ka table aur unke examples zarur aate hain. `%c` vs `%d` ka difference aur `&` operator ka use `scanf` mein bahut important hai. Width/precision (`%5.2f`) ke saath simple interest wala program bhi yaad rakhna. All the best!
