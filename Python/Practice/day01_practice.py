# Question 1: Write a Program to input 2 numbers & print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("the sum of", num1, "and", num2, "is", num1 + num2)


# Question 2: WAP to input side of a square & print its area
side = float(input("Enter the side of the square in cm: "))
print("The area of the square is", side * side, "cm²")


# Question 3: WAP to input 2 floating point numbers & print their average
num1 = float(input("Enter first floating point number:"))
num2 = float(input("Enter second floating point number:"))
average = (num1 + num2)/2
print("The average of", num1, "and", num2, "is", average)


# Question 4: WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.
a = int(input("enter first number: "))
b = int(input("enter second number:"))
print(a >= b)

# 📝 Python Basics - Practice Test

# Section A: Multiple Choice Questions

# Question 1: Python mein variable name kaunsa valid nahi hai? a) my_var b) _var1 c) 2var d) var_2 ANS-B
# Question 2: ‘None’ kis data type ka hai? ANS - none type
# Question 3: Neeche diye code ka output kya hoga? print(type(True)) ANS - <class 'bool'>
# Question 4: Python case-sensitive hai. Kaunsa statement sahi hai? a) name aur Name ek hi variable hain. b) name aur Name alag-alag hain. c) Python case-sensitive nahi hai. d) Sirf uppercase variable allowed hain. ANS-B
# Question 5: Neeche diye code mein error kyun aayega? a = 5 b = "10" c = a + b ANS - Kyunki a or b diffrent data types hai
# Question 6: Kaunsa keyword Python ka reserved word nahi hai? a) for b) while c) loop d) if ANS - loop
# Question 7: Multiline comment ke liye kaunsa syntax use hota hai? ANS- '''s''' ya """ss"""
# Question 8: print("Hello" + " " + "World") ka output kya hoga? ANS - Hello World
# Question 9: Type Casting ka example kaunsa hai?a) int("5") b) 5 + 2.0 c) str(123) d) dono a aur c ANS - d
# Question 10: Input statement input() hamesha kaunsa data type return karta hai? ANS - string

# Section B: Predict the Output

# Question 1: a=10 , b=20 so print(a+b*2) ANS - 50 
# Question 2: x = "python" y = 3 so print(x*y) ANS - pythonpythonpython
# Question 3: num = 5.5 print(int(num)) ANS - 5
# Question 4: a = True b = False print(a and b) print(a or b) ANS - False  and True
# Question 5: name = "sohail" Name = "rahul" print(name == Name) ANS - False

# Section C: Find the Error

# Question 1: 5name = "Sohail" print(5name) ANS - variable valid nahi hai error aayega
# Question 2: a = 10 b = 20 sum = a + b print(sum) ANS - no error output is 30
# Question 3: x = "5" y = 2 z = x + y print(z) ANS - cannot add diffrent data types
# Question 4: my_var = None print(type(my_var)) ANS - no erroe output Nonetype

# Section D: Write Code

# Question 1: User se do numbers input lo aur unka sum print karo. (Type casting ka dhyan rakho)
First_Number = int(input("enter first number: "))
Second_Number = int(input("enter second number: "))
print(First_Number+Second_Number)

# Question 2: Ek variable age banayein jisme user apni age integer me daale. Phir usko float me convert karke print karein
age = int(input("enter your age: "))
print(float(age))

# Question 3: Code likho: a = 20, b = 7.In dono ko use karke ek aisa expression likho jiska output 6 aaye
a = 20
b = 7
print(a%b)
