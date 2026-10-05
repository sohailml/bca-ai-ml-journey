"""
============================================================
  PYTHON BASICS - DAY 3 PRACTICE SET (85 Questions)
  Topics: Lists & Tuples (+ Day 1 & Day 2 mix)
============================================================
  Har question ke neeche # answer: likha hai
  Wahan apna answer likho (code ya explanation)
  Loop use NAHI karna
============================================================
"""

# ============================================================
#  CATEGORY 1: WARM-UP (Q1-Q6)
# ============================================================

# Q1. [Day 3] List aur Tuple mein main difference kya hai? Ek line mein likho.
# answer: list ko square bracket mai likhte hai and tuple ko parenthesis mai and list mutable hoti hai change kar sakte hia but tuple change nai kar sakte immuatable hai


# Q2. [Day 3] List ka bracket kya hai? Tuple ka bracket kya hai? Dono ka example likho.
# answer: list ko square bracket mai likhte hai [] and tuple ko parenthesis ()


# Q3. [Day 3] List mutable hoti hai — iska kya matlab? Ek example se samjhao.
# answer:list mutable hoti hai iska mtlb hai ki ham list ko change kar sakte hai originl list
# list = [2,3,"sohail"]
# list[1] = "ansari"
# print(list)


# Q4. [Day 3] Tuple immutable hota hai — iska kya matlab? Agar tuple mein value change karne ki koshish karo toh kya hoga?
# answer:tuple ko change nahi kar sakte hai value change karne ki kosis karen to erroe aayega example:
# list = (2,3,"sohail")
# list[1] = "ansari"
# print(list)


# Q5. [Day 3] append() aur insert() mein kya farak hai?
# answer:appen() list ke last mai vo value add karta hai and insert() list ke kisi specific index mai vo value add karta


# Q6. [Day 3] pop() aur remove() mein kya farak hai?
# answer:pop() us index ki value ko hata deta hai and remove() us value ko hata deta hai jaha vo first occur hota hai



# ============================================================
#  CATEGORY 2: OUTPUT PREDICT (Q7-Q24)
# ============================================================

# Q7. [Day 3] Output kya aayega?
# my_list = [1, 3, "sohail", 5]
# print(len(my_list))
# answer: iski length 4 hai


# Q8. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# print(my_list[0])
# print(my_list[1:3])
# print(my_list[-1])
# answer: iska output pehle 10 fir [20,30] third 40


# Q9. [Day 3] Output kya aayega?
# my_list = [1, 2, 3]
# my_list.append(100)
# print(my_list)
# answer:[1,2,3,100]


# Q10. [Day 3] Output kya aayega?
# my_list = [5, 2, 8, 1]
# my_list.sort()
# print(my_list)
# answer:[1,2.5.8]


# Q11. [Day 3] Output kya aayega?
# my_list = [5, 2, 8, 1]
# my_list.sort(reverse=True)
# print(my_list)
# answer:[8,5,2,1]


# Q12. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# my_list.insert(1, 50)
# print(my_list)
# answer:[10,50,20,30,40]


# Q13. [Day 3] Output kya aayega?
# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)
# answer:[4,3,2,1]


# Q14. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# my_list.pop(2)
# print(my_list)
# answer:[10,20,40]


# Q15. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# my_list.remove(30)
# print(my_list)
# answer:[10,20,40]


# Q16. [Day 3] Output kya aayega?
# my_list = [1, 2, 3]
# new_list = my_list.copy()
# new_list.append(4)
# print(my_list)
# print(new_list)
# answer:1st [1,2,3] 2nd output [1,2,3,4]


# Q17. [Day 3] Output kya aayega?
# tup = (10, 20, 30, 40)
# print(tup[1])
# print(tup[1:3])
# print(tup[-1])
# answer:1st 20 2nd (20,30) 3rd 40


# Q18. [Day 3] Output kya aayega?
# tup = (1, 2, 3, 2)
# print(tup.index(2))
# print(tup.count(2))
# answer:1st 1 second 2


# Q19. [Day 2] Output kya aayega?
# s = "sohail"
# print(s[1:4])
# print(s[::-1])
# answer:1st oha 2nd liahos


# Q20. [Day 2] Output kya aayega?
# age = 20
# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teen")
# else:
#     print("Child")
# answer:Adult


# Q21. [Day 1] Output kya aayega?
# a = 10
# b = 3
# print(a / b)
# print(a // b)
# print(a % b)
# answer: 1st 3.33333 2nd 3 3rd 1


# Q22. [Day 1] Output kya aayega?
# print("5" + "5")
# print("5" * 2)
# print(5 + 5)
# answer:1st 55 2nd mai 55 3rd mai 10


# Q23. [Mix: Day 2 + Day 3] Output kya aayega?
# s = "hello"
# lst = [1, 2, 3]
# print(s[1])
# print(lst[1])
# print(s[-1])
# print(lst[-1])
# answer:1st e 2nd 2 3rd o 4th 3


# Q24. [Mix: Day 1 + Day 2 + Day 3] Output kya aayega?
# x = "10"
# y = int(x)
# z = [y, y + 5]
# print(z)
# print(type(z[0]))
# answer:1st [10,15] 2nd int



# ============================================================
#  CATEGORY 3: LOGIC BUILDING (Q25-Q36)
# ============================================================

# Q25. [Day 3] my_list = [3, 1, 4, 1, 5, 9, 2, 6]. Length print karo, aur last element print karo.
# answer:
# my_list = [3, 1, 4, 1, 5, 9, 2, 6]
# print(len(my_list))
# print(my_list[-1])


# Q26. [Day 3] my_list = [10, 20, 30, 40, 50]. Slicing se [20, 30, 40] print karo.
# answer:
# my_list = [10, 20, 30, 40, 50]
# print(my_list[1:4])


# Q27. [Day 3] my_list = [1, 2, 3, 4, 5]. Isme 99 ko index 2 pe insert karo aur print karo.
# answer:
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2,99)
# print(my_list)


# Q28. [Day 3] my_list = [5, 3, 8, 1, 9]. Ascending aur descending order mein print karo.
# answer:
# my_list = [5, 3, 8, 1, 9]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)


# Q29. [Day 3] my_list = [10, 20, 30, 40]. Index 1 wala element delete karo aur print karo.
# answer:
# my_list = [10, 20, 30, 40]
# my_list.pop(1)
# print(my_list)


# Q30. [Day 3] my_list = [10, 20, 30, 20, 40]. Value 20 ko delete karo (pehli occurrence) aur print karo.
# answer:
# my_list = [10, 20, 30, 20, 40]
# my_list.remove(20)
# print(my_list)


# Q31. [Day 3] tup = (1, 2, 3, 2, 4, 2). 2 kitni baar aaya? Aur 2 ka first index?
# answer:
# tup = (1, 2, 3, 2, 4, 2)
# print(tup.count(2))
# print(tup.index(2))


# Q32. [Day 3 + Day 2] my_list = ["sohail", "ansari", "python"]. Har element ki length print karo.
# answer:
# my_list = ["sohail", "ansari", "python"]
# print(len(my_list[0]))
# print(len(my_list[1]))
# print(len(my_list[2]))


# Q33. [Day 3 + Day 2] s = "hello world". split() use karke list banao.
# answer:
# s = "hello world"
# list = s.split()
# print(list)


# Q34. [Day 3 + Day 1] my_list = [10, 20, 30]. Saare elements ka sum manually nikalo.
# answer:
# my_list = [10, 20, 30]
# sum = my_list[0]+my_list[2]+my_list[1]
# print(sum)


# Q35. [Day 3 + Day 2] User se naam input lo. First aur last character print karo. Phir usko list mein daalo.
# answer:
# name = input("Enter name: ")
# start = name[0]
# end = name[-1]
# lst = []
# print(start)
# print(end)
# lst.append(start)
# lst.append(end)
# print(lst)


# Q36. [Mix: Day 1 + Day 2 + Day 3] User se 3 numbers input lo, list mein daalo, sort karo, print karo.
# answer:
# first = int(input("enter no: "))
# second = int(input("enter no: "))
# third = int(input("enter no: "))
# lst =[]
# lst.append(first)
# lst.append(second)
# lst.append(third)
# lst.sort()
# print(lst)


# ============================================================
#  CATEGORY 4: TRICKY / EDGE CASE (Q37-Q48)
# ============================================================

# Q37. [Day 3] Kya hoga aur kyun?
# tup = (1, 2, 3)
# tup[0] = 100
# print(tup)
# answer:error aayega tup immuatable hota hai 


# Q38. [Day 3] Kya hoga aur kyun?
# my_list = [1, 2, 3]
# my_list[0] = 100
# print(my_list)
# answer: change ho jayega [100,2,3] output 1 ki jagah 100


# Q39. [Day 3] Output kya aayega? [1,2,3] ya [1,2,3,4]? Kyun?
# my_list = [1, 2, 3]
# new_list = my_list
# new_list.append(4)
# print(my_list)
# answer:[1,2,3,4] hi aayega


# Q40. [Day 3] Q39 ko copy() use karke fix karo.
# answer:
# my_list = [1, 2, 3]
# new_list =my_list.copy()
# new_list.append(4)
# print(my_list)


# Q41. [Day 3] Kya error aayega?
# my_list = [1, 2, 3]
# print(my_list[5])
# answer:index out of range 5th index hai hi nahi koi


# Q42. [Day 3] Error ya output? Kya aayega?
# my_list = [1, 2, 3]
# print(my_list[1:10])
# answer: error nahi aayega output [2,3] hoga


# Q43. [Day 3] pop() mein argument nahi diya — kya hoga?
# my_list = [10, 20, 30]
# my_list.pop()
# print(my_list)
# answer: pop mai argument nahi diya so by defaul last ka index remove kar dega output [10,20]


# Q44. [Day 3] Kya error aayega?
# my_list = [1, 2, 3]
# my_list.remove(5)
# print(my_list)
# answer:error aayega kyunki 5 present hi nai hai


# Q45. [Day 3] Pehla print kya dega — None ya list? Kyun?
# my_list = [1, 2, 3]
# print(my_list.reverse())
# print(my_list)
# answer:pehel none prin hoga fir list kyunki my_list.reverse() ko direct print function mai isilye


# Q46. [Day 3] Output kya aayega?
# my_list = [3, 1, 2]
# print(my_list.sort())
# answer:none


# Q47. [Day 2 + Day 3] Char lines ka output batao. String slicing vs list slicing farak batao.
# s = "sohail"
# lst = ["sohail"]
# print(s[0])
# print(lst[0])
# print(s[0:3])
# print(lst[0:3])
# answer: list  slicing string slicing same hi kuchh jyada diffrence nahi hai list slicing new list bana ke deta hai and first output s sencond output sohail third soh fourth ["sohail"]


# Q48. [Mix: Day 1 + Day 3] Kya error aayega? Kyun?
# lst = [1, "2", 3.0, True]
# print(len(lst))
# print(lst[1] + lst[0])
# answer: pehle output aayega 4 kyunki list ki lenght 4 hai and second error kyunki diffrent data type hai isiliye add nahi ho sakta



# ============================================================
#  CATEGORY 5: DEBUGGING (Q49-Q58)
# ============================================================

# Q49. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# my_list.append[100]
# print(my_list)
# answer: isme .append ke sath [] ye use kar liya isiliye bug hai sahi syntax append() hai
# my_list = [1, 2, 3]
# my_list.append(100)
# print(my_list)


# Q50. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# my_list.push(100)
# print(my_list)
# answer:.push ki jagah .appen ayega ya
# my_list = [1, 2, 3]
# my_list.append(100)
# print(my_list)


# Q51. Bug kya hai? Do reason batao.
# tup = (1, 2, 3)
# tup.append(4)
# print(tup)
# answer:tup immutable hai .append nai kar sakte 


# Q52. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# print(my_list.length())
# answer:isme bug ye hai ki len ki jagah length use hai and proper syntax nahi hai aise hoga:
# my_list = [1, 2, 3]
# print(len(my_list))


# Q53. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# print(len[my_list])
# answer:isme bug ye hai ki len function parenthesis use hota hai isme bracket use hua hai
# my_list = [1, 2, 3]
# print(len(my_list))


# Q54. Ye chalega ya nahi? Output kya?
# my_list = [1, 2, 3]
# my_list.remove(2)
# print(my_list)
# answer:output aayeaga [1,3]


# Q55. [Day 2] Bug kya hai? Fix karo.
# s = "sohail"
# if s = "sohail":
#     print("match")
# answer:isme s = use hua ha python mai equal to ke liye == use hota hai
# s = "sohail"
# if s =="sohail":
#     print("match")


# Q56. [Day 2] Bug kya hai? Fix karo.
# age = 20
# if age >= 18:
# print("Adult")
# answer:indentation error
# age = 20
# if age >= 18:
#   print("Adult")


# Q57. [Mix: Day 1 + Day 3] Bug kya hai? Do fix batao.
# lst = [1, 2, 3]
# result = lst + 5
# print(result)
# answer:bug ye hai ki ham list ko int se add kar rahe to fix ya to append use kare and last mai 5 concatinate kar de ya 5 ko list bana de
# lst = [1, 2, 3]
# result = lst + [5]
# print(result)


# Q58. [Mix: Day 2 + Day 3] Bug kya hai? Kyun capitalize() list pe kaam nahi karta?
# my_list = ["sohail", "ansari"]
# print(my_list.capitalize())
# answer:.capitalize list mai nahi use kar sakte list mai diffrent type ke data hoten hai .capitalize string ka first letter capital karta hai



# ============================================================
#  CATEGORY 6: CHALLENGE (Q59-Q68)
# ============================================================

# Q59. [Day 3] my_list = [1, 2, 3, 4, 5]. Reverse karo do tarike se (reverse() aur slicing).
# answer:
# my_list = [1, 2, 3, 4, 5]
# print(my_list[::-1])
# my_list.reverse()
# print(my_list)


# Q60. [Day 3] my_list = [10, 20, 30, 40, 50]. Middle element nikalo bina index hardcode kiye.
# answer:
# my_list = [10, 20, 30, 40, 50]
# print(my_list[len(my_list)//2])


# Q61. [Day 3] my_list = [1, 2, 3, 4, 5]. First half aur second half alag print karo.
# answer:
# my_list = [1, 2, 3, 4, 5]
# print(my_list[0:2])
# print(my_list[3:])


# Q62. [Day 3] tup = (1, 2, 3, 4, 5). Reverse karo (tuple mein reverse() nahi hota).
# answer:
# tup = (1, 2, 3, 4, 5)
# print(tup[::-1])


# Q63. [Day 3 + Day 2] my_list = ["apple", "banana", "cherry"]. Har word ka first character print karo.
# answer:
# my_list = ["apple", "banana", "cherry"]
# first = my_list[0]
# second = my_list[1]
# third = my_list[2]
# print(first[0])
# print(second[0])
# print(third[0])


# Q64. [Day 3 + Day 1] my_list = [2, 4, 6, 8]. Har element ka square karke nayi list banao.
# answer:


# Q65. [Day 3] t1 = (1, 2, 3), t2 = (4, 5). Concatenate karke naya tuple banao.
# answer:


# Q66. [Day 3 + Day 2] s = "i love python". Split karo, reverse karo, join karke string banao.
# answer:


# Q67. [Mix: Day 1 + Day 3] my_list = [10, 20, 30]. 40 add karo do tarike se (append aur +).
# answer:


# Q68. [Mix: Day 2 + Day 3] User se word lo. Characters ki list banao. Reverse karo. Palindrome check karo.
# answer:



# ============================================================
#  CATEGORY 7: WRITE A PROGRAM (Q69-Q80)
# ============================================================

# Q69. [Day 3] List [10, 20, 30, 40, 50] banao, length + first + last print karo.
# answer:


# Q70. [Day 3] Empty list banao, 10, 20, 30 append karo, print karo.
# answer:


# Q71. [Day 3] List [5, 2, 9, 1, 7] ko sort karo, phir reverse sort karke print karo.
# answer:


# Q72. [Day 3] List [1, 2, 3, 4, 5] mein index 2 pe 99 insert karo.
# answer:


# Q73. [Day 3] List [10, 20, 30, 40, 50] se index 1 wala pop karo.
# answer:


# Q74. [Day 3] List [10, 20, 30, 20, 40] se value 20 remove karo.
# answer:


# Q75. [Day 3] Tuple (1, 2, 3, 2, 4, 2) ka 2 ka count aur first index print karo.
# answer:


# Q76. [Day 3 + Day 2] User se 3 words lo, list mein daalo, sort karke print karo.
# answer:


# Q77. [Day 3 + Day 2] User se sentence lo, split karke list banao, length print karo.
# answer:


# Q78. [Day 3 + Day 1] User se 5 numbers lo, list mein daalo, sum aur average print karo (bina sum()).
# answer:


# Q79. [Day 3 + Day 2] User se word lo. Characters ki list banao. Reverse karo. Palindrome check karo.
# answer:


# Q80. [Day 3 + Day 2 + Day 1] Student naam + 3 marks lo. Marks list mein. Sort karo. Highest + lowest print karo. Agar highest >= 90 toh "Topper" warna "Average".
# answer:



# ============================================================
#  CATEGORY 8: REVISION MIX (Q81-Q85)
# ============================================================

# Q81. [Mix: Day 1 + Day 3] Output batao aur copy() ka role samjhao.
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b)
# answer:


# Q82. [Mix: Day 2 + Day 3] Output kya aayega?
# s = "sohail"
# lst = [s, s.capitalize(), s[::-1]]
# print(lst)
# answer:


# Q83. [Mix: Day 1 + Day 2 + Day 3] Output kya aayega?
# x = "10"
# y = int(x)
# lst = [y, y * 2, y + 5]
# print(lst)
# print(lst[1] > lst[0])
# answer:


# Q84. [Mix: Day 2 + Day 3] Output kya aayega?
# tup = ("a", "b", "c", "b")
# print(tup.count("b"))
# print(tup.index("b"))
# print(tup[-1])
# answer:


# Q85. [Mix: Day 1 + Day 2 + Day 3] my_list = [10, "20", 30.0, True]. Har element ka type print karo. Kaunsa string hai?
# answer:



# ============================================================
#  MISTAKE NOTEBOOK
# ============================================================

# Mistake 1:Q12 mai maine socha ki .insert(1,50) karne se 1st index pe jo hai vo delete hoke insert hoga but isne 1 index pe 50 add kiya or 20 ko remove nahi kiya 2nd index pe shift kar idya
# Mistake 2:Q17 mai tup[1] maine socha tha ki output (20) aise aayega parenthesis ke andar ye mistake thi 
# Mistake 3:Q28 mai ascending and descending mai karna tha to maine direct print(my_list.sort()) and print(my_lsit.sort(reverse=True)) kar diya tha isiliye none output aa gya tha
# Mistake 4:Q39 mai new list mai append hua and print mai tha my_list so maine socha ki new list mai appned hua hai to my list same rahegi and output[1,2,3] original list aayegi but new list = my list tha isiliye my list bhi append hua
# Mistake 5:Q43 mai pop() tha koi argument nai diya tha mai socha ki kuch remove nahi hoga but last vala index delte ho gya