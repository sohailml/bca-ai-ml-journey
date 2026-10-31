# 💻 C Programming - Unit 3: I/O Operations in C

> **Course:** BCA - Semester 1  
> **Topic:** Formatted I/O (`printf`, `scanf`), Unformatted I/O (`getchar`, `putchar`, `gets`, `puts`, `getch`, `getche`), Interactive Programming  

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [Types of I/O in C](#-2-types-of-io-in-c)
3. [Formatted Input: `scanf()`](#-3-formatted-input-scanf)
4. [Formatted Output: `printf()`](#-4-formatted-output-printf)
5. [Unformatted I/O Functions (Character & String)](#-5-unformatted-io-functions-character--string)
6. [Common I/O Problems & Solutions (Exam Important)](#-6-common-io-problems--solutions-exam-important)
7. [Interactive Programming](#-7-interactive-programming)
8. [Summary, MCQs & Terminal Q&A](#-8-summary-mcqs--terminal-qa)

---

## 📌 1. Introduction & Objectives

C programming mein **Input** aur **Output** operations ke liye kai functions hain. PDF mein specifically inka zikr hai:
*   **`printf()`** aur **`scanf()`**: Formatted input aur output ke liye. Ye single character, numerical values, aur strings sab handle kar sakte hain.
*   **`gets()`** aur **`puts()`**: Strings ke input aur output ke liye.
*   **`getchar()`**: Strings/characters read karne ke liye (especially whitespace ke saath).

> [!IMPORTANT]
> **Security Note:** Input handling careful honi chahiye taaki buffer overflows jaise security risks se bacha ja sake. `printf` aur `scanf` mein specifiers ka alignment (match) hona bahut zaroori hai.

**Objectives:**
*   `printf` function ko formatted output ke liye samajhna aur implement karna.
*   `scanf` function ko formatted input ke liye proficiently use karna.

---

## 🗂️ 2. Types of I/O in C

C mein I/O functions ko 2 main categories mein baanta jata hai:

| Type | Functions | Kya Karte Hain? |
| :--- | :--- | :--- |
| **Formatted I/O** | `printf()`, `scanf()` | Data ko specific format (specifiers jaise `%d`, `%f`) ke saath read/write karte hain. |
| **Unformatted I/O** | `getchar()`, `putchar()`, `gets()`, `puts()`, `getch()`, `getche()`, `putch()` | Data ko bina kisi format ke, raw form mein read/write karte hain (character by character ya string by string). |

> [!NOTE]
> Saare functions `stdio.h` header file include karne ke baad hi use ho sakte hain (except `getch()`/`getche()` jo `conio.h` mein hote hain).

---

## ⌨️ 3. Formatted Input: `scanf()`

`scanf()` function standard input device (keyboard) se data enter karne ke liye use hota hai. Ye numerical values, single character, aur strings—sab enter kar sakta hai.

**Syntax:**
```c
scanf(control string, arg1, arg2, ...argn);
```

*   **Control String:** Ye string batati hai ki kaunsa data type enter karna hai (formatting information).
*   **Arguments (arg1, arg2...):** Ye **pointers** hote hain jo memory mein data items ke addresses indicate karte hain. (Isliye `&` operator use karte hain, strings ke alawa).

**Control String ke Parts:**
1.  **Control Characters:** `%` sign se preceded hote hain (jaise `%d`, `%f`).
2.  **Whitespace Characters:** Tabs, spaces, etc. (scanf inhe skip kar deta hai).
3.  **Non-whitespace Characters:** Match hone ke baad discard ho jate hain.

### 3.1 Control Characters Table (Table 3.1.1)

| Control Character | Explanation (Kya Karta Hai?) |
| :--- | :--- |
| **`%c`** | Ek single character read karta hai. |
| **`%d`** | Ek decimal integer read karta hai. |
| **`%i`** | Ek integer read karta hai (auto-detect: decimal, octal, ya hex). |
| **`%e`, `%f`, `%g`** | Ek floating-point number read karta hai. |
| **`%o`** | Ek octal number read karta hai. |
| **`%s`** | Ek string read karta hai (sirf ek word, space par ruk jata hai). |
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

> [!NOTE]
> **`%d` vs `%i` ka Difference:**
> *   `%d` sirf **decimal** integer read karta hai.
> *   `%i` **auto-detect** karta hai: agar number `0` se start ho toh octal, `0x` se start ho toh hex, warna decimal.

### 3.2 Program: Reading Integers, Floats, Characters, and Strings

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

### 3.3 Reading Strings with Whitespace

`%s` control character sirf ek word (bina space ke) read karta hai. Agar string mein spaces hain, toh `%s` sirf pehla word read karega.

**PDF mein bataye gaye Solutions:**
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
> Agar lowercase letters bhi allow karne hain, toh list mein `a-z` bhi add karna padega (jaise `%[A-Za-z ]`).

---

## 🖨️ 4. Formatted Output: `printf()`

`printf()` function standard output device (screen) par formatted output likhne ke liye use hota hai.

**Syntax:**
```c
printf(control string, arg1, arg2, ...argn);
```

### 4.1 Format Specifiers for `printf()` (Table 3.1.2)

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

### 4.2 Width and Precision (Field Width)

Aap print hone wale numbers/strings ki **width** aur **precision** (decimal places) specify kar sakte hain.

*   **`%3d`:** Ek `int` ko kam se kam 3 spaces wide field mein print karega.
*   **`%5.2f`:** Ek `float`/`double` ko kam se kam 5 spaces wide field mein print karega, jisme **2 decimal places** hongi.

**Left Justification (`-` flag):**
*   **`%-5d`:** Number ko 5 spaces mein left-aligned print karega (right side par spaces bachengi).

**Zero Padding (`0` flag):**
*   **`%05d`:** Number ko 5 spaces mein print karega, aur agar number chhota hai toh aage `0` lagayega (jaise `00042`).

**Dynamic Width (`*`):**
*   **`%*d`:** Width ko argument se lene ke liye (jaise `printf("%*d", 5, 42);` → 5 spaces wide).

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

### 4.3 `%c` vs `%d` (Character vs Integer)

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

### 4.4 `printf()` ka Return Value (Exam Important)

`printf()` return karta hai:
*   **Success:** Print kiye gaye total characters ki count (integer).
*   **Error:** Negative value.

**Example:**
```c
int count = printf("Hello");
// count = 5 (kyunki 5 characters print hue)
```

### 4.5 `%f` vs `%lf` (Float vs Double)

*   **`printf` mein:** `%f` aur `%lf` dono `float` aur `double` ke liye kaam karte hain (kyunki `float` automatically `double` mein promote ho jata hai).
*   **`scanf` mein:** `%f` sirf `float` ke liye, aur `%lf` sirf `double` ke liye. Ise mix mat karna!

### 4.6 Common Errors with `printf()`

> [!WARNING]
> `printf` ko nahi pata ki kitne arguments pass hue hain ya unka type kya hai. Wo sirf format string mein specifiers dekh kar kaam karta hai.
> *   Agar specifiers aur arguments match nahi karte (jaise `%d` ko float pass karna), toh `printf` **nonsense numbers** print kar sakta hai.
> *   **Type Matching Rules:**
>     *   `%c` aur `%d` ke liye argument `char` ya `int` ho sakta hai.
>     *   `%s` ke liye string constant, char array, ya char pointer ho sakta hai.
>     *   `%e`, `%f`, `%g` ke liye `float` ya `double` ho sakta hai.
>     *   **`%d` long int, float, double ke liye kaam nahi karta.**
>     *   **`%f` int ke liye kaam nahi karta.**

---

## 🔄 5. Unformatted I/O Functions (Character & String)

PDF mein clearly likha hai: *"The functions scanf() and printf() permit the transfer of single character, numerical values and strings; the functions gets() and puts() facilitate the input and output of strings."* Aur *"One way is to use the getchar() function within a loop."*

Isliye, ye functions exam ke liye bahut important hain.

### 5.1 `getchar()` (Character Input)
*   **Kaam:** Standard input (keyboard) se **ek single character** read karta hai.
*   **Syntax:** `int getchar(void);`
*   **Return:** Read kiya gaya character (integer ke roop mein) return karta hai. Agar end of file (EOF) aa jaye, toh `EOF` return karta hai.
*   **Use Case:** Strings ko character-by-character read karne ke liye (especially jab spaces bhi read karne ho).

**Example:**
```c
#include <stdio.h>
int main() {
    char c;
    printf("Enter a character: ");
    c = getchar(); // Ek character read karega
    printf("You entered: %c\n", c);
    return 0;
}
```

### 5.2 `putchar()` (Character Output)
*   **Kaam:** Standard output (screen) par **ek single character** print karta hai.
*   **Syntax:** `int putchar(int char);`
*   **Return:** Print kiya gaya character return karta hai. Error par `EOF` return karta hai.
*   **Use Case:** Single character ko screen par dikhane ke liye.

**Example:**
```c
#include <stdio.h>
int main() {
    char c = 'A';
    putchar(c); // 'A' print karega
    putchar('\n'); // New line print karega
    return 0;
}
```

### 5.3 `gets()` (String Input)
*   **Kaam:** Standard input se ek **poori line (string)** read karta hai, jab tak Enter (newline) na dabaya jaye. Isme spaces bhi shamil hote hain.
*   **Syntax:** `char *gets(char *str);`
*   **Security Issue:** `gets()` ka koi bound check nahi hota, isliye ye **buffer overflow** ka khatra paida kar sakta hai. (Aaj kal ise use nahi karte, `fgets()` better hai).
*   **Return:** Success par string ka pointer return karta hai, error par `NULL`.

**Example:**
```c
#include <stdio.h>
int main() {
    char str[50];
    printf("Enter a string: ");
    gets(str); // Spaces ke saath poori line read karega
    printf("You entered: %s\n", str);
    return 0;
}
```

### 5.4 `puts()` (String Output)
*   **Kaam:** Standard output par ek **string print** karta hai aur automatically end mein ek **newline character (`\n`)** add kar deta hai.
*   **Syntax:** `int puts(const char *str);`
*   **Return:** Success par non-negative value, error par `EOF`.

**Example:**
```c
#include <stdio.h>
int main() {
    char str[] = "Hello World";
    puts(str); // "Hello World" print karega aur new line add karega
    return 0;
}
```

### 5.5 `getch()` and `getche()` (Non-Standard, but Common in Exams)

> [!IMPORTANT]
> Ye functions standard C ka part nahi hain. Ye `conio.h` header file mein aate hain (mainly Turbo C / Windows compilers mein). Exams mein aksar inka comparison `getchar()` se pucha jata hai.

*   **`getch()`:** Character read karta hai bina screen par echo kiye (type karte hi kuch dikhta nahi, bas enter karna padta hai). Password input ke liye use hota hai.
*   **`getche()`:** Character read karta hai aur screen par echo bhi karta hai (type karte hi character dikh jata hai).
*   **`getchar()`:** Character read karta hai, echo bhi karta hai, aur Enter dabane ka wait karta hai (buffered input).

| Function | Header | Echo? | Buffered? |
| :--- | :--- | :--- | :--- |
| `getchar()` | `stdio.h` | Yes | Yes (Enter wait) |
| `getch()` | `conio.h` | No | No |
| `getche()` | `conio.h` | Yes | No |

### 5.6 `fgets()` and `fputs()` (Safer Alternatives)

*   **`fgets()`:** `gets()` ka safer version. Ye ek maximum length leta hai, jisse buffer overflow nahi hota.
    *   **Syntax:** `fgets(str, size, stdin);` (Size se zyada characters read nahi karega).
*   **`fputs()`:** `puts()` jaisa, par ye automatically newline nahi add karta.
    *   **Syntax:** `fputs(str, stdout);`

**Example:**
```c
char str[50];
fgets(str, 50, stdin); // Safe way to read a line
fputs(str, stdout);    // Prints without extra newline
```

### 5.7 Comparison Table: All I/O Functions

| Function | Type | Header | Purpose |
| :--- | :--- | :--- | :--- |
| `scanf()` | Formatted Input | `stdio.h` | Mixed data types (int, float, string) read karta hai, spaces par ruk jata hai. |
| `printf()` | Formatted Output | `stdio.h` | Mixed data types ko format ke saath print karta hai. |
| `getchar()` | Unformatted Input | `stdio.h` | Ek single character read karta hai (buffered, Enter wait). |
| `putchar()` | Unformatted Output | `stdio.h` | Ek single character print karta hai. |
| `gets()` | String Input | `stdio.h` | Poori line (spaces ke saath) read karta hai (unsafe). |
| `puts()` | String Output | `stdio.h` | String print karta hai aur auto newline lagata hai. |
| `getch()` | Unformatted Input | `conio.h` | Character read, no echo, no Enter wait (non-standard). |
| `getche()` | Unformatted Input | `conio.h` | Character read, echo, no Enter wait (non-standard). |
| `fgets()` | String Input | `stdio.h` | Safe way to read a line with max length limit. |
| `fputs()` | String Output | `stdio.h` | String print, no auto newline. |

---

## ⚠️ 6. Common I/O Problems & Solutions (Exam Important)

### 6.1 The Newline Buffer Problem (Very Important)

Jab tu `scanf()` se input leta hai aur Enter dabata hai, toh Enter ka newline character (`\n`) input buffer mein reh jata hai. Agli baar `getchar()` ya `%c` use karne par ye newline hi read ho jata hai, aur actual character miss ho jata hai.

**Problem Example:**
```c
int num;
char ch;
printf("Enter a number: ");
scanf("%d", &num);
printf("Enter a character: ");
scanf("%c", &ch); // Ye newline read kar lega, actual character nahi
```

**Solutions:**
1.  **Space in `scanf`:** `scanf(" %c", &ch);` (Space lagane se whitespace skip ho jata hai).
2.  **`fflush(stdin)`:** `fflush(stdin);` se buffer clear karo (non-standard, but works in Windows).
3.  **Extra `getchar()`:** Ek extra `getchar()` call karke newline consume karo.

### 6.2 Buffer Overflow with `gets()`
`gets()` size check nahi karta, isliye zyada input dene par buffer overflow ho jata hai. `fgets()` use karna chahiye.

### 6.3 Format Specifier Mismatch
Agar `printf`/`scanf` mein galat specifier use kiya, toh garbage value aati hai ya program crash ho jata hai.

### 6.4 `scanf` mein `&` Bhoolna
Integer, float, char ke liye `&` lagana zaroori hai. Strings ke liye nahi. Agar `&` bhool gaya, toh program crash ho sakta hai.

---

## 💬 7. Interactive Programming (Question-Answer Style)

Interactive programming mein computer aur user ke beech question-answer dialog hota hai. C mein ye `scanf()` aur `printf()` ke alternate use se banaya jata hai.

### 7.1 Program: Calculate Simple Interest

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

## 📝 8. Summary, MCQs & Terminal Q&A

### 8.1 Summary
*   **`scanf()`:** Formatted input ke liye. Variables ke addresses (`&`) arguments ke roop mein maangta hai (strings ke alawa).
*   **`printf()`:** Formatted output ke liye. Return value: print kiye gaye characters ki count.
*   **Format Specifiers:** `%d` (int), `%f` (float/double), `%c` (char), `%s` (string), `%o` (octal), `%x` (hex), etc.
*   **Width and Precision:** `%3d` (min 3 spaces), `%5.2f` (min 5 spaces, 2 decimals), `%-5d` (left aligned), `%05d` (zero padded).
*   **`getchar()`/`putchar()`:** Single character input/output.
*   **`gets()`/`puts()`:** String input (spaces ke saath) / output (auto newline). `gets()` unsafe hai.
*   **`fgets()`/`fputs()`:** Safer string I/O.
*   **`getch()`/`getche()`:** Non-standard character input (conio.h).
*   **Newline Buffer Problem:** `scanf` ke baad `getchar`/`%c` use karne par `\n` read ho sakta hai. Space in `scanf(" %c")` solution hai.
*   **Interactive Programming:** `printf` se prompt dikhana, `scanf` se input lena, aur phir `printf` se output dikhana.

### 8.2 Self-Assessment Questions (Quick Answers)
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

### 8.3 Terminal Questions (Hints)
*   **Q1: Role of format specifiers in `printf`?**
    *   *Ans:* Format specifiers batate hain ki argument ko kaise interpret aur print karna hai (e.g., `%d` for integer, `%f` for float). Bina specifier ke `printf` ko type nahi pata.
*   **Q2: How is `scanf` used for input? Importance of correct specifiers?**
    *   *Ans:* `scanf` control string aur variables ke addresses leta hai. Correct specifier (`%d` for int, `%f` for float) batana zaroori hai taaki input sahi memory location par sahi type ke saath store ho. Galat specifier se garbage value aa sakti hai.
*   **Q3: Significance of `&` (ampersand) in `scanf`?**
    *   *Ans:* `&` operator variable ka memory address deta hai. `scanf` ko address chahiye hota hai taaki wo us location par value store kar sake. Strings ke liye `&` nahi lagta kyunki string ka naam hi address hota hai.

### 8.4 Additional Possible Exam Questions (Practice)
1.  **Difference between `printf` and `puts`?** (`printf` formatted, `puts` string + newline).
2.  **Difference between `scanf` and `gets`?** (`scanf` `%s` stops at space, `gets` reads full line).
3.  **Why is `gets` dangerous?** (No bound checking, buffer overflow).
4.  **What is the return value of `printf`?** (Number of characters printed).
5.  **Difference between `%d` and `%i` in `scanf`?** (`%d` decimal only, `%i` auto-detect base).
6.  **Difference between `getch` and `getche`?** (getch no echo, getche echo).
7.  **Write a program to read a character and print its ASCII value.**

---
> **💡 Bhai ka Gyan:** Exam mein `printf`/`scanf` ke format specifiers, unke return values, `%d` vs `%i`, `gets` vs `fgets`, `getch` vs `getche` vs `getchar`, aur newline buffer problem ke questions zarur aate hain. Aur simple interest wala interactive program bhi yaad rakhna. Ab tu in notes ke bharose exam de sakta hai! All the best! 🚀
