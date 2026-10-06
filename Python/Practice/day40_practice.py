"""
============================================================
  PYTHON BASICS - DAY 3 | HARD MODE (50 Questions)
  Topics: Lists & Tuples + Day 1 & Day 2 Mix
============================================================
"""

# ============================================================
#  SECTION 1: DEEP CONCEPT TRAPS (Q1-Q10)
# ============================================================

# Q1. [Day 3] Ye code kya print karega? Line-by-line reason batao.
# a = [1, 2, 3]
# b = a
# c = a.copy()
# a.append(4)
# b.append(5)
# c.append(6)
# print(a)
# print(b)
# print(c)
# answer:


# Q2. [Day 3] Nested list ka case. copy() ne kya kiya? Kya a bhi change hua? Shallow copy concept samjhao.
# a = [1, [2, 3]]
# b = a.copy()
# b[1].append(4)
# b.append(5)
# print(a)
# print(b)
# answer:


# Q3. [Day 2] String immutable hai, list mutable. Ye code kya karega? Kyun ek error deta hai aur dusra nahi?
# s = "hello"
# s[0] = "H"
# print(s)
#
# lst = ["hello"]
# lst[0] = "H"
# print(lst)
# answer:


# Q4. [Day 3] + vs append() vs extend(). Teeno output batao. append([3,4]) aur + [3,4] mein fundamental farak kya hai?
# a = [1, 2]
# b = [3, 4]
# print(a + b)
# print(a)
# a.append(b)
# print(a)
# answer:


# Q5. [Day 3] Tuple ke andar list. Tuple immutable hai — phir bhi change ho gaya? Reason batao.
# t = (1, 2, [3, 4])
# t[2].append(5)
# print(t)
# answer:


# Q6. [Day 3] sort() vs sorted(). x, y, lst — teeno ka output? Farak batao.
# lst = [3, 1, 2]
# x = lst.sort()
# y = sorted(lst)
# print(x)
# print(y)
# print(lst)
# answer:


# Q7. [Day 2 + Day 3] Slicing trap. 6 lines ka output batao. s[:] aur lst[:] ka type same hai ya different?
# s = "sohail"
# lst = list(s)
# print(s[:])
# print(lst[:])
# print(s[::-1])
# print(lst[::-1])
# print(type(s[:]))
# print(type(lst[:]))
# answer:


# Q8. [Day 3] pop() ka trap. x aur y ki value kya? Aur lst mein kya bacha?
# lst = [1, 2, 3, 4, 5]
# x = lst.pop(2)
# y = lst.pop()
# print(x, y)
# print(lst)
# answer:


# Q9. [Day 1 + Day 3] Identity vs Equality. Char lines ka output aur reason batao.
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
# print(a == b)
# print(a is b)
# print(a is c)
# print(a == c)
# answer:


# Q10. [Day 3] Empty containers. Last line kya karegi? Error ya output? Kyun?
# a = []
# b = ()
# c = ""
# d = None
# print(bool(a), bool(b), bool(c), bool(d))
# print(len(a), len(b), len(c))
# print(len(d))
# answer:



# ============================================================
#  SECTION 2: OUTPUT PREDICTION — ADVANCED CHAINS (Q11-Q22)
# ============================================================

# Q11. Output kya aayega?
# lst = [1, 2, 3, 4, 5]
# lst[1:4] = [10, 20]
# print(lst)
# print(len(lst))
# answer:


# Q12. Output kya aayega?
# lst = [1, 2, 3]
# lst[1:1] = [99, 100]
# print(lst)
# answer:


# Q13. Output kya aayega?
# lst = [1, 2, 3, 4, 5]
# del lst[1:3]
# print(lst)
# answer:


# Q14. Output kya aayega?
# lst = [1, 2, 3]
# print(lst * 2)
# print(lst + [4])
# answer:


# Q15. Output kya aayega?
# tup = (1, 2, 3)
# print(tup * 2)
# print(tup + (4, 5))
# print(len(tup * 2))
# answer:


# Q16. Output kya aayega?
# s = "abc"
# lst = ["a", "b", "c"]
# print(s * 2)
# print(lst * 2)
# print(s + "d")
# print(lst + ["d"])
# answer:


# Q17. Output kya aayega?
# lst = [3, 1, 4, 1, 5, 9, 2, 6]
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)
# print(lst[2:5])
# answer:


# Q18. Output kya aayega?
# tup = (5, 3, 1, 4, 2)
# print(tup[1:4])
# print(tup[::-1])
# print(tup[-2:])
# answer:


# Q19. Output kya aayega? += ne kya kiya? lst bhi change hua?
# lst = [1, 2, 3]
# lst2 = lst
# lst2 += [4]
# print(lst)
# print(lst2)
# answer:


# Q20. Teeno alag? Same? Reason batao.
# a = [1, 2, 3]
# b = a + [4]
# c = a
# c += [4]
# print(a)
# print(b)
# print(c)
# answer:


# Q21. [Mix: Day 1+2+3] Output kya aayega?
# x = "5"
# y = int(x)
# z = [x, y, str(y), bool(y)]
# print(z)
# print(type(z[0]), type(z[1]), type(z[2]), type(z[3]))
# answer:


# Q22. [Mix: Day 1+2+3] Output kya aayega?
# name = "sohail"
# marks = [85, 92, 78]
# avg = (marks[0] + marks[1] + marks[2]) / 3
# result = [name, avg, avg >= 80]
# print(result)
# print(name.capitalize(), result[2])
# answer:



# ============================================================
#  SECTION 3: HARD LOGIC BUILDING (Q23-Q34)
# ============================================================

# Q23. [Day 3] lst = [1, 2, 3, 4, 5, 6]. First half aur second half alag list banao slicing se. Dono ka sum compare karo (bina sum()).
# answer:


# Q24. [Day 3] lst = [10, 25, 30, 45, 50, 65]. Sirf woh elements ki nayi list banao jo 5 se divisible hain. (Bina loop)
# answer:


# Q25. [Day 3] lst = [1, 2, 3, 2, 4, 2, 5]. Value 2 ki saari occurrences hatao sirf remove() se. Kitni baar call karoge?
# answer:


# Q26. [Day 3] a = [1, 2, 3], b = [4, 5, 6]. Bina extend() ya + use kiye dono ko merge karke [1,2,3,4,5,6] banao.
# answer:


# Q27. [Day 3] t = (10, 20, 30, 40, 50). Middle element nikalo bina index hardcode kiye.
# answer:


# Q28. [Day 3 + Day 2] s = "i love python programming". Split karke list banao. Length print karo. Last word uppercase karo.
# answer:


# Q29. [Day 3 + Day 2] lst = ["apple", "banana", "cherry", "date"]. Har word ka first aur last letter nayi list mein daalo. Output: ['ae', 'ba', 'cy', 'de']
# answer:


# Q30. [Day 3 + Day 1] lst = [5, 10, 15, 20, 25]. Second largest element nikalo bina sort() use kiye.
# answer:


# Q31. [Day 3 + Day 2] lst = [1, 2, 3, 4, 5]. Reverse karo 3 tarike se: reverse(), slicing, manually.
# answer:


# Q32. [Day 3 + Day 2] User se word lo. Agar palindrome → "Palindrome". Agar length 3 se kam → "Too short". Warna → "Not palindrome". Order of checks socho.
# answer:


# Q33. [Day 3 + Day 2] lst = [1..10]. Even aur odd numbers ki alag lists banao. Dono ki length compare karo.
# answer:


# Q34. [Day 3 + Day 1] prices = [99.5, 45.25, 200.0, 15.75]. Har price ko int mein convert karke nayi list banao. Sum manually nikalo.
# answer:



# ============================================================
#  SECTION 4: HARD DEBUGGING (Q35-Q42)
# ============================================================

# Q35. Ye code kya karega? Bug kya hai?
# lst = [1, 2, 3]
# lst = lst.append(4)
# print(lst)
# answer:


# Q36. Kya tup change hua? Kyun?
# tup = (1, 2, 3)
# tup2 = tup
# tup2 += (4,)
# print(tup)
# print(tup2)
# answer:


# Q37. Ye infinite loop hai — kyun? Reason batao.
# lst = [1, 2, 3]
# for x in lst:
#     lst.append(x)
# print(lst)
# answer:


# Q38. b ki value kya? a[:] ne kya kiya?
# a = [1, 2, 3]
# b = a[:]
# a.append(4)
# print(b)
# answer:


# Q39. Teeno lines — kaunsi error degi?
# lst = [1, 2, 3]
# print(lst[1:2])
# print(lst[1:2][0])
# print(lst[1:2][1])
# answer:


# Q40. Output kya hoga? (join na aaye toh skip)
# name = "sohail"
# lst = list(name)
# lst.sort()
# print(lst)
# print("".join(lst))
# answer:


# Q41. Output kya aayega?
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x
# x.append(4)
# print(x == y)
# print(x == z)
# print(y == z)
# print(x is z)
# answer:


# Q42. Second line kya karegi?
# t = (1, 2, 3)
# print(t.index(2))
# print(t.index(5))
# answer:



# ============================================================
#  SECTION 5: WRITE A PROGRAM — HARD (Q43-Q50)
# ============================================================

# Q43. User se 5 numbers lo, list mein daalo, sort karo, aur: highest, lowest, second highest (sorted list se index se), average (bina sum()) print karo.
# answer:


# Q44. User se sentence lo: total words, total characters (with spaces), total characters (without spaces), longest word print karo.
# answer:


# Q45. lst = [10, 20, 30, 20, 40, 20, 50]. Value 20 ki saari occurrences hatao. Naya list print karo. Original aur nayi length compare karo.
# answer:


# Q46. a = [1, 2, 3, 4, 5], b = [3, 4, 5, 6, 7]. Common elements ki nayi list banao (bina loop, bina set). Output: [3, 4, 5]
# answer:


# Q47. User se student naam + 5 subject marks lo (list). Sort karo. Top 3 marks print karo (slicing). Lowest 2 marks print karo (slicing). Average nikaalo. Grade: >=90 Topper, >=75 Distinction, >=60 First Class, warna Needs improvement.
# answer:


# Q48. s = "programming". Sabhi vowels ki list banao (manually, loop nahi). Sabhi consonants ki list banao. Dono print karo. Length compare karo.
# answer:


# Q49. User se 10 numbers lo (list). Ascending sort karo. Descending sort karo. Dono lists compare karo — kya exact reverse hain? Output True/False.
# answer:


# Q50. Inventory system simulate karo:
# items = ["pen", "book", "pencil"]
# prices = [10, 50, 5]
# quantity = [100, 20, 200]
# User se item naam lo. Agar item list mein hai → index dhundho, price aur quantity print karo, total value (price × quantity) print karo. Warna → "Item not found". (index() use karo, loop nahi)
# answer:



# ============================================================
#  SECTION 6: IQ BOOSTER — REASONING TRAPS (B1-B5)
# ============================================================

# B1. a = [1, 2, 3]. b = a kiya, phir b.append(4). Ab a mein bhi 4 hai. Kyun? Python ka design decision kyun hai? Real world example do.
# answer:


# B2. == aur is — Google interview classic. Ek scenario socho jaha a == b True hai but a is b False. Aur ek jaha dono True hain.
# answer:


# B3. lst = [1, 2, 3]. lst2 = lst[:] kiya. Kya lst2 nayi list hai ya same list ka reference? Prove karo code se.
# answer:


# B4. Tuple immutable hai — phir bhi uske andar list mutable kaise? Ye contradiction nahi hai? Reason batao.
# answer:


# B5. s = "sohail". s + " ansari" kiya but s change nahi hua. lst + [4] kiya toh bhi lst change nahi hota. Phir list ko mutable kyun kehte hain? Confusion clear karo.
# answer:



# ============================================================
#  MISTAKE NOTEBOOK
# ============================================================

# Mistake 1:
# Mistake 2:
# Mistake 3:
# Mistake 4:
# Mistake 5:
# Mistake 6:
# Mistake 7:
# Mistake 8:
# Mistake 9:
# Mistake 10: