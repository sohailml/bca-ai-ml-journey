# 🔢 Fundamentals of Computers & Digital Systems - Unit 4: Introduction to Number Systems

> **Course:** BCA - Semester 1  
> **Topic:** Binary, Decimal, Octal, Hexadecimal & Conversions  

---

## 📑 Table of Contents
1. [Introduction & Objectives](#-1-introduction--objectives)
2. [Number System Overview](#-2-number-system-overview)
3. [Binary Number System (Base-2)](#-3-binary-number-system-base-2)
4. [Binary to Decimal Conversion](#-4-binary-to-decimal-conversion)
5. [Decimal to Binary Conversion](#-5-decimal-to-binary-conversion)
6. [Arithmetic Operations on Binary Numbers](#-6-arithmetic-operations-on-binary-numbers)
7. [1's and 2's Complement](#-7-1s-and-2s-complement)
8. [Decimal Number System (Base-10)](#-8-decimal-number-system-base-10)
9. [Conversion from Other Systems to Decimal](#-9-conversion-from-other-systems-to-decimal)
10. [Conversion from Decimal to Other Systems](#-10-conversion-from-decimal-to-other-systems)
11. [Octal Number System (Base-8)](#-11-octal-number-system-base-8)
12. [Hexadecimal Number System (Base-16)](#-12-hexadecimal-number-system-base-16)
13. [Summary & Q&A](#-13-summary--qa)

---

## 📌 1. Introduction & Objectives

Number systems mathematics aur computing ka foundation hain. Ye quantities ko represent aur manipulate karne ka universal language hain. Basic arithmetic se lekar complex computer programming tak, ye har jagah essential hain.

**Number System kya hai?** Ek structured way jisme hum numerical values ko symbols ya digits ke set se express karte hain. In symbols ko predefined rules ke according manipulate karke arithmetic aur logical operations perform kiye jate hain.

Computer science mein 4 key systems primarily use hote hain:
1.  **Binary (Base-2):** 0, 1
2.  **Decimal (Base-10):** 0-9
3.  **Octal (Base-8):** 0-7
4.  **Hexadecimal (Base-16):** 0-9, A-F

**Objectives:**
*   Number system ka concept define karna.
*   Base ki significance explain karna.
*   Binary ko decimal mein aur decimal ko binary, octal, hexadecimal mein convert karna.
*   Binary, decimal, octal, aur hexadecimal systems mein simple arithmetic operations solve karna.
*   Conversion chart/table create karna jo charon systems ka correspondence dikhaye.

---

## 🗂️ 2. Number System Overview

Number system numbers ko represent karne ke liye use hota hai. Har system ka ek base (radix) hota hai.

| System | Base | Digits Used | Example |
| :--- | :--- | :--- | :--- |
| **Decimal** | 10 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 | \((111)_{10}\), \((28.123)_{10}\) |
| **Binary** | 2 | 0, 1 | \((101)_2\), \((1010.1001)_2\) |
| **Octal** | 8 | 0, 1, 2, 3, 4, 5, 6, 7 | \((346)_8\), \((45.523)_8\) |
| **Hexadecimal** | 16 | 0-9, A(10), B(11), C(12), D(13), E(14), F(15) | \((2DF)_{16}\), \((1D4F)_{16}\) |

---

## 💻 3. Binary Number System (Base-2)

Binary digits ko **"bits"** kehte hain. Ye computer ke fundamental building blocks hain. Binary mein sirf do digits hote hain: **0** (off/false) aur **1** (on/true).

### 3.1 Importance of Bits
*   **Data Representation:** Sab kuch (text, images, audio, video) 0s aur 1s mein convert hota hai.
*   **Information Processing:** CPU bits par arithmetic aur logical operations karta hai.
*   **Memory:** RAM aur storage devices bits mein data store karte hain.
*   **Communication:** Data transmission ke time bits ki stream banti hai.
*   **Logic and Decision Making:** AND, OR, NOT, XOR jaise logical operations bits par based hote hain.
*   **Addressing and Storage:** Memory locations ko address karne ke liye bits use hote hain.

### 3.2 Binary Place Value System
Har digit ki position ek specific power of 2 represent karti hai (right se left).

**Example:** \((10110)_2\)
*   Rightmost digit (0) = \(2^0 = 1\)
*   Next (1) = \(2^1 = 2\)
*   Next (1) = \(2^2 = 4\)
*   Next (0) = \(2^3 = 8\)
*   Leftmost (1) = \(2^4 = 16\)

**Calculation:**
\[
(10110)_2 = (1 \times 2^4) + (0 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)
\]
\[
= 16 + 0 + 4 + 2 + 0 = (22)_{10}
\]

### 3.3 Binary Number Table
| Decimal | Binary | Decimal | Binary |
| :--- | :--- | :--- | :--- |
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | 10 | 1010 |
| 3 | 0011 | 11 | 1011 |
| 4 | 0100 | 12 | 1100 |
| 5 | 0101 | 13 | 1101 |
| 6 | 0110 | 14 | 1110 |
| 7 | 0111 | 15 | 1111 |

> **Note:** LSB (Least Significant Bit) rightmost bit hota hai, MSB (Most Significant Bit) leftmost bit hota hai. 4 bits ke group ko **Nibble** kehte hain.

---

## 🔄 4. Binary to Decimal Conversion

**Rule:** Har binary digit ko uski position ke power of 2 se multiply karo aur add karo.

**Formula:** \(D = (b_{n-1} \times 2^{n-1}) + ... + (b_1 \times 2^1) + (b_0 \times 2^0)\)

**Example:** Convert \((10010)_2\) to decimal.
\[
(10010)_2 = (1 \times 2^4) + (0 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)
\]
\[
= 16 + 0 + 0 + 2 + 0 = (18)_{10}
\]

---

## 🔄 5. Decimal to Binary Conversion

**Rule:** Decimal number ko 2 se repeatedly divide karo jab tak quotient 1 na ho jaye. Remainders ko neeche se upar (reverse order) likho.

**Example:** Convert \((30)_{10}\) to binary.
*   \(30 \div 2 = 15\) remainder **0**
*   \(15 \div 2 = 7\) remainder **1**
*   \(7 \div 2 = 3\) remainder **1**
*   \(3 \div 2 = 1\) remainder **1**
*   \(1 \div 2 = 0\) remainder **1**

Remainders ko neeche se upar padho: **11110**

**Answer:** \((30)_{10} = (11110)_2\)

---

## ➕ 6. Arithmetic Operations on Binary Numbers

Binary arithmetic rightmost bit (LSB) se shuru hoti hai.

### 6.1 Binary Addition
**Rules:**
*   \(0 + 0 = 0\)
*   \(0 + 1 = 1\)
*   \(1 + 0 = 1\)
*   \(1 + 1 = 10\) (0 likho, 1 carry karo)

**Example:**
```
  1101  (13 in decimal)
+ 0101  (5 in decimal)
-------
 10010  (18 in decimal)
```
*Explanation:* Rightmost: \(1+1=10\) (0 likha, 1 carry). Next: \(0+0+1(carry)=1\). Next: \(1+1=10\) (0 likha, 1 carry). Leftmost: \(1+0+1(carry)=10\).

### 6.2 Binary Subtraction
**Rules:**
*   \(0 - 0 = 0\)
*   \(1 - 0 = 1\)
*   \(1 - 1 = 0\)
*   \(0 - 1 = 1\) (1 borrow from next higher bit)

**Example:**
```
  1101  (13 in decimal)
- 0110  (6 in decimal)
-------
  0111  (7 in decimal)
```
*Explanation:* Rightmost: \(1-0=1\). Next: \(0-1\) (borrow 1) = 1. Next: \(0-1\) (borrow 1) = 1. Leftmost: \(1-0=1\).

### 6.3 Binary Multiplication
**Rules:**
*   \(0 \times 0 = 0\)
*   \(0 \times 1 = 0\)
*   \(1 \times 0 = 0\)
*   \(1 \times 1 = 1\)

**Example:**
```
    110  (6 in decimal)
  x 101  (5 in decimal)
  -----
    110
   000
  110
  -----
 11110  (30 in decimal)
```

### 6.4 Binary Division
Decimal division jaisa hi hota hai, bas 0 aur 1 use karte hain.

**Example:** \(11010 \div 101\)
```
        101  (Quotient)
      ______
  101 ) 11010
        101
        ---
         110
         101
         ---
           1  (Remainder)
```

---

## 🔄 7. 1's and 2's Complement

Ye methods negative binary numbers represent karne aur arithmetic operations perform karne ke liye use hote hain.

### 7.1 1's Complement
**Rule:** Har bit ko flip karo (0 ko 1, 1 ko 0).

**Example:** Find 1's complement of \((11010)_2\).
*   Original: `1 1 0 1 0`
*   Flip: `0 0 1 0 1`
*   **Answer:** \((00101)_2\)

### 7.2 2's Complement
**Rule:** Pehle 1's complement nikaalo, phir result mein 1 add karo (rightmost bit par).

**Example:** Find 2's complement of \((11010)_2\).
*   1's complement: `0 0 1 0 1`
*   Add 1: `0 0 1 0 1 + 1 = 0 0 1 1 0`
*   **Answer:** \((00110)_2\)

> [!NOTE]
> *   1's complement = Flip all bits.
> *   2's complement = Flip all bits + 1.
> *   Nibble = 4 bits ka group.

---

## 🔟 8. Decimal Number System (Base-10)

Ye sabse common system hai jo hum daily life mein use karte hain. Isme 10 digits hote hain: 0,1,2,3,4,5,6,7,8,9. Har digit ki position 10 ki power represent karti hai.

**Example 1:** \(986\)
\[
= 9 \times 10^2 + 8 \times 10^1 + 6 \times 10^0
\]
\[
= 9 \times 100 + 8 \times 10 + 6 \times 1
\]
\[
= 900 + 80 + 6 = 986
\]

**Example 2:** \(450.36\)
\[
= 4 \times 10^2 + 5 \times 10^1 + 0 \times 10^0 + 3 \times 10^{-1} + 6 \times 10^{-2}
\]
\[
= 400 + 50 + 0 + 0.3 + 0.06 = 450.36
\]

---

## 🔄 9. Conversion from Other Systems to Decimal

### 9.1 Binary to Decimal
Steps:
1.  Binary number likho.
2.  Right se left har digit ko \(2^0, 2^1, 2^2...\) se multiply karo.
3.  Sab results add karo.

**Example:** \((1101)_2\) to decimal.
*   \(1 \times 2^3 = 8\)
*   \(1 \times 2^2 = 4\)
*   \(0 \times 2^1 = 0\)
*   \(1 \times 2^0 = 1\)
*   **Sum = 8 + 4 + 0 + 1 = 13**
*   **Answer:** \((1101)_2 = (13)_{10}\)

### 9.2 Octal to Decimal
Steps:
1.  Octal number likho.
2.  Right se left har digit ko \(8^0, 8^1, 8^2...\) se multiply karo.
3.  Sab results add karo.

**Example:** \((346)_8\) to decimal.
*   \(3 \times 8^2 = 3 \times 64 = 192\)
*   \(4 \times 8^1 = 4 \times 8 = 32\)
*   \(6 \times 8^0 = 6 \times 1 = 6\)
*   **Sum = 192 + 32 + 6 = 230**
*   **Answer:** \((346)_8 = (230)_{10}\)

### 9.3 Hexadecimal to Decimal
Steps:
1.  Hex number likho.
2.  A=10, B=11, C=12, D=13, E=14, F=15 assign karo.
3.  Right se left har digit ko \(16^0, 16^1, 16^2...\) se multiply karo.
4.  Sab results add karo.

**Example:** \((1A3B)_{16}\) to decimal.
*   B (11) \(\times 16^0 = 11 \times 1 = 11\)
*   3 \(\times 16^1 = 3 \times 16 = 48\)
*   A (10) \(\times 16^2 = 10 \times 256 = 2560\)
*   1 \(\times 16^3 = 1 \times 4096 = 4096\)
*   **Sum = 11 + 48 + 2560 + 4096 = 6725**
*   **Answer:** \((1A3B)_{16} = (6725)_{10}\)

---

## 🔄 10. Conversion from Decimal to Other Systems

### 10.1 Decimal to Octal
**Rule:** Decimal number ko 8 se repeatedly divide karo, remainders ko reverse order mein likho.

**Example:** Convert \((394)_{10}\) to octal.
*   \(394 \div 8 = 49\) remainder **2**
*   \(49 \div 8 = 6\) remainder **1**
*   \(6 \div 8 = 0\) remainder **6**

Remainders neeche se upar: **612**

**Answer:** \((394)_{10} = (612)_8\)

### 10.2 Decimal to Hexadecimal
**Rule:** Decimal number ko 16 se repeatedly divide karo, remainders ko reverse order mein likho. Remainder 10-15 ko A-F mein convert karo.

**Example:** Convert \((314)_{10}\) to hexadecimal.
*   \(314 \div 16 = 19\) remainder **10 (A)**
*   \(19 \div 16 = 1\) remainder **3**
*   \(1 \div 16 = 0\) remainder **1**

Remainders neeche se upar: **1 3 A**

**Answer:** \((314)_{10} = (13A)_{16}\)

---

## 8️⃣ 11. Octal Number System (Base-8)

Octal system mein 8 digits hote hain: 0,1,2,3,4,5,6,7. Har digit ki position 8 ki power represent karti hai.

**Example:** \((346)_8\)
*   \(3 \times 8^2 = 192\)
*   \(4 \times 8^1 = 32\)
*   \(6 \times 8^0 = 6\)
*   Sum = 230

**Use:** Unix file permissions mein octal ka use hota hai.

---

## 🔠 12. Hexadecimal Number System (Base-16)

Hexadecimal (hex) system mein 16 symbols hote hain: 0-9 aur A-F (A=10, B=11, C=12, D=13, E=14, F=15).

| Decimal | Hex | Decimal | Hex |
| :--- | :--- | :--- | :--- |
| 0 | 0 | 8 | 8 |
| 1 | 1 | 9 | 9 |
| 2 | 2 | 10 | A |
| 3 | 3 | 11 | B |
| 4 | 4 | 12 | C |
| 5 | 5 | 13 | D |
| 6 | 6 | 14 | E |
| 7 | 7 | 15 | F |

### 12.1 Hexadecimal to Decimal Conversion
**Example:** Convert \((1A3)_{16}\) to decimal.
*   3 \(\times 16^0 = 3 \times 1 = 3\)
*   A (10) \(\times 16^1 = 10 \times 16 = 160\)
*   1 \(\times 16^2 = 1 \times 256 = 256\)
*   **Sum = 3 + 160 + 256 = 419**
*   **Answer:** \((1A3)_{16} = (419)_{10}\)

**Use:** Memory addresses, color codes (#FF0000), binary data compact representation.

---

## 📝 13. Summary & Q&A

### Summary
*   **Number System:** Numbers represent karne ka tarika.
*   **Binary (Base-2):** 0, 1. Computers ki language.
*   **Decimal (Base-10):** 0-9. Daily life mein use.
*   **Octal (Base-8):** 0-7. Unix permissions mein.
*   **Hex (Base-16):** 0-9, A-F. Memory addresses mein.
*   **Conversions:** Binary to Decimal (power of 2 se multiply), Decimal to Binary (2 se divide), Octal/Hex similar methods.
*   **Binary Arithmetic:** Addition, Subtraction, Multiplication, Division (decimal jaisa, bas 0-1 rules).
*   **Complements:** 1's (flip bits), 2's (flip + 1).

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
*   **Q: Steps for binary to decimal?** (Multiply by powers of 2, add. Example: \((1101)_2 = 13\)).
*   **Q: Binary subtraction vs addition?** (Addition carries over, subtraction borrows. Example: \(1101 - 0110 = 0111\)).
*   **Q: 1's and 2's complement of "110010"?**
    *   1's: `001101`
    *   2's: `001101 + 1 = 001110`
*   **Q: Hex "1A3" to binary and decimal?**
    *   Decimal: \(1 \times 256 + 10 \times 16 + 3 \times 1 = 419\)
    *   Binary: \(1 = 0001\), \(A = 1010\), \(3 = 0011\) → `0001 1010 0011` (or `110100011`)
*   **Q: Octal system explain?** (Base-8, digits 0-7, relate to binary as 3 bits per octal digit).
*   **Q: Decimal 243 to binary, octal, hex?**
    *   Binary: \(243 \div 2\) repeatedly → `11110011`
    *   Octal: \(243 \div 8\) repeatedly → `363`
    *   Hex: \(243 \div 16\) repeatedly → `F3`

---
> **💡 Bhai ka Gyan:** Exam mein conversion questions (Binary ↔ Decimal, Decimal → Octal/Hex) aur Binary Arithmetic (Addition/Subtraction) ke questions pakke aate hain. 1's aur 2's complement nikalna zarur aana chahiye. Table yaad rakho (Binary 0-15, Hex 0-F) aur practice karte raho!
