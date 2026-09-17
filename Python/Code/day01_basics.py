# first program
print("Hello, World!")

# variable
Name = "Sohail"
Age = 18
value = 99.66
Boy = True
skill = None

print("My name is",Name)
print("I am",Age,"years old")

# type of variable data
print(type(Name))  #string
print(type(Age))   #integer
print(type(value)) #float
print(type(Boy))   #boolean
print(type(skill)) #NoneType

# arithmetic operations
a = 8
b = 2
sum = a + b
difference = a - b
multiplication = a * b
division = a / b
power = a ** b
floor_division = a // b # quotient of the division
modulus = a % b # remainder of the division

print(sum)
print(difference)
print(multiplication)
print(division)
print(power)
print(floor_division)
print(modulus)

# relational operators
x = 10
y = 5
print(x > y)  # True
print(x < y)  # False
print(x == y) # False
print(x != y) # True
print(x >= y) # True
print(x <= y) # False

# assignment operators
z = 10  # assignment
z += 5  # addition assignment
z -= 3  # subtraction assignment
z *= 2  # multiplication assignment
z /= 4  # division assignment

# logical operators
p = True
q = False
print(p and q)  # False
print(p or q)   # True
print(not p)    # False

# type conversion
a1 = 10
b1 = 3.14
sum1 = a1 + b1  # implicit type conversion
print(sum1)  # 13.14

# type casting
a2 = "100"
b2 = int(a2)  # explicit type conversion
print(b2)  # 100

# input from user
name = input("Enter your name: ")
print("Hello",name)
