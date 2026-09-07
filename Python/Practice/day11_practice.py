"""Q1: Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average."""
# class student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name = name
#         self.marks1= marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def average(self):
#         avg = (self.marks1+self.marks2+self.marks3)/3
#         print(self.name,"your average is ",avg)

# s1 = student("sohail",75,85,65)
# s1.average()
"""second solution"""
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def average(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("hi",self.name,"your average score is",sum/3)

# s1 = student("sohail",[98,97,96])
# s1.average()


"""Q2: Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance."""           
# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def debit(self,amount):
#         self.balance -=amount
#         print(amount,"is debit from your account")
#         print("your balance is ",self.balance)

#     def credit(self,amount):
#         self.balance +=amount
#         print(amount,"is credit to your account")
#         print("your balance is ",self.balance)

#     def get_balance(self):
#         print("your total balnce is",self.balance)


# acc1 = Account(40000,71008100005928)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.debit(24000)
# acc1.credit(3.44)
# acc1.debit(344)
# acc1.get_balance()
