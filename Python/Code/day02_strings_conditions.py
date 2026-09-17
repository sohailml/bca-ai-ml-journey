# day 2 of my jurney
str1 = "sohail"
str2 = 'ansari' #we can use single or double quotes for strings
str3 = """this is sohail's code""" # we use triple quotes or double quotes for using apostrophe

# escape sequence characters
str4 = "this is string \nthis is new line" # \n is used for new line
print(str4)

str5 = "this is string \tthis is tab space" # \t is used for tab space
print(str5)

# basic string operations
print(str1 +" "+str2) # concatenation
print(len(str1)) #length of string
print(len(str2)) 

#indexing and slicing[start index : End index : step]
print(str2[2])
print(str1[-3]) # negative indexing

print(str1[0:4]) # slicing , last index is not included
print(str1[0:]) # slicing from 0 to end
print(str1[:4]) # slicing from start to 4th index
print(str1[-3:]) # slicing with negative indexing
print(str1[-1:-6:-2]) # slicing with step 2

# string functions
str6 = "i am learning python"
print(str6.endswith("on")) # check if string ends with "on"
print(str6.endswith("am")) # check if string ends with "am"
print(str6.capitalize()) # capitalize the first letter of the string
print(str6.replace("python","java")) # replace "python" with "java"
print(str6.find("learning")) # find the index of the first occurrence of "a"
print(str6.count("q")) # count the number of occurrences of "a"

# conditional statements
a = -5
if(a > 0):
    print("a is positive")
elif(a== 0):
    print("a is zero")
else:
    print("a is negative")

# nesting of if else statements
b = 5
if(b > 0):
    if(b%2 == 0):
        print("b is positive and even")
    else:
        print("b is positive and odd")

elif(b == 0):
    print("b is zero")

else:
    print("b is negative")
