# day 6 of my journey
# function
a = 5
b = 4
sum = a + b 
print(sum)

# # suppose more line of code

a = 9
b = 8
sum = a+b
print(sum)

# we use function
def cal_sum(a,b): # function difinition
    sum = a+b
    return sum

print(cal_sum(8,2))

def cal_sub(a,b): #a,b are parameter
    sub = a-b
    print(sub)
    return sub

cal_sub(4,2) #fuction call 4,2 are arguments

def cal_mul(a,b):
    return a*b  #return output
print(cal_mul(2,4))

def prt():
    print("hello sohail")

prt()
prt()
prt()

# average of 3 number
def avg(a,b,c):
    average = (a+b+c)/3
    print(average)
    return average

x = avg(6,2,1)
print(x)

# type of function
# built in function
print("sohail","ansari", sep="#$") # default sep =" "
print("languge",end="\t") # default end = \n
print("python")

x = 'sohail'
print(len(x))  # len function
print(type(x)) # type function
for i in range(1,11):  # range funvtion
    print(i)

# default parameter
def prod(a=1,b=1):
    print(a*b)
    return a*b
prod()

# recursion - when function start calling itslef 
def show(n):  # it is same as loops
    if (n==0):     #base case
        return
    print(n)
    show(n-1)
    print("end")
show(5) 

#faactorial using recursion
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n

print(fact(6))
