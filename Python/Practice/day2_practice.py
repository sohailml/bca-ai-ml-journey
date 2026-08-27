"""Question 1: Write a Program to input user name and print its length"""
Name = input("Enter your name: ")
print("your name length is",len(Name))


"""Question 2: Write a program to find occuarence of $ in string"""
str = "sohail $ is a good boy $"
print("$ is occuring",str.count("$"),"times in the string")


"""Question 3: WRite a program to check a number is even or odd"""
num = int(input("Enter a number: "))
if (num % 2 == 0):
    print(num,"is an even number")

else:
    print(num,"is an odd number")


"""Question 4: Write a program to find the greatest of 3 numbers entered by user"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1>num2 and num1>num3):
    print(num1,"is the greatest number")

elif(num2>num3 and num2>num1):
    print(num2,"is the greatest number")

else:
    print(num3,"is the greatest number")


"""Question 5: Write a program to check a number is multiple of 7"""
num = int(input("Enter a number: "))
if (num %7 ==0):
    print(num,"is a multiple of 7")
else:
    print(num,"is not a multiple of 7")


"""Question 6: Ek, string s = "hello" lo. Isko aise print karo ki output aaye: "h e l l o" (har character ke beech space)."""
s = "hello"
print(s[0],s[1],s[2],s[3],s[4])


"""Question 7: Kya "10" > "2" ka result True aayega ya False?"""
print("10">"2") # false kyunki ye integer nahi hai string hai and string alphabtically dekha jata hai so 10 ka pehla 1 and 2 ka 2 so 1 is less then 2 so false


# basic test - write a program Question

"""Question 1:[Palindrome Checker with a Twist] User se ek string input lo. Program check kare: Agar string palindrome hai (ulta seedha same, e.g., "madam"),
toh "Yes, it's a palindrome" print karo. Agar nahi hai, toh check karo ki agar hum pehle aur aakhri character hata den toh palindrome ban jaata hai?
Agar haan, toh "Almost palindrome" print karo. Otherwise "Not a palindrome" print karo."""
str = input("enter some word: ")
if (str[0:] == str[::-1]):
    print("this is palindrome")

elif (str[1:len(str)-1] == str[-2:-len(str):-1]):
    print("almost palindrome")
else:
    print("this not palindrome")


"""Question 2:[Vowels vs Consonants – Nested Logic] User se ek single character input lo (assume karo ki user ne ek hi letter diya).
Nested if-else use karke: Agar charac ter alphabet hai ('a' to 'z' ya 'A' to 'Z'), toh check karo ki vowel hai ya consonant. 
Vowel hai toh "Vowel" print karo, consonant hai toh "Consonant". Agar alphabet nahi hai, toh "Not a letter" print karo."""
alph = input("Enter a alphabet: ")
if (len(alph)>1):
    print("enter only one character")

elif ("a"<=alph<="z") or ("A"<=alph<="Z"):
    if alph in "aeiouAEIOU":
        print("vowel")
    else:
        print("consonant")

else:
    print("not a alphabet")


"""Question 3:[The "10" > "2" Mystery] Bina code run kiye , batao ki "10" > "2" ka output kya hoga? ANS - False
Ab ek program likho jo user se do strings (numbers ki tarah) input le, 
aur unko numeric value ke hisaab se compare kare (i.e., "10" ko 10 maane, "2" ko 2). 
Agar pehla bada hai toh "First is greater", chhota hai toh "Second is greater", equal hai toh "Equal" print karo."""
num1=input("enter first number: ")
num2=input("enter second  number: ")

if (int(num1)>int(num2)):
    print("first number is greater")
elif (int(num1)<int(num2)):
    print("second number is greater")
else:
    print("equal")


"""Question 4:[Username Validator – Triple Condition] 
User se ek username input lo. Program check kare (nested if use karo):
Agar username ki length 8 se kam hai, toh directly "Too short" print karo. 
Agar length 8 ya zyada hai, toh check karo ki username "@" contain karta hai ya nahi.
Agar contain karta hai, toh check karo ki username " " (space) contain karta hai ya nahi.
Agar space bhi hai, toh "Invalid: contains @ and space".
Agar space nahi hai, toh "Valid username".
Agar "@" nahi hai, toh "Invalid: missing @"."""

user = input("Enter your username: ")
if (len(user)>=8):
    if ("@" in user):
        if (" " in user):
            print("sapce not allowed")
        else:
            print("valid username")
    else:
        print("missing @")

else:
    print("too sort")


