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

#basic test - python
"""Q1. The Stepped Recursion
Ek recursive function likho print_stepped(lst, step=1) jo list ke elements ko step ke hisaab se print kare.

Default step=1 → normal order (0,1,2,3...)

Agar step=2 → index 0,2,4,... print kare

Base case handle karo (jab index list length se bahar ho).
Bina kisi loop ke, sirf recursion."""
# def print_stepped(lst, idx=0, step=1):
#     if idx >= len(lst):
#         return
#     print(lst[idx], end=" ")
#     print_stepped(lst, idx + step, step)
# print_stepped([10, 20, 30, 40, 50], step=2)


"""Q2. Reverse String – Recursive Way
Ek function reverse_str(s) likho jo string ko recursively reverse kare aur return kare.
Condition: Slicing ([::-1]) use nahi karna. Sirf concatenation (+) aur recursion.
(Hint socho: base case empty string, return last char + reverse(rest))"""
# def reverse_str(s):
#     if len(s) <= 1:
#         return s
#     return s[-1] + reverse_str(s[:-1])
# print(reverse_str("hello"))


"""Q3. Default Parameter Trap
Ek function multiply(n=1, times=1) likho jo n ko times baar multiply karke return kare (i.e., n ** times).
Par agar user sirf ek argument deta hai (e.g., multiply(3)), toh usko n maano aur times default 1 rahe.
Agar koi argument nahi deta, toh n=1, times=1 → return 1.
Twist: Function ko call karo multiply(times=3) – output kya hoga? (Bina run kiye batao aur reason do)"""    
# def multiply(n=1, times=1):
#     return(n**times)
# print(multiply(times=3))


"""Q4. The Sorted List Checker (Recursion)
Function is_sorted(lst) likho jo recursively check kare ki list ascending order mein sorted hai ya nahi.
Empty list ya single element → True
Compare first two, fir rest pe recursion.
Output predict karo: is_sorted([1, 3, 2]) kya return karega?"""
# def is_sorted(lst):
#     if len(lst) <= 1:
#         return True
#     if lst[0] > lst[1]:
#         return False
#     return is_sorted(lst[1:])
# print(is_sorted([1, 3, 2]))
# print(is_sorted([1, 2, 3]))
