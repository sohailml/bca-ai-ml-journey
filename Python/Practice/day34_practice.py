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
# answer:


# Q2. [Day 3] List ka bracket kya hai? Tuple ka bracket kya hai? Dono ka example likho.
# answer:


# Q3. [Day 3] List mutable hoti hai — iska kya matlab? Ek example se samjhao.
# answer:


# Q4. [Day 3] Tuple immutable hota hai — iska kya matlab? Agar tuple mein value change karne ki koshish karo toh kya hoga?
# answer:


# Q5. [Day 3] append() aur insert() mein kya farak hai?
# answer:


# Q6. [Day 3] pop() aur remove() mein kya farak hai?
# answer:



# ============================================================
#  CATEGORY 2: OUTPUT PREDICT (Q7-Q24)
# ============================================================

# Q7. [Day 3] Output kya aayega?
# my_list = [1, 3, "sohail", 5]
# print(len(my_list))
# answer:


# Q8. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# print(my_list[0])
# print(my_list[1:3])
# print(my_list[-1])
# answer:


# Q9. [Day 3] Output kya aayega?
# my_list = [1, 2, 3]
# my_list.append(100)
# print(my_list)
# answer:


# Q10. [Day 3] Output kya aayega?
# my_list = [5, 2, 8, 1]
# my_list.sort()
# print(my_list)
# answer:


# Q11. [Day 3] Output kya aayega?
# my_list = [5, 2, 8, 1]
# my_list.sort(reverse=True)
# print(my_list)
# answer:


# Q12. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# my_list.insert(1, 50)
# print(my_list)
# answer:


# Q13. [Day 3] Output kya aayega?
# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)
# answer:


# Q14. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# my_list.pop(2)
# print(my_list)
# answer:


# Q15. [Day 3] Output kya aayega?
# my_list = [10, 20, 30, 40]
# my_list.remove(30)
# print(my_list)
# answer:


# Q16. [Day 3] Output kya aayega?
# my_list = [1, 2, 3]
# new_list = my_list.copy()
# new_list.append(4)
# print(my_list)
# print(new_list)
# answer:


# Q17. [Day 3] Output kya aayega?
# tup = (10, 20, 30, 40)
# print(tup[1])
# print(tup[1:3])
# print(tup[-1])
# answer:


# Q18. [Day 3] Output kya aayega?
# tup = (1, 2, 3, 2)
# print(tup.index(2))
# print(tup.count(2))
# answer:


# Q19. [Day 2] Output kya aayega?
# s = "sohail"
# print(s[1:4])
# print(s[::-1])
# answer:


# Q20. [Day 2] Output kya aayega?
# age = 20
# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teen")
# else:
#     print("Child")
# answer:


# Q21. [Day 1] Output kya aayega?
# a = 10
# b = 3
# print(a / b)
# print(a // b)
# print(a % b)
# answer:


# Q22. [Day 1] Output kya aayega?
# print("5" + "5")
# print("5" * 2)
# print(5 + 5)
# answer:


# Q23. [Mix: Day 2 + Day 3] Output kya aayega?
# s = "hello"
# lst = [1, 2, 3]
# print(s[1])
# print(lst[1])
# print(s[-1])
# print(lst[-1])
# answer:


# Q24. [Mix: Day 1 + Day 2 + Day 3] Output kya aayega?
# x = "10"
# y = int(x)
# z = [y, y + 5]
# print(z)
# print(type(z[0]))
# answer:



# ============================================================
#  CATEGORY 3: LOGIC BUILDING (Q25-Q36)
# ============================================================

# Q25. [Day 3] my_list = [3, 1, 4, 1, 5, 9, 2, 6]. Length print karo, aur last element print karo.
# answer:


# Q26. [Day 3] my_list = [10, 20, 30, 40, 50]. Slicing se [20, 30, 40] print karo.
# answer:


# Q27. [Day 3] my_list = [1, 2, 3, 4, 5]. Isme 99 ko index 2 pe insert karo aur print karo.
# answer:


# Q28. [Day 3] my_list = [5, 3, 8, 1, 9]. Ascending aur descending order mein print karo.
# answer:


# Q29. [Day 3] my_list = [10, 20, 30, 40]. Index 1 wala element delete karo aur print karo.
# answer:


# Q30. [Day 3] my_list = [10, 20, 30, 20, 40]. Value 20 ko delete karo (pehli occurrence) aur print karo.
# answer:


# Q31. [Day 3] tup = (1, 2, 3, 2, 4, 2). 2 kitni baar aaya? Aur 2 ka first index?
# answer:


# Q32. [Day 3 + Day 2] my_list = ["sohail", "ansari", "python"]. Har element ki length print karo.
# answer:


# Q33. [Day 3 + Day 2] s = "hello world". split() use karke list banao.
# answer:


# Q34. [Day 3 + Day 1] my_list = [10, 20, 30]. Saare elements ka sum manually nikalo.
# answer:


# Q35. [Day 3 + Day 2] User se naam input lo. First aur last character print karo. Phir usko list mein daalo.
# answer:


# Q36. [Mix: Day 1 + Day 2 + Day 3] User se 3 numbers input lo, list mein daalo, sort karo, print karo.
# answer:



# ============================================================
#  CATEGORY 4: TRICKY / EDGE CASE (Q37-Q48)
# ============================================================

# Q37. [Day 3] Kya hoga aur kyun?
# tup = (1, 2, 3)
# tup[0] = 100
# print(tup)
# answer:


# Q38. [Day 3] Kya hoga aur kyun?
# my_list = [1, 2, 3]
# my_list[0] = 100
# print(my_list)
# answer:


# Q39. [Day 3] Output kya aayega? [1,2,3] ya [1,2,3,4]? Kyun?
# my_list = [1, 2, 3]
# new_list = my_list
# new_list.append(4)
# print(my_list)
# answer:


# Q40. [Day 3] Q39 ko copy() use karke fix karo.
# answer:


# Q41. [Day 3] Kya error aayega?
# my_list = [1, 2, 3]
# print(my_list[5])
# answer:


# Q42. [Day 3] Error ya output? Kya aayega?
# my_list = [1, 2, 3]
# print(my_list[1:10])
# answer:


# Q43. [Day 3] pop() mein argument nahi diya — kya hoga?
# my_list = [10, 20, 30]
# my_list.pop()
# print(my_list)
# answer:


# Q44. [Day 3] Kya error aayega?
# my_list = [1, 2, 3]
# my_list.remove(5)
# print(my_list)
# answer:


# Q45. [Day 3] Pehla print kya dega — None ya list? Kyun?
# my_list = [1, 2, 3]
# print(my_list.reverse())
# print(my_list)
# answer:


# Q46. [Day 3] Output kya aayega?
# my_list = [3, 1, 2]
# print(my_list.sort())
# answer:


# Q47. [Day 2 + Day 3] Char lines ka output batao. String slicing vs list slicing farak batao.
# s = "sohail"
# lst = ["sohail"]
# print(s[0])
# print(lst[0])
# print(s[0:3])
# print(lst[0:3])
# answer:


# Q48. [Mix: Day 1 + Day 3] Kya error aayega? Kyun?
# lst = [1, "2", 3.0, True]
# print(len(lst))
# print(lst[1] + lst[0])
# answer:



# ============================================================
#  CATEGORY 5: DEBUGGING (Q49-Q58)
# ============================================================

# Q49. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# my_list.append[100]
# print(my_list)
# answer:


# Q50. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# my_list.push(100)
# print(my_list)
# answer:


# Q51. Bug kya hai? Do reason batao.
# tup = (1, 2, 3)
# tup.append(4)
# print(tup)
# answer:


# Q52. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# print(my_list.length())
# answer:


# Q53. Bug kya hai? Fix karo.
# my_list = [1, 2, 3]
# print(len[my_list])
# answer:


# Q54. Ye chalega ya nahi? Output kya?
# my_list = [1, 2, 3]
# my_list.remove(2)
# print(my_list)
# answer:


# Q55. [Day 2] Bug kya hai? Fix karo.
# s = "sohail"
# if s = "sohail":
#     print("match")
# answer:


# Q56. [Day 2] Bug kya hai? Fix karo.
# age = 20
# if age >= 18:
# print("Adult")
# answer:


# Q57. [Mix: Day 1 + Day 3] Bug kya hai? Do fix batao.
# lst = [1, 2, 3]
# result = lst + 5
# print(result)
# answer:


# Q58. [Mix: Day 2 + Day 3] Bug kya hai? Kyun capitalize() list pe kaam nahi karta?
# my_list = ["sohail", "ansari"]
# print(my_list.capitalize())
# answer:



# ============================================================
#  CATEGORY 6: CHALLENGE (Q59-Q68)
# ============================================================

# Q59. [Day 3] my_list = [1, 2, 3, 4, 5]. Reverse karo do tarike se (reverse() aur slicing).
# answer:


# Q60. [Day 3] my_list = [10, 20, 30, 40, 50]. Middle element nikalo bina index hardcode kiye.
# answer:


# Q61. [Day 3] my_list = [1, 2, 3, 4, 5]. First half aur second half alag print karo.
# answer:


# Q62. [Day 3] tup = (1, 2, 3, 4, 5). Reverse karo (tuple mein reverse() nahi hota).
# answer:


# Q63. [Day 3 + Day 2] my_list = ["apple", "banana", "cherry"]. Har word ka first character print karo.
# answer:


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

# Mistake 1:
# Mistake 2:
# Mistake 3:
# Mistake 4:
# Mistake 5: