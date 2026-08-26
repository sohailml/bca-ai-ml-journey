# Question 1: Write a Program to input user name and print its length
Name = input("Enter your name: ")
print("your name length is",len(Name))

# Question 2: Write a program to find occuarence of $ in string
str = "sohail $ is a good boy $"
print("$ is occuring",str.count("$"),"times in the string")

# Question 3: WRite a program to check a number is even or odd
num = int(input("Enter a number: "))
if (num % 2 == 0):
    print(num,"is an even number")

else:
    print(num,"is an odd number")

# Question 4: Write a program to find the greatest of 3 numbers entered by user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1>num2 and num1>num3):
    print(num1,"is the greatest number")

elif(num2>num3 and num2>num1):
    print(num2,"is the greatest number")

else:
    print(num3,"is the greatest number")

# Question 5: Write a program to check a number is multiple of 7
num = int(input("Enter a number: "))
if (num %7 ==0):
    print(num,"is a multiple of 7")
else:
    print(num,"is not a multiple of 7")

