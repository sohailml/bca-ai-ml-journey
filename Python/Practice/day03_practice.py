"""Question 1: WAP to ask the user to enter names of their 3 favorite movies & store them in a list."""
# first=input("Enter your first favourite movie: ")
# second=input("Enter your second favourite movie: ")
# third=input("Enter your third favourite movie: ")

# list_of_your_favourite_movie =[first,second,third]
# print(list_of_your_favourite_movie)

# #second solution
# Movies=[]
# mov1=input("Enter your first favourite movie: ")
# mov2=input("Enter your first favourite movie: ")
# mov3=input("Enter your first favourite movie: ")
# Movies.insert(0,mov1)
# Movies.insert(1,mov2)
# Movies.insert(2,mov3)
# print(Movies)


"""Question 2: WAP to check if a list contains a palindrome(1,2,3,2,1) of elements. (Hint: use copy( ) method)"""
# list = [1,2,3,4,1]
# list2 =list.copy()
# list2.reverse()
# if (list==list2):
#     print("this list is palindrome")
# else:
#     print("this list is not palindrome")


"""Question 3: WAP to count the number of students with the “A” grade in the following tuple."""
# Grade = ("C", "D", "A","A", "B", "B", "A")
# print(Grade.count("A"))


"""Question 4: Store the above values in a list & sort them from “A” to “D”"""
# Grade1 = ["C", "D", "A","A", "B", "B", "A"]
# Grade1.sort()
# print(Grade1)

# Basic test - python


"""Q1: Q1. The Swap Master (Slicing Assignment) 🔄
Ek list hai: lst = [10, 20, 30, 40, 50, 60]
Kya karna hai: Bina koi naya list banaye, ek hi line (ya maximum 2 lines) mein pehla element (10) ko aakhri (60) se swap karo,
aur doosra (20) ko aakhri se doosra (50) se swap karo.(Hint: Slicing assignment use karo. lst[0:2] aur lst[-2:] ka combination)
Print: Final list kaisi dikhti hai?"""
# lst = [10, 20, 30, 40, 50, 60]
# lst[0],lst[-1] = lst[-1],lst[0]
# lst[1],lst[-2] = lst[-2],lst[1]
# print(lst)


"""Q2. The Copy Trap 🪤
Code likho: a = [1, 2, 3] \n b = a \n c = a.copy() # ya a[:] 
Ab tum karo:
b mein index 0 ki value 99 karo.
c mein index 1 ki value 88 karo.
Questions (Code likh kar demonstrate karo):
a ki value kya ho gayi?
b ki value kya hai?
c ki value kya hai?
Comments me likho ki aisa kyun hua (mutability aur copy ka concept)."""
# a = [1, 2, 3]
# b = a
# c = a.copy()
# b[0] = 99
# c[1] = 88
# print(b) # b ki value [99,2,3]
# print(c) # c ki value [1,88,3]
# print(a) # a ki value [99,2,3]
#explation: b = a tha yani ki dono ek hi hai so hamne b[0] ki value 99 rakhi so a[0] bhi 99 ho gya isiliye a list change hua [99,2,3] kyunki list muatable hai or jo c tha vo only copy tha yani ki e nayi list ban gayi us value se isiliye hamne c[1] cahnge karne pe bhi a list mai c vala value nahi aaya


"""Q3. Slicing Replacement 🧩
nums = [0, 1, 2, 3, 4, 5] di gayi hai.
Kya karna hai: Slicing assignment ka use karke, is list ke index 2, 3, 4 (i.e. [2,3,4]) ko hata kar unki jagah [99, 100] insert karo.
Print: Final list kya aayegi?
(Soch: Length increase hogi ya decrease?)"""
# nums = [0, 1, 2, 3, 4, 5]
# nums[2:5]=[99,100]
# print(nums)


"""Q4. Tuple Unpacking Trick 🎩
User se ek tuple input lo (maan lo tup = (15, 25)).
Kya karna hai: Bina kisi temporary variable (temp) ke, aur bina list mein convert kiye, in dono values ko swap karo. Phir naya tuple print karo.
(Hint: Python ki tuple unpacking a, b = b, a yaad hai?)"""
# tup = (15, 25)
# a = tup[0]
# b = tup[1]
# a,b=b,a
# new_tup = (a,b)
# print(new_tup)


"""Q5. Manual Calculator (No built-in max/min) 🧮
Ek list hai: numbers = [34, 12, 89, 5, 67]
Kya karna hai: Python ke built-in max() aur min() functions use kiye bina, sirf if conditions aur indexing ka use karke, is list ka sabse bada aur sabse chhota number find karo.
(Hint: Pehle maan lo 0th index sabse bada hai, fir baaki se compare karo if se).
Print: "Largest: 89, Smallest: 5" """
# numb = [34, 12, 89, 5, 67]

# largest = numb[0]
# smallest = numb[0]
# if (numb[1]>largest):
#     largest = numb[1]
# if (numb[2]>largest):
#     largest = numb[2]
# if (numb[3]>largest):
#     largest = numb[3]
# if (numb[4]>largest):
#     largest = numb[4]

# if (numb[1]<smallest):
#     smallest = numb[1]
# if (numb[2]<smallest):
#     smallest = numb[2]
# if (numb[3]<smallest):
#     smallest = numb[3]
# if (numb[4]<smallest):
#     smallest = numb[4]

# print("largest =",largest,"smallest =",smallest)


"""Q6. Pop & Remove Combo 🥊
data = ['apple', 'banana', 'cherry', 'banana', 'date'] di gayi hai.
Kya karna hai (step-by-step code likho):
remove() method use karke pehli 'banana' ko hatao. List print karo.
Fir pop() method use karke index 2 wala element hatao. List print karo.
Explain karo (comment me): remove() aur pop() mein kya basic difference hai?"""
# data = ['apple', 'banana', 'cherry', 'banana', 'date']
# data.remove("banana")
# print(data)
# data.pop(2)
# print(data)
# remove us value ko hata dega ha jo list mai pehli bar aayegi usko hatayega and pop us index ko


"""Q7. The Mutable Tuple (Brain Fryer) 🤯
Tuple diya hai: t = ([1, 2], 3, 4)
Hum jaante hain ki Tuple immutable hota hai (change nahi kar sakte).
Kya karna hai: Is tuple ke andar jo list hai ([1, 2]), usko change karke [100, 200] karo. Phir tuple print karo.
Sawaal (code ke saath comment mein likho):
Tuple change nahi ho sakta, phir yeh kaise possible hua? (Hint: Tuple ke andar ka object mutable hai, tuple sirf reference rakhta hai)."""
# t = ([1, 2], 3, 4)
# t[0][0] = 100
# t[0][1] = 200
# print(t)


"""Q8. Middle Element in Sorted List 📊
nums = [5, 12, 9, 33, 21, 8] di gayi hai.
Kya karna hai:
List ko descending order (ulta) mein sort karo (use sort(reverse=True)).
Is sorted list ka middle element (agar length odd hai) ya middle ke do elements (agar length even hai) print karo.
(Hint: Day 2 ka middle character wala logic yaad karo, bas ab list pe apply karna hai)."""
# nums = [5, 12, 9, 33, 21, 8]
# nums.sort(reverse=True)
# print(nums)
# if ((len(nums)%2) == 0):
#     print(nums[(len(nums)//2)-1:(len(nums)//2)+1])
# else:
#     print(nums[len(nums)//2])


"""🏆 Bonus Brain Teaser (No code, sirf output batao):
Agar tup = (1, 2, 3, 4, 5) hai, to print(tup[1::2]) kya output dega? Aur print(tup[-1:-4:-1]) kya dega?
(Bina code chalaye batao aur reason do)"""
# tup = (1, 2, 3, 4, 5)
# print(tup[1::2]) #iska output aayega (2,4)
# print(tup[-1:-4:-1]) # iska output aayega (5,4,3)
