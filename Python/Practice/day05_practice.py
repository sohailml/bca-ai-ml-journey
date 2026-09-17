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

# Day 5 —  Practice Test (20 Questions)
"""Q1. Ek while loop likho jo 1 se 100 tak numbers print kare, 
lekin 5 se divisible numbers ko skip karna hai (bina continue ke, sirf condition change karke).
"""
# i = 1
# while i<=100:
#     if (i%5 != 0):
#         print(i)
#     i +=1


"""Q2. Predict output (bina run kiye):
i = 5
while i > 0:
    i -= 1
    if i == 2:
        break
    print(i, end=" ")"""
#iska output 4 3 hoga kyunki print function i -= 1 ke bad hai


"""Q3. for loop aur range() ka use karke ek aisa pattern print karo:
1
22
333
4444
55555"""
# for i in range(1,6):
#     print(str(i)*i)


"""Q4. Ek list hai: nums = [10, 20, 30, 40, 50]. Bina reverse() method aur bina [::-1] slicing ke,
ek while loop use karke list ko ulta karo (in-place reverse). Print karo final list."""
# nums = [10, 20, 30, 40, 50]
# i = 0
# j = len(nums) - 1
# while i < j:
#     nums[i], nums[j] = nums[j], nums[i]
#     i += 1
#     j -= 1
# print(nums)


"""Q5. For loop aur range() ka use karke ek list ke even indices (0, 2, 4...) par jo elements hain, 
unka sum calculate karo. Bina [::2] slicing ke."""
# lst = [1,12,3,14,25,46,7,38,19,10]
# sumeven = 0
# for i in range(0,len(lst),2):
#     sumeven = sumeven+lst[i]
# print(sumeven)


"""Q6. Ek dictionary hai: scores = {"A": 85, "B": 92, "C": 78, "D": 95}. 
Bina max() function ke, for loop use karke maximum value wali key aur value print karo."""
# scores = {"A": 85, "B": 92, "C": 78, "D": 95}

# max_value = 0
# max_key = ""

# for i in scores:
#     if scores[i] > max_value:
#         max_value = scores[i]
#         max_key = i

# print({max_key:max_value})


"""Q7. User se ek string input lo (e.g., "hello"). for loop use karke is string ka reverse nikal kar print karo.
Bina [::-1] slicing ke."""
# n = input("Enter your word: ")
# rev = ""
# for i in range(-1, -len(n)-1, -1):
#     rev += n[i]
# print(rev)


"""Q8. Predict output (bina run kiye):
x = 0
for i in range(10):
    if i % 2 == 0:
        continue
    x += i
else:
    x += 100
print(x)"""
#125 continue even valo ko skip kar dega odd valo ko jodega 


"""Q9. Ek list hai: data = [1, 2, 3, 4, 5]. For loop use karke list ke har element
ko uske square se replace karo (e.g., [1, 4, 9, 16, 25]). Print karo final list."""
# data = [1, 2, 3, 4, 5]
# for i in range(len(data)):
#     data[i] = data[i] ** 2
# print(data)


"""Q10. Ek tuple hai: tup = (2, 3, 5, 7, 11). for loop use karke check karo ki tuple mein 7 exist karta hai ya nahi. 
Agar milta hai toh "Found" print karo aur loop tod do (break). Agar nahi milta toh "Not Found" print karo."""
# tup = (2, 3, 5, 7, 11)
# for i in tup:
#     if i == 7:
#         print("Found")
#         break
# else:  # Yeh else loop ke BAHAR hai, tabhi chalega jab break nahi hua
#     print("Not Found")


"""Q11. while loop use karke, user se bar-bar numbers lo (input). Jab user 0 daale, 
toh loop stop ho jaye (break). Program print kare ki user ne kitne numbers daale (0 ko count mat karo)."""
# count = 0
# while True:
#     num =int(input("enter number: "))
#     if (num ==0):
#         break
#     count+=1
# print("you enter: ",count,"times")


"""Q12. Ek list hai: lst = [1, 2, 3, 4, 5]. For loop chalate waqt, agar current element 3 hai, 
toh usko list se remove karo (remove()). Phir list print karo. (Sochna: loop safe rahega ya index shift ka problem aayega?)"""
# lst = [1, 2, 3, 4, 5]
# for i in lst[:]:  # Copy par loop chal raha hai
#     if i == 3:
#         lst.remove(i)
# print(lst)  # Output: [1, 2, 4, 5]


"""Q13. Ek string hai: text = "aabbbcccaaa". 
For loop use karke har character ka count dictionary mein store karo (bina count() method ke). Print karo dictionary."""
# text = "aabbbcccaaa"
# count_dict = {}
# for char in text:
#     count_dict[char] = count_dict.get(char, 0) + 1
# print(count_dict)  # Output: {'a': 5, 'b': 3, 'c': 3}


"""Q14. Ek number lo (e.g., n = 1234). while loop use karke uska reverse nikaalo (e.g., 4321) aur print karo. 
(Digit extract karne ke liye % 10 aur // 10 use karo)"""
# n = 1234
# rev = 0
# while n > 0:
#     rev = (rev * 10) + (n % 10)  
#     n = n // 10                  
# print(rev)  # Output: 4321


"""Q15. Ek list hai: nums = [5, 12, 9, 33, 21, 8, 17]. Bina sort() method use kiye, 
for loop se dusra sabse bada number (second largest) find karo."""
# nums = [5, 12, 9, 33, 21, 8, 17]
# largest = float('-inf')
# second = float('-inf')

# for num in nums:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print(second)


"""Q16. Predict output (bina run kiye) —:
a = [1, 2, 3, 4]
for i in a:
    if i == 2:
        a.append(5)
    print(i, end=" ")"""
#iska output 1,2,3,4,5


"""Q17. Nested for loop use karke yeh pattern print karo:
*
* *
* * *
* * * *
* * * * *
(No string multiplication "* " * i allowed. Sirf print("*", end=" ") aur inner loop manual karo)"""
char = "*"
# for i in range(1, 6):          
#     for j in range(i):          
#         print("*", end=" ")
#     print()                     


"""Q18. Ek set hai: s = {10, 20, 30, 40, 50}. for loop use karke set ke har element ko 3 se multiply karo. 
Kya set ke elements change ho sakte hain? Agar nahi, toh naya set banao aur print karo. (Set mutable hai par elements immutable hote hain, soch)"""
# s = {10, 20, 30, 40, 50}
# new_set = set()
# for val in s:
#     new_set.add(val * 3)
# print(new_set) 


"""Q19. [The Ultimate Irodov] Ek list hai: nums = [1, 2, 3, 4, 5]. Ek for loop likho jo sirf original elements 
(1,2,3,4,5) par iterate kare, lekin loop ke andar un original elements ke squares ko list ke end mein append kare. 
Final list aisi dikhni chahiye: [1, 2, 3, 4, 5, 1, 4, 9, 16, 25].Condition: Tum nums.copy() ya nums[:] ka use kar sakte ho, 
par loop ko original list pe nahi chalana, ek copy pe chalana hai taaki infinite loop na ho. (Isme tujhe range aur length ka bhi use karna padega)"""
# nums = [1, 2, 3, 4, 5]
# for i in nums[:]:          
#     nums.append(i ** 2)    
# print(nums)  
