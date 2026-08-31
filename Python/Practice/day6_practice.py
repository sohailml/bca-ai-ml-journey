"""Q1: WAF(write a function) to print the length of a list. ( list is the parameter)"""
# def lst(list):
#     print(len(list))
#     return len(list)

# lst(["sohail",4,5,45.6])


"""Q2: WAF to print the elements of a list in a single line. ( list is the parameter)"""
# def element(list):
#     for i in list:
#         print(i)
# element(["sohail",4,5,45.6])


"""Q3: WAF to find the factorial of n. (n is the parameter)"""
# def factorial(n):
#     fact = 1
#     i = 1
#     while i<=n:
#         fact = fact*i
#         i+=1
#     print(fact)
# factorial(5)

# #or
# def facto(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#     print(fact)
# facto(6)


"""Q4: WAF to convert USD to INR."""
# def cnvt(n):
#     print(n,"USD in INR is = ",n*95)
#     return n*95
# cnvt(2)

"""Q5: WAF to identify the number n is odd or even so if number is odd it print string odd or if even so even"""


"""Q6: Write a recursive function to calculate the sum of first n natural numbers."""
# def sum_nat(n):
#     if (n==0):
#         return 0
#     else:
#         return sum_nat(n-1)+n

# print(sum_nat(5))


"""Q7: Write a recursive function to print all elements in a list.
Hint : use list & index as parameters"""
# def ele(list,idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     ele(list,idx+1)

# fruites = ["mango","orange","papita"]
# ele(fruites)

