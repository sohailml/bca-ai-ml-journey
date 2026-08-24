# Day 1: Python Basics

## 🖨️ Print Function
The `print()` function displays output on the screen.

**Example:**
```python
print("Hello, World!")
Output: Hello, World!

You can use both double quotes (" ") and single quotes (' ') inside print().

📦 Variables
A variable is a container that stores data.

Example:

python
name = "Sohail"
age = 25
Rules for Variable Names:
Cannot start with a number (e.g., 5name is invalid)

Cannot contain special symbols like #, $, %

Python is case-sensitive — name and Name are different.

📊 Data Types in Python
Data Type	Description	Example
String (str)	Text inside quotes	"Sohail", "22"
Integer (int)	Whole numbers	5, -1, 0
Float	Decimal numbers	50.22, 3.14
Boolean (bool)	True or False	True, False
NoneType	Empty or nothing	None
⚠️ Important Notes:
True, False, and None always start with a capital letter.

Python is case-sensitive — true is not the same as True.

🔑 Keywords
Reserved words in Python that cannot be used as variable names.

Common Keywords:

text
and, as, assert, break, class, continue, def, del, elif, else, except,
finally, for, from, False, global, if, import, in, is, lambda, None,
nonlocal, not, or, pass, raise, return, True, try, while, with, yield
💬 Comments in Python
Comments are used to make code more readable and are ignored by Python.

Single-line comment:

python
# This is a comment
print("Hello")
Multi-line comment (Shortcut): Ctrl + /

📌 Alternate multi-line comment: Use """ """ or ''' ''' (triple quotes).

➕ Arithmetic Operations
Python follows the BODMAS rule.

Example:

python
a = 96
b = 4
print(a + b)  # Output: 100
🔢 Operators in Python
Arithmetic Operators
Operator	Description	Example
+	Addition	a + b
-	Subtraction	a - b
*	Multiplication	a * b
/	Division (float)	a / b
%	Modulus (remainder)	a % b
**	Exponentiation	a ** b
Relational / Comparison Operators
Operator	Description	Example
==	Equal to	a == b
!=	Not equal to	a != b
>	Greater than	a > b
<	Less than	a < b
>=	Greater than or equal to	a >= b
<=	Less than or equal to	a <= b
Assignment Operators
Operator	Description	Example
=	Assign value	a = 5
+=	Add and assign	a += 3
-=	Subtract and assign	a -= 2
*=	Multiply and assign	a *= 4
/=	Divide and assign	a /= 2
%=	Modulus and assign	a %= 3
**=	Power and assign	a **= 2
Logical Operators
Operator	Description
and	Returns True if both are true
or	Returns True if at least one is true
not	Reverses the boolean value
🔄 Type Conversion & Casting
Implicit Type Conversion (Automatic)
Python automatically converts one data type to another.

Example:

python
a = 1       # int
b = 2.0     # float
sum = a + b
print(sum)  # Output: 3.0 (float)
⚠️ Error Case:

python
a = 1
b = "2"
print(a + b)  # ❌ TypeError
Explicit Type Casting (Manual)
We can force convert using int(), float(), str(), etc.

Example:

python
a = 1
b = "2"
c = int(b)      # Convert string to int
print(a + c)    # Output: 3
⌨️ Taking Input from User
Syntax:

python
input("Enter something: ")
⚠️ Note: The result of input() is always a string.

To Convert Input:
python
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # Convert to int
height = float(input("Enter height: ")) # Convert to float
📌 Summary
print() → Output

input() → Input (always string)

# → Single-line comment

int(), float(), str() → Type casting

Python is case-sensitive

True, False, None → Capital first letter

Variables cannot start with numbers or special symbols

✍️ Created by: Sohail Ansari
📅 Date: 23 August 2026
🚀 Goal: Build strong Python foundation for AI/ML

#BuildInPublic #Python #BCA #AI #100DaysOfCode
