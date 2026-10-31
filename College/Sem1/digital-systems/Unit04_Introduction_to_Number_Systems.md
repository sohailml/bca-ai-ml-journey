# 🔢 Fundamentals of Computers & Digital Systems - Unit 4: Introduction to Number Systems

> **Course:** BCA - Semester 1  
> **Topic:** Binary, Decimal, Octal, Hexadecimal & All Conversions (Including Shortcuts)  

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [Number System Overview](#-2-number-system-overview)
3. [Binary Number System (Base-2)](#-3-binary-number-system-base-2)
4. [Decimal Number System (Base-10)](#-4-decimal-number-system-base-10)
5. [Octal Number System (Base-8)](#-5-octal-number-system-base-8)
6. [Hexadecimal Number System (Base-16)](#-6-hexadecimal-number-system-base-16)
7. [Conversion via Decimal (PDF Method)](#-7-conversion-via-decimal-pdf-method)
8. [Direct Conversions (Shortcut Methods - Exam Important)](#-8-direct-conversions-shortcut-methods---exam-important)
9. [Arithmetic Operations on Binary Numbers](#-9-arithmetic-operations-on-binary-numbers)
10. [1's and 2's Complement](#-10-1s-and-2s-complement)
11. [Summary & Q&A](#-11-summary--qa)

---

## 📌 1. Introduction & Objectives

Number systems mathematics aur computing ka foundation hain. Computer science mein 4 key systems primarily use hote hain:
1.  **Binary (Base-2):** 0, 1
2.  **Decimal (Base-10):** 0-9
3.  **Octal (Base-8):** 0-7
4.  **Hexadecimal (Base-16):** 0-9, A-F

**Objectives:**
*   Number system ka concept aur base ki significance samajhna.
*   Conversions karna (Binary, Decimal, Octal, Hexadecimal).
*   Binary arithmetic operations solve karna.

---

## 🗂️ 2. Number System Overview

| System | Base | Digits Used | Example |
| :--- | :--- | :--- | :--- |
| **Decimal** | 10 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 | \((111)_{10}\), \((28.123)_{10}\) |
| **Binary** | 2 | 0, 1 | \((101)_2\), \((1010.1001)_2\) |
| **Octal** | 8 | 0, 1, 2, 3, 4, 5, 6, 7 | \((346)_8\), \((45.523)_8\) |
| **Hexadecimal** | 16 | 0-9, A(10), B(11), C(12), D(13), E(14), F(15) | \((2DF)_{16}\), \((1D4F)_{16}\) |

---

## 💻 3. Binary Number System (Base-2)

Binary digits ko **"bits"** kehte hain. Binary mein sirf do digits hote hain: **0** (off/false) aur **1** (on/true).

*   **Place Value System:** Har digit ki position ek specific power of 2 represent karti hai (right se left).
*   **Example:** \((10110)_2 = (1 \times 2^4) + (0 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) = 16 + 0 + 4 + 2 + 0 = (22)_{10}\).
*   **Nibble:** 4 bits ka group.

**Binary Table (0-15):**
| Dec | Bin | Dec | Bin |
| :--- | :--- | :--- | :--- |
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | 10 | 1010 |
| 3 | 0011 | 11 | 1011 |
| 4 | 0100 | 12 | 1100 |
| 5 | 0101 | 13 | 1101 |
| 6 | 0110 | 14 | 1110 |
| 7 | 0111 | 15 | 1111 |

---

## 🔟 4. Decimal Number System (Base-10)

Ye sabse common system hai jo hum daily life mein use karte hain. Isme 10 digits hote hain (0-9). Har digit ki position 10 ki power represent karti hai.

*   **Example:** \(986 = 9 \times 10^2 + 8 \times 10^1 + 6 \times 10^0 = 900 + 80 + 6 = 986\).

---

## 8️⃣ 5. Octal Number System (Base-8)

Octal system mein 8 digits hote hain: 0, 1, 2, 3, 4, 5, 6, 7. Har digit ki position 8 ki power represent karti hai.
*   **Example:** \((346)_8 = 3 \times 8^2 + 4 \times 8^1 + 6 \times 8^0 = 192 + 32 + 6 = (230)_{10}\).
*   **Use:** Unix file permissions mein use hota hai.

---

## 🔠 6. Hexadecimal Number System (Base-16)

Hexadecimal system mein 16 symbols hote hain: 0-9 aur A-F (A=10, B=11, C=12, D=13, E=14, F=15).
*   **Use:** Memory addresses, color codes (#FF0000), binary data compact representation.

---

## 🔄 7. Conversion via Decimal (PDF Method)

### 7.1 Binary to Decimal
**Rule:** Har binary digit ko uski position ke power of 2 se multiply karo aur add karo.
*   **Example:** \((10010)_2 = (1 \times 16) + (0 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1) = 16 + 0 + 0 + 2 + 0 = (18)_{10}\).

### 7.2 Decimal to Binary
**Rule:** Decimal number ko 2 se repeatedly divide karo jab tak quotient 1 na ho jaye. Remainders ko neeche se upar (reverse order) likho.
*   **Example:** Convert \((30)_{10}\) to binary.
    *   \(30 \div 2 = 15\) rem **0**
    *   \(15 \div 2 = 7\) rem **1**
    *   \(7 \div 2 = 3\) rem **1**
    *   \(3 \div 2 = 1\) rem **1**
    *   \(1 \div 2 = 0\) rem **1**
    *   **Answer:** \((11110)_2\).

### 7.3 Octal to Decimal
**Rule:** Right se left har digit ko \(8^0, 8^1, 8^2...\) se multiply karo aur add karo.
*   **Example:** \((346)_8 = (3 \times 64) + (4 \times 8) + (6 \times 1) = 192 + 32 + 6 = (230)_{10}\).

### 7.4 Decimal to Octal
**Rule:** Decimal number ko 8 se repeatedly divide karo, remainders ko reverse order mein likho.
*   **Example:** \((394)_{10}\) to Octal.
    *   \(394 \div 8 = 49\) rem **2**
    *   \(49 \div 8 = 6\) rem **1**
    *   \(6 \div 8 = 0\) rem **6**
    *   **Answer:** \((612)_8\).

### 7.5 Hex to Decimal
**Rule:** Right se left har digit ko \(16^0, 16^1, 16^2...\) se multiply karo aur add karo.
*   **Example:** \((1A3)_{16} = (1 \times 256) + (10 \times 16) + (3 \times 1) = 256 + 160 + 3 = (419)_{10}\).

### 7.6 Decimal to Hex
**Rule:** Decimal number ko 16 se repeatedly divide karo, remainders ko reverse order mein likho (10-15 ko A-F mein convert karo).
*   **Example:** \((314)_{10}\) to Hex.
    *   \(314 \div 16 = 19\) rem **10 (A)**
    *   \(19 \div 16 = 1\) rem **3**
    *   \(1 \div 16 = 0\) rem **1**
    *   **Answer:** \((13A)_{16}\).

---

## ⚡ 8. Direct Conversions (Shortcut Methods - Exam Important)

> [!IMPORTANT]
> PDF mein ye direct methods nahi diye hain, par exams mein **Binary ↔ Octal** aur **Binary ↔ Hex** ke direct questions bahut aate hain. Ye shortcut methods sabse fast hain.

### 8.1 Binary to Octal (3-bit grouping)
**Rule:** Binary digits ko right se left **3-3 ke group** mein baanto. Har group ko octal digit mein convert karo.
*   **Example:** Convert \((110101)_2\) to Octal.
    *   Grouping: `110` | `101`
    *   Convert: `110` = 6, `101` = 5
    *   **Answer:** \((65)_8\)

### 8.2 Octal to Binary (3-bit expansion)
**Rule:** Har octal digit ko **3-bit binary** mein convert karo aur jod do.
*   **Example:** Convert \((65)_8\) to Binary.
    *   `6` = `110`, `5` = `101`
    *   **Answer:** \((110101)_2\)

### 8.3 Binary to Hexadecimal (4-bit grouping)
**Rule:** Binary digits ko right se left **4-4 ke group** mein baanto. Har group ko hex digit mein convert karo.
*   **Example:** Convert \((11010110)_2\) to Hex.
    *   Grouping: `1101` | `0110`
    *   Convert: `1101` = D, `0110` = 6
    *   **Answer:** \((D6)_{16}\)

### 8.4 Hexadecimal to Binary (4-bit expansion)
**Rule:** Har hex digit ko **4-bit binary** mein convert karo aur jod do.
*   **Example:** Convert \((D6)_{16}\) to Binary.
    *   `D` = `1101`, `6` = `0110`
    *   **Answer:** \((11010110)_2\)

---

## ➕ 9. Arithmetic Operations on Binary Numbers

### 9.1 Binary Addition
**Rules:** \(0+0=0\), \(0+1=1\), \(1+0=1\), \(1+1=10\) (0 likho, 1 carry).
*   **Example:**
    ```
      1101  (13)
    + 0101  (5)
    -------
     10010  (18)
    ```

### 9.2 Binary Subtraction
**Rules:** \(0-0=0\), \(1-0=1\), \(1-1=0\), \(0-1=1\) (1 borrow from next).
*   **Example:**
    ```
      1101  (13)
    - 0110  (6)
    -------
      0111  (7)
    ```

### 9.3 Binary Multiplication
**Rules:** \(0 \times 0=0\), \(0 \times 1=0\), \(1 \times 0=0\), \(1 \times 1=1\).
*   **Example:**
    ```
        110  (6)
      x 101  (5)
      -----
        110
       000
      110
      -----
     11110  (30)
    ```

### 9.4 Binary Division
Decimal division jaisa hi hota hai.
*   **Example:** \(11010 \div 101 = 101\) (Quotient), Remainder 1.

---

## 🔄 10. 1's and 2's Complement

### 10.1 1's Complement
**Rule:** Har bit ko flip karo (0 ko 1, 1 ko 0).
*   **Example:** 1's complement of \((11010)_2\) is \((00101)_2\).

### 10.2 2's Complement
**Rule:** Pehle 1's complement nikaalo, phir result mein 1 add karo (rightmost bit par).
*   **Example:** 2's complement of \((11010)_2\).
    *   1's: `00101`
    *   Add 1: `00101 + 1 = 00110`
    *   **Answer:** \((00110)_2\).

---

## 📝 11. Summary & Q&A

### Summary
*   **Binary (Base-2):** 0,1.
*   **Decimal (Base-10):** 0-9.
*   **Octal (Base-8):** 0-7.
*   **Hex (Base-16):** 0-9, A-F.
*   **Conversions:** Decimal ke through (PDF method) aur Direct Shortcuts (3-bit for Octal, 4-bit for Hex).
*   **Binary Arithmetic:** Addition, Subtraction, Multiplication, Division.
*   **Complements:** 1's (flip), 2's (flip + 1).

### Self-Assessment Questions (Quick Answers)
1.  **Decimal equivalent of "10101"?** \(16+4+1 = 21\).
2.  **Nibble?** 4 bits.
3.  **Flipping bit represents?** Negation (1's complement).
4.  **Place value of rightmost decimal digit?** Ones (units).
5.  **Decimal equivalent of "1011"?** \(8+0+2+1 = 11\).
6.  **"C" in hex?** 12.
7.  **Hex "1F" to decimal?** \(1 \times 16 + 15 \times 1 = 31\).

### Terminal Questions (Hints)
*   **Q: Compare binary, decimal, octal, hexadecimal.** (Use the table in Section 2).
*   **Q: Steps for binary to decimal?** (Multiply by powers of 2, add).
*   **Q: Binary subtraction vs addition?** (Addition carries over, subtraction borrows).
*   **Q: 1's and 2's complement of "110010"?** 1's: `001101`, 2's: `001110`.
*   **Q: Hex "1A3" to binary and decimal?** Decimal: 419. Binary: `0001 1010 0011`.
*   **Q: Octal system explain?** (Base-8, digits 0-7, relate to binary as 3 bits).
*   **Q: Decimal 243 to binary, octal, hex?** Binary: `11110011`, Octal: `363`, Hex: `F3`.

---
> **💡 Bhai ka Gyan:** Exam mein conversion questions (Binary ↔ Decimal, Binary ↔ Octal/Hex) aur Binary Arithmetic (Addition/Subtraction) ke questions pakke aate hain. 1's aur 2's complement nikalna zarur aana chahiye. Table yaad rakho (Binary 0-15, Hex 0-F) aur practice karte raho! All the best!
