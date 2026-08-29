"""Q1: Print numbers from 1 to 100"""
# i = 1
# while i<=100:
#     print(i)
#     i+=1
# print("end")


"""Q2: Print numbers from 100 to 1."""
# j = 100
# while j>=1:
#     print(j)
#     j-=1
# print("end")


"""Q3: Print the multiplication table of a number n."""
# n = int(input("enter a number: "))
# i = 1
# while i<=10:
#     print(n*i)
#     i += 1
# print("end")


"""Q4: Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]"""
# num =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i = 0
# while i< len(num):
#     print(num[i])
#     i+=1


"""Q5: Search for a number x in this tuple using loop:
(1, 4, 9, 16, 25, 36, 49, 64, 81,100)"""
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# i = 0
# while tup[i] != 36:
#     print(tup[i])
#     i += 1
#     print(tup[i])

#or 
# tp = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# print(tp)
# x = int(input("what you want to search from above tuple: "))
# i = 0
# while i<len(tp):
#     if (tp[i] == x ):
#         print(x,"found at index",i)
#         break
#     else:
#         print("finding...")
#     i += 1
# print("end of loop")


"""Q6: Print the elements of the following list using a for loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]"""
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for val in num:
#     print(val)


"""Q7: Search for a number x in this tuple using for loop:
(1, 4, 9, 16, 25, 36, 49, 64, 81,100)"""
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x = int(input("what number yor want to search: "))
# ind = 0
# for val in tup:
#     if (val == x):
#         print(val,"found at index",ind)
#         break
#     ind+=1
#     print(val)


""" Q8: Print numbers from 1 to 100 using for and range()"""
# for i in range(1,101):
#     print(i)


"""Q9: Print numbers from 100 to 1 using for and range()"""
# for i in range(100,0,-1):
#     print(i)


"""Q10: Print the multiplication table of a number n. using for and range()"""
# n = int(input("enter a number: "))
# for i in range(1,11):
#     print(n*i)


"""Q11: WAP to find the sum of first n natural numbers. (using while)"""
# n = int(input("enter number: "))
# sum = 0
# i = 1
# while i<=n:
#     sum+=i
#     i += 1
# print("total sum of first",n,"natural number is: ",sum)


"""Q12: WAP to find the factorial of first n numbers. (using for)"""
# n = int(input("enter number for its factorial: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print("factorial of",n,"is: ",fact)
