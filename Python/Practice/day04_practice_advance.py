"""
============================================================
  PYTHON - DAY 4 MEGA PRACTICE SET (100 Questions)
  PRIMARY: Day 4 (Dictionary & Set)
  MIXED: Day 1, 2, 3 concepts naturally integrated
============================================================
  STRUCTURE:
  - Easy:        12 Qs
  - Medium:      20 Qs
  - Hard:        25 Qs
  - Super Hard:  25 Qs
  - Ultra Hard:  18 Qs (dimag faad 🔥)
============================================================
"""


# ############################################################
#  SECTION 1: EASY (Q1-Q12)  🟢
#  Time: 30 min
# ############################################################

# Q1. [Output Predict] Dict basic output.
# d = {"name": "sohail", "age": 18, "marks": 90}
# print(len(d))
# print(d["name"])
# print(type(d))
# answer:first 3 second sohail third dict


# Q2. [Output Predict] Set basic output.
# s = {1, 2, 3, 3, 4, 4, 5}
# print(s)
# print(len(s))
# answer:{1,2,3,4,5} second 5


# Q3. [Debugging] Bug kya hai? Fix karo.
# d = {"a": 1, "b": 2}
# d.append({"c": 3})
# print(d)
# answer:bug hai .append dict mai add karne ke liye update use karte hai 
# d = {"a": 1, "b": 2}
# d.update({"c": 3})
# print(d)


# Q4. [Debugging] Bug kya hai? Fix karo.
# s = {1, 2, 3}
# s.append(4)
# print(s)
# answer:.append bug hai set mai add karne ke liye .add() ka use karte hai
# s = {1, 2, 3}
# s.add(4)
# print(s)


# Q5. [Concept] Dict aur Set mein main difference kya hai?
# answer:dict or set dono hi curly braces mai likhte hai and dono hi unorder hote hai but dict key:value pair mai store hota hai and dict mutable hota hai set bhi mutable hota hai but element immutable isiliye set mai dict and list store nahi kar sakte


# Q6. [Code Completion] Blank bharo - dict mein naya key-value add karna hai.
# d = {"a": 1, "b": 2}
# d._____({"c": 3})
# print(d)
# answer:blank mai update aayega


# Q7. [Write a Program] Apne baare mein dict banao (name, age, city). Keys, values, items print karo.
# answer:
# self = {"name":"sohail","age":18,"city":"new delhi"}
# print(self)
# print(self.items())


# Q8. [Write a Program] Set {1, 2, 3, 4, 5} banao. 6 add karo, 1 remove karo, print karo.
# answer:
# st={1, 2, 3, 4, 5}
# st.add(6)
# st.remove(1)
# print(st)


# Q9. [Write a Program] User se naam aur age le. Dict banao {"name": naam, "age": age, "length": len(naam)}. Print karo.
# answer:
# name = input("enter your name: ")
# age = int(input("enter your age: "))
# dic = {"name": name, "age": age, "length_of_name": len(name)}
# print(dic)


# Q10. [Write a Program] Do sets {1, 2, 3} aur {3, 4, 5} lo. Union, intersection, difference print karo.
# answer:
# A = {1, 2, 3} 
# B = {3, 4, 5}
# print(A.union(B))
# print(A.intersection(B))
# print("A-B =",A-A.intersection(B))


# Q11. [Write a Program] Dict {"name": "sohail", "age": 18} mein "city": "Delhi" add karo (update se). Phir "name" key ki value uppercase karke print karo.
# answer:
# dic = {"name": "sohail", "age": 18}
# dic.update({"city": "delhi"})
# print(dic)
# name = dic.get("name")
# print(name.upper())


# Q12. [Write a Program] List [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] ko set mein convert karo. Unique elements print karo. Original list ki length aur set ki length compare karo.
# answer:
# lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# st = set(lst)
# print(st)
# if len(lst)<len(st):
#     print("length of list is smaller than length of set")
# elif len(lst)>len(st):
#     print("length of list is bigger than length of set")
# else:
#     print("both length are equal")



# ############################################################
#  SECTION 2: MEDIUM (Q13-Q32)  🟡
#  Time: 2.5 hrs
# ############################################################

# Q13. [Output Predict] Dict methods output.
# d = {"name": "sohail", "age": 18}
# print(d.keys())
# print(d.values())
# print(list(d.keys()))
# print(d.get("city", "Unknown"))
# answer:dict_keys(['name', 'age']) second dict_values(['sohail', 18]) third ['name', 'age'] fourth Unknown


# Q14. [Output Predict] Set methods output.
# s = {1, 2, 3, 4}
# s.add(5)
# s.add(2)
# s.remove(1)
# print(s)
# print(len(s))
# answer: first {2,3,4,5} and len 4


# Q15. [Output Predict] Nested dict output.
# student = {"name": "sohail", "marks": {"math": 90, "sci": 85}}
# print(student["marks"]["math"])
# print(student["name"].upper())
# print(student["marks"]["math"] + student["marks"]["sci"])
# answer:1st 90 2nd SOHAIL 3rd 175


# Q16. [Output Predict] String + Set mix.
# s = "programming"
# unique = set(s)
# print(unique)
# print(len(s), len(unique))
# answer:1st {"p","r","o","g","a","m","i","n"} 2nd 11 8


# Q17. [Debugging] Bug kya hai? Fix karo.
# d = {"a": 1, "b": 2}
# print(d["c"])
# answer:bug hai ki ham c search kar rahe hai but dict mai c hai nahi so ham .get() use kar sakte hai ya c ko pehle add kar sakte hai
# d = {"a": 1, "b": 2}
# print(d.get("c","not found"))

#or
# d = {"a": 1, "b": 2}
# d["c"] = 3
# print(d["c"])
# print(d)


# Q18. [Debugging] Bug kya hai? Fix karo.
# s = {[1, 2], [3, 4]}
# print(s)
# answer:bug hai ki ham set mai list store kar rahe hai jo ki allowed nahi hai so ham list mai stoe na karke simple store kar sakte hai 
# s = {1, 2, 3, 4}
# print(s)


# Q19. [Debugging] Bug kya hai? Fix karo.
# s = {1, 2, 3}
# s.remove(10)
# print(s)
# answer:bug hai ki isme 10 hai hi nhai or ham remove kar rahe hai so fix hai ki remove line ko hata dena
# s = {1, 2, 3}
# print(s)


# Q20. [Concept] Dict ki key immutable honi chahiye — kyun? Mutable key allowed hoti toh kya problem hoti?
# answer: dict ki immutable honi chahiye kyunki python hash value mai store karta hai or agar change hoti to hash vlaue change hote and difficulty hoti search karne mai isiliye


# Q21. [Concept] `d.get("key")` aur `d["key"]` mein kya farak hai? Kab kaunsa use karoge?
# answer:d.get("key") error nahi deta and d["key"] agar key nahi hai dict mai so ye keyerror de dega


# Q22. [Code Completion] Blank bharo - do dicts merge karo.
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 100, "c": 3}
# d1._____(d2)
# print(d1)
# answer:blank mai update aa jayega
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 100, "c": 3}
# d1.update(d2)
# print(d1)


# Q23. [Code Completion] Blank bharo - do sets ka intersection.
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# result = s1._____(s2) 
# print(result)
# answer:blank mai intersection aa jayega


# Q24. [Write a Program] User se ek word le. Set mein convert karke unique characters print karo. Original word ki length aur unique characters count compare karo.
# answer:
# name = input("enter your name: ")
# unique = set(name)
# print(unique)
# print(len(name)>len(unique))


# Q25. [Write a Program] Nested dict banao student ka — name + marks dict (3 subjects). Har subject ka marks print karo, aur total marks nikalo.
# answer:
# student = {"name":"sohail","marks":{"phy":78,"chem":82,"math":93}}
# print(student["marks"]["phy"])
# print(student["marks"]["chem"])
# print(student["marks"]["math"])
# total = student["marks"]["phy"]+student["marks"]["chem"]+student["marks"]["math"]
# print(total)


# Q26. [Write a Program] User se 5 numbers le (list mein). Set mein convert karke unique numbers print karo. Kitne duplicates the — batao.
# answer:
# a = int(input("1st: "))
# e = int(input("2nd: "))
# b = int(input("3rd: "))
# c = int(input("4th: "))
# d = int(input("5th: "))
# lst =[]
# lst.append(a)
# lst.append(b)
# lst.append(c)
# lst.append(d)
# lst.append(e)
# print(lst)
# unique = set(lst)
# print(unique)
# print("duplicate:",len(lst)-len(unique))


# Q27. [Write a Program] Dict {"math": 90, "science": 85, "english": 95} lo. Highest marks wala subject print karo (bina loop).
# answer:
# d = {"math": 90, "science": 85, "english": 95}

# highest = max(d,key=d.get)

# print("Highest marks subject:", highest)
# print("Marks:", d[highest])


# Q28. [Write a Program] User se ek sentence le. Split karke list banao. Set mein convert karke unique words print karo. Total words aur unique words count batao.
# answer:
# sen = input("enter a sentance: ")
# lst = sen.split()
# print(lst)
# unique = set(lst)
# print("unique word=",unique)
# print("total word enter by user =",len(lst))
# print("total unique word enter by user =",len(unique))


# Q29. [Write a Program] User se naam, age, aur 3 subject marks le. Ek dict banao jisme:
# - name (string), age (int), marks (list), average (float)
# Print karo:
# - Name uppercase
# - Average
# - Agar average >= 80 → "Good" warna "Average"
# answer:
# name = input("Enter name: ")
# age = int(input("Enter age: "))

# sub1 = float(input("Enter marks 1: "))
# sub2 = float(input("Enter marks 2: "))
# sub3 = float(input("Enter marks 3: "))

# marks = [sub1, sub2, sub3]
# average = sum(marks) / len(marks)

# student = {
#     "name": name,
#     "age": age,
#     "marks": marks,
#     "average": average
# }

# print("Name:", student["name"].upper())
# print("Average:", student["average"])

# if student["average"] >= 80:
#     print("Good")
# else:
#     print("Average")


# Q30. [Write a Program] Do sets {1, 2, 3, 4, 5} aur {4, 5, 6, 7} lo. Aise elements ki set banao jo:
# - Dono mein common hain (intersection)
# - Sirf pehle mein hain (difference)
# - Dono mein se kisi ek mein hain (symmetric difference)
# answer:
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7}
# intersection =a.intersection(b)
# diffrence = a-a.intersection(b)
# symmetric = a.symmetric_difference(b)
# print(intersection)
# print(diffrence)
# print(symmetric)


# Q31. [Write a Program] Dict {"name": "sohail", "age": 18, "marks": [85, 92, 78]} lo. Marks ka average nikalo. Dict mein naya key "average" add karo. Final dict print karo.
# answer:
# student = {"name": "sohail", "age": 18, "marks": [85, 92, 78]}
# average = (student["marks"][0]+student["marks"][1]+student["marks"][2])/3
# print(average)
# student.update({"average":average})
# print(student)


# Q32. [Write a Program] User se 2 strings le. Dono ke unique characters ki sets banao. Phir:
# - Common characters (intersection)
# - Saare unique characters (union)
# - Sirf pehli string ke characters (difference)
# answer:
# s = input("enter word: ")
# s2 = input("enter word: ")
# set1 = set(s)
# set2 = set(s2)
# common = set1.intersection(set2)
# all_char = set1.union(set2)
# only_set1_char = set1-common
# print(common)
# print(all_char)
# print(only_set1_char)



# ############################################################
#  SECTION 3: HARD (Q33-Q57)  🟠
#  Time: 3.5 hrs
# ############################################################

# Q33. [Output Predict] Dict view dynamic.
# d = {"a": 1, "b": 2}
# keys = d.keys()
# print(list(keys))
# d.update({"c": 3})
# print(list(keys))
# print(len(keys))
# answer:first [a,b] 2nd [a,b,c] 3rd 3


# Q34. [Output Predict] Set pop random.
# s = {1, 2, 3, 4, 5}
# x = s.pop()
# y = s.pop()
# print(len(s))
# print(x + y)  # Kya ye deterministic hai?
# answer:first len 3 second pop random vlaue remive karta hai isiliye ye non determinsitic hua


# Q35. [Output Predict] String + Dict + List mix.
# name = "sohail"
# marks = [85, 92, 78]
# d = {"name": name, "marks": marks, "avg": (marks[0] + marks[1] + marks[2]) / 3}
# print(d["name"].upper())
# print(d["marks"][1])
# print(d["avg"] >= 85)
# answer:1st SOHAIL 2nd 92 3rd True


# Q36. [Output Predict] Nested set trap.
# s = {1, 2, 3}
# x = s
# y = s.copy()
# x.add(4)
# y.add(5)
# print(s)
# print(y)
# print(s is x)
# print(s is y)
# answer:1st {1,2,3,4} 2nd {1,2,3,5} 3rd True false


# Q37. [Output Predict] Tuple as dict key.
# d = {(1, 2): "a", (3, 4): "b"}
# print(d[(1, 2)])
# print(len(d))
# d[(1, 2, 3)] = "c"   # ye line kya karegi?
# answer: 1st a second 2 and d[(1, 2, 3)] = "c" ye dict mai new bana dega 


# Q38. [Debugging] Bug kya hai? Fix karo.
# d = {"a": 1, "b": 2}
# d.update("c", 3)
# print(d)
# answer: bug hai ki isme update mai c:3 ye curly bracet mai nahi hai and semicolon ki jagah commar laga hai isliye
# d = {"a": 1, "b": 2}
# d.update({"c":3})
# print(d)


# Q39. [Debugging] Bug kya hai? Fix karo.
# s = {1, 2, 3}
# x = s.pop(2)
# print(x)
# answer:pop ke andar 2 kyunki pop random value remove karta ha or agar hame 2 remove karna hai to pop ki jagah remive aayega


# Q40. [Debugging] Bug kya hai? Fix karo.
# d = {"a": 1, "b": 2}
# keys = d.keys()
# print(keys[0])
# answer:isme bug hai keys[0] yunki .key normal list mai output nahi deta hai dict view mai deta hai isliye bug hai agar hame chahiye [0] so ham keys ko list mai chnage kar sakte hai 
# d = {"a": 1, "b": 2}
# keys = list(d.keys())
# print(keys[0])


# Q41. [Debugging] Bug kya hai? Fix karo.
# d = {"name": "sohail", "marks": [85, 92]}
# print(d["marks"][5])
# answer: bug hai ki makrs mai 2 hi value hai and ye 5th search kar raha  index out of range isliye


# Q42. [Concept] Set unordered hota hai — iska kya matlab? Set pe indexing kyun nahi chalti? Ek real-world example do jaha set better ho list se.
# answer:Set unordered hota hai matlab uske elements ka order fix nahi hota. Isiliye set pe indexing kaam nahi karti, kyunki hum uske elements ko index number se access nahi kar sakte.
#Real-world example: Agar mujhe students ke unique names store karne hain aur duplicate names nahi chahiye, toh list ki jagah set use kar sakte hain, kyunki set automatically duplicate values hata deta hai.


# Q43. [Concept] Dict ki keys view, values view, items view — ye "dynamic" kyun hote hain? Example do.
# answer: key value item  ye sab dyanmic hote hai jise  ham jab bhi dict mai change karenge to ye directily key value item view bhi change hoga 
# ex:
# d = {"a": 1, "b": 2}

# keys = d.keys()
# print(keys)

# d["c"] = 3
# print(keys)


# Q44. [Concept] Set ke andar list nahi daal sakte but tuple daal sakte hain — kyun?
# answer: Set ke elements hashable hone chahiye. List mutable hoti hai aur hashable nahi hoti, isliye use set mein nahi daal sakte. Tuple immutable hota hai, isliye use daal sakte hain agar uske saare elements hashable hon.

# Q45. [Code Completion] Blank bharo - dict se value safely nikaalo.
# d = {"a": 1, "b": 2}
# val = d._____("c", 0)
# print(val)
# answer: blank mai get aayega
# d = {"a": 1, "b": 2}
# val = d.get("c", 0)
# print(val)


# Q46. [Code Completion] Blank bharo - set se element hatao (error ke bina).
# s = {1, 2, 3}
# s._____(10)
# print(s)
# answer:blank mai discard aayega
# s = {1, 2, 3}
# s.discard(10)
# print(s)

# Q47. [Write a Program] User se ek sentence le. Dict banao jisme har unique word ki length ho: {"python": 6, "is": 2, ...}. (Bina loop — manually socho)
# answer:
# s = input("enter a sentance: ")
# st = set(s.split())
# lst = list(st)
# print(st)
# dic = {
#     lst[0]:len(lst[0])
# }
# print(dic)
#or
# s = input("Enter a sentence: ")
# words = set(s.split())

# dic = {word: len(word) for word in words}

# print(dic)


# Q48. [Write a Program] User se 5 numbers le (list mein). Un sab ka set banao. Phir check karo:
# - Kitne unique numbers hain
# - Kaunsa number sabse zyada baar aaya (Hint: list.count() use karo)
# answer:
# first = int(input("enter 1st: "))
# second = int(input("enter 2nd: "))
# third = int(input("enter 3rd: "))
# fourth = int(input("enter 4th: "))
# fifth = int(input("enter 5th: "))
# lst = []
# lst.append(first)
# lst.append(second)
# lst.append(third)
# lst.append(fourth)
# lst.append(fifth)
# unique = set(lst)
# print("there are",len(unique),"unique charachter")
# max_count = max(lst.count(x) for x in unique)
# a = [x for x in unique if lst.count(x) == max_count]

# print("Most repeated number(s):", a)


# Q49. [Write a Program] Do lists: a = [1, 2, 3, 4, 5], b = [3, 4, 5, 6, 7]. Dono ko set mein convert karo. Phir:
# - Common elements ki list
# - Sirf pehli list ke elements
# - Dono ke combined unique elements
# answer:
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# set1 = set(a)
# set2 = set(b)
# print("common element =",set1.intersection(set2))
# print("only element of list a =",set1-(set1.intersection(set2)))
# print("unique element in both =",set1.symmetric_difference(set2))


# Q50. [Write a Program] Inventory system simulate karo:
# items = ["pen", "book", "pencil", "eraser"]
# prices = [10, 50, 5, 3]
# quantity = [100, 20, 200, 150]
# User se item naam lo:
# - Agar mile → index dhundho, price, quantity, total value print karo
# - Warna → "Item not found"
# answer:
# items = ["pen", "book", "pencil", "eraser"]
# prices = [10, 50, 5, 3]
# quantity = [100, 20, 200, 150]
# user = input("enter your item: ")
# if user in items:
#     idx = items.index(user)
#     print("price of this item is:",prices[idx])
#     print("quantity of this item is:",quantity[idx])
#     print("your total value is:",(prices[idx])*(quantity[idx]))
# else:
#     print("Item not found")


# Q51. [Write a Program] User se ek paragraph le. Dict banao:
# - "words": total words count
# - "chars": total characters (bina spaces)
# - "unique_words": set ki length
# - "longest": longest word
# answer:
# para = input("enter a paragraph: ")
# lst = list(para.split())
# char = para.replace(" ","")
# dic = {
#     "words":len(lst),
#     "chars":len(char),
#     "unique_words":len(set(lst)),
#     "longest": max(lst, key=len) if lst else ""
# }
# print(dic)


# Q52. [Write a Program] User se naam, age, aur skills list le. Ek dict banao:
# {"name": ..., "age": ..., "skills": set(skills), "total_skills": len(set(skills))}
# Print karo. Agar total_skills > 3 → "Multi-skilled" warna "Learning"
# answer:
# name = input("enter your name: ")
# age = int(input("enter your age: "))
# skills = list(input("enter your skills: ").split())
# dic = {
#     "name":name,
#     "age":age,
#     "skills":set(skills),
#     "total skills": len(set(skills))
# }
# print(dic)
# if dic["total skills"]> 3:
#     print("multi-skilled")
# else:
#     print("learning")


# Q53. [Write a Program] Do dicts: d1 = {"a": 1, "b": 2, "c": 3}, d2 = {"b": 100, "c": 200, "d": 4}. Naya dict banao jisme d1 ke saare aur d2 ke saare keys hon. Agar key dono mein hai toh d2 ki value use karo.
# answer:
# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 100, "c": 200, "d": 4}

# d3 = d1.copy()
# d3.update(d2)
# print(d3)


# Q54. [Write a Program] Student data:
# names = ["sohail", "rahul", "priya"]
# marks = [[85, 92], [78, 88], [95, 90]]
# Dict banao {name: [marks]}. Phir har student ka average nikaal ke print karo. Highest average wale ka naam print karo.
# answer:
# names = ["sohail", "rahul", "priya"]
# marks = [[85, 92], [78, 88], [95, 90]]

# dic = {
#     names[0]: marks[0],
#     names[1]: marks[1],
#     names[2]: marks[2]
# }

# avg1 = sum(dic["sohail"]) / len(dic["sohail"])
# avg2 = sum(dic["rahul"]) / len(dic["rahul"])
# avg3 = sum(dic["priya"]) / len(dic["priya"])

# print("sohail Average:", avg1)
# print("rahul Average:", avg2)
# print("priya Average:", avg3)

# if avg1 > avg2 and avg1 > avg3:
#     print("Highest average: sohail")
# elif avg2 > avg1 and avg2 > avg3:
#     print("Highest average: rahul")
# else:
#     print("Highest average: priya")


# Q55. [Write a Program] User se ek string le. Dict banao jisme har character ka count ho:
# {"s": 2, "o": 1, "h": 1, ...}
# (Bina loop — manually socho. Har character ke liye count() use karo)
# answer:
# s = input("enter a string: ")
# dic = {}
# for char in s:
#     dic[char] = s.count(char)
# print(dic)


# Q56. [Write a Program] Set theory: 3 sets banao:
# python_devs = {"sohail", "rahul", "priya"}
# ml_devs = {"sohail", "priya", "vikas"}
# ai_devs = {"priya", "vikas", "neha"}
# Print karo:
# - Sabhi unique developers
# - Jo sirf python jaante hain
# - Jo teeno jaante hain
# - Jo kam se kam 2 jaante hain
# answer:
# python_devs = {"sohail", "rahul", "priya"}
# ml_devs = {"sohail", "priya", "vikas"}
# ai_devs = {"priya", "vikas", "neha"}
# print("All unique developers:", python_devs.union(ml_devs).union(ai_devs))
# print("Only python developers:", python_devs - ml_devs - ai_devs)
# print("Developers who know all three:", python_devs.intersection(ml_devs).intersection(ai_devs))
# at_least_two = (python_devs.intersection(ml_devs)).union(python_devs.intersection(ai_devs)).union(ml_devs.intersection(ai_devs))
# print("Developers who know at least two:", at_least_two)


# Q57. [Write a Program] User se ek sentence le. Ek dict banao jisme:
# - "vowels": set of vowels
# - "consonants": set of consonants
# - "count_vowels": len of vowels set
# - "count_consonants": len of consonants set
# Print karo. Agar vowels > consonants → "Vowel heavy" warna "Consonant heavy"
# answer:
# sen = input("enter a sentence: ")
# vowels_set = set()
# consonants_set = set()

# for char in sen:
#     if char.lower() in "aeiou":
#         vowels_set.add(char)
#     elif char.isalpha():
#         consonants_set.add(char)

# print("Vowels:", vowels_set)
# print("Consonants:", consonants_set)
# print("Count of Vowels:", len(vowels_set))
# print("Count of Consonants:", len(consonants_set))

# if len(vowels_set) > len(consonants_set):
#     print("Vowel heavy")
# else:
#     print("Consonant heavy")



# ############################################################
#  SECTION 4: SUPER HARD (Q58-Q82)  🔴
#  Time: 5 hrs
# ############################################################

# Q58. [Output Predict] Dict with mutable values.
# d = {"list1": [1, 2], "list2": [3, 4]}
# d["list1"].append(5)
# d["list2"] = d["list2"] + [5]
# print(d)
# print(d["list1"] is d["list2"])
# answer:


# Q59. [Output Predict] Set of tuples.
# lst = [(1, 2), (3, 4), (1, 2), (5, 6)]
# s = set(lst)
# print(s)
# print(len(lst), len(s))
# answer:


# Q60. [Output Predict] Nested dict + list modification.
# data = {
#     "user": {
#         "profile": {"name": "sohail", "skills": ["python", "ml"]}
#     }
# }
# data["user"]["profile"]["skills"].append("ai")
# data["user"]["profile"]["skills"].append("python")
# print(data["user"]["profile"]["skills"])
# print(len(data["user"]["profile"]["skills"]))
# print(len(set(data["user"]["profile"]["skills"])))
# answer:


# Q61. [Output Predict] Tuple in dict, list in set trap.
# d = {"coords": (1, 2), "nums": [3, 4]}
# print(d["coords"][0])
# print(d["nums"][-1])
# # s = {d["nums"]}  # ye line kya karegi?
# answer:


# Q62. [Output Predict] Dict merge + set conversion.
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 100, "c": 3}
# d3 = d1.copy()
# d3.update(d2)
# print(d3)
# print(len(d3))
# print(set(d3.keys()))
# print(set(d3.values()))
# answer:


# Q63. [Debugging] Bug kya hai? Fix karo.
# data = {
#     "students": [
#         {"name": "sohail", "marks": [85, 92]},
#         {"name": "rahul", "marks": [78, 88]}
#     ]
# }
# print(data["students"]["name"])
# answer:


# Q64. [Debugging] Bug kya hai? Fix karo.
# s = {1, 2, 3}
# for x in s:  # loop allowed nahi, but bug identify karo
#     s.add(x + 10)
# print(s)
# answer:


# Q65. [Debugging] Bug kya hai? Fix karo.
# d = {"a": 1, "b": 2}
# val = d.pop("c")
# print(val)
# answer:


# Q66. [Concept] Shallow copy aur deep copy mein farak — dict aur set ke reference mein samjhao. Example do.
# answer:


# Q67. [Concept] `set` aur `frozenset` mein kya farak hai? frozenset kab use karoge? (frozenset tune padha nahi — sirf soch ke batao)
# answer:


# Q68. [Code Completion] Blank bharo - dict ki saari keys ki sorted list banao.
# d = {"c": 3, "a": 1, "b": 2}
# keys = _____(d.keys())
# keys._____()
# print(keys)
# answer:


# Q69. [Code Completion] Blank bharo - set se duplicate list banao.
# lst = [1, 2, 2, 3, 3, 3, 4]
# unique = _____(lst)
# print(unique)
# print(_____(unique))
# answer:


# Q70. [Write a Program] Mini library management:
# books = ["Python", "ML", "AI", "Data Science"]
# authors = ["Guido", "Andrew", "Yann", "Andrew"]
# User se book naam lo. Agar book list mein hai:
# - uska index dhundho
# - author print karo
# - "Book available"
# Warna: "Not available"
# Saath mein: authors se unique authors ki set banao aur print karo.
# answer:


# Q71. [Write a Program] User se ek sentence le. Dict banao:
# - Har word ki length: {word: len(word)}
# - Longest word
# - Shortest word
# - Average word length
# answer:


# Q72. [Write a Program] Quiz app:
# questions = ["Capital of India?", "2+2?", "Python creator?"]
# answers = ["Delhi", "4", "Guido"]
# User se 3 answers input lo (ek-ek karke).
# Har sahi answer ke liye score +1.
# Final score print karo.
# - Score == 3 → "Perfect!"
# - Score == 2 → "Good"
# - Score == 1 → "Try harder"
# - Warna → "Better luck next time"
# answer:


# Q73. [Write a Program] Product bill:
# User se: product_name, price, quantity, discount% le.
# - subtotal = price × quantity
# - discount_amount = subtotal × discount / 100
# - final = subtotal - discount_amount
# Ek dict banao aur print karo:
# {"product": ..., "subtotal": ..., "discount": ..., "final": ...}
# - Agar final > 1000 → "Premium" warna "Regular"
# answer:


# Q74. [Write a Program] Student report card:
# User se: naam, roll_no, 5 subject marks (list), skills (list).
# Generate karo:
# - total (bina sum())
# - avg
# - grade: >=90 "A+", >=80 "A", >=70 "B", >=60 "C", warna "F"
# - sorted marks
# - highest, lowest
# - unique skills (set)
# - Final dict: {"name": ..., "roll": ..., "total": ..., "avg": ..., "grade": ..., "skills": ...}
# answer:


# Q75. [Write a Program] Employee database:
# names = ["sohail", "rahul", "priya"]
# salaries = [50000, 75000, 60000]
# departments = ["IT", "HR", "IT"]
# Dict banao {name: {"salary": ..., "dept": ...}}.
# Print karo:
# - IT department ke saare employees
# - Highest salary wala employee
# - Average salary
# - Unique departments (set)
# answer:


# Q76. [Write a Program] User se do sentences le. Dono ke unique words ki sets banao. Print karo:
# - Common words (intersection)
# - Saare unique words (union)
# - Sirf pehle sentence ke words (difference)
# - Sirf dusre sentence ke words (difference)
# answer:


# Q77. [Write a Program] Nested dict:
# data = {
#     "student1": {"name": "sohail", "marks": [85, 92, 78]},
#     "student2": {"name": "rahul", "marks": [78, 88, 92]},
#     "student3": {"name": "priya", "marks": [95, 90, 88]}
# }
# Har student ka average nikaalo. Dict banao {name: avg}. Highest avg wale ka naam print karo.
# answer:


# Q78. [Write a Program] Text analyzer:
# User se ek paragraph le.
# Dict banao:
# - total_words
# - unique_words (set ki length)
# - total_chars (bina spaces)
# - vowels_set
# - consonants_set
# - most_common_word (list.count() use karo)
# answer:


# Q79. [Write a Program] Shopping cart:
# cart = {"apple": 3, "banana": 2, "cherry": 5}  # qty
# prices = {"apple": 50, "banana": 20, "cherry": 100}
# Har item ka total (qty × price) nikaalo. Grand total nikaalo.
# Final dict print karo: {item: {"qty": ..., "price": ..., "total": ...}}
# answer:


# Q80. [Write a Program] User se ek sentence le aur ek dict banao jisme har character ka count ho. Phir:
# - Sabse zyada baar aane wala character
# - Sabse kam baar aane wala character
# - Sirf vowels ka set
# - Sirf consonants ka set
# answer:


# Q81. [Write a Program] Inventory with categories:
# products = ["pen", "book", "pencil", "eraser", "notebook"]
# categories = ["stationery", "stationery", "stationery", "stationery", "stationery"]
# prices = [10, 50, 5, 3, 30]
# Dict banao {product: {"category": ..., "price": ...}}.
# Print karo:
# - Saare products jinki price < 20
# - Unique categories
# - Total inventory value (sum of all prices)
# answer:


# Q82. [Write a Program] User se ek string le. Isme se:
# - Duplicate characters hata ke naya string banao (set use karo)
# - Original string aur naya string ki length compare karo
# - Sabse zyada baar aane wala character nikaalo
# - Ek dict banao {char: count} aur print karo
# answer:



# ############################################################
#  SECTION 5: ULTRA HARD / DIMAG FAAD (Q83-Q100)  💀🔥
#  Time: 6 hrs
#  Ye woh questions hain jo top 1% interview level ke hain
# ############################################################

# Q83. [Output Predict] Reference trap in dict.
# a = {"x": [1, 2]}
# b = a
# c = a.copy()
# a["x"].append(3)
# c["x"].append(4)
# b["y"] = 5
# print(a)
# print(b)
# print(c)
# print(a is b)
# answer:


# Q84. [Output Predict] Set comprehension with tuples.
# pairs = [(1, 2), (2, 3), (1, 2), (4, 5)]
# s = set(pairs)
# print(s)
# print(len(pairs), len(s))
# print((1, 2) in s)
# print((2, 1) in s)
# answer:


# Q85. [Output Predict] Nested mutable trap.
# d = {"a": {"b": [1, 2]}}
# d2 = d.copy()
# d2["a"]["b"].append(3)
# d2["a"]["c"] = "new"
# print(d)
# print(d2)
# answer:


# Q86. [Debugging] Bug kya hai? Fix karo.
# data = {
#     "marks": {"math": 90, "sci": 85}
# }
# keys = list(data["marks"].keys())
# print(keys[0])
# print(keys[-1])
# print(data["marks"][keys[0]] + data["marks"][keys[1]])
# answer:


# Q87. [Debugging] Bug kya hai? Fix karo.
# s = {1, 2, 3}
# s2 = s
# s2.add(4)
# s3 = s.copy()
# s3.add(5)
# print(s)
# print(s3)
# print(s is s2)
# print(s is s3)
# answer:


# Q88. [Concept] Dict view objects dynamic kyun hote hain? Ye design decision kyun liya gaya? Ek use case batao.
# answer:


# Q89. [Concept] Set ki internal implementation (hash table) ke baare mein socho. Set mein `in` operator O(1) kyun hota hai jabki list mein O(n)? (Tune padha nahi — sirf soch ke batao)
# answer:


# Q90. [Concept] Tuple as dict key kyun kaam karta hai but list nahi? Immutability ka role samjhao.
# answer:


# Q91. [Write a Program] User se ek paragraph le. Dict banao:
# - Har word ka count: {word: count}
# - Sabse zyada baar aane wala word
# - Sabse kam baar aane wala word
# - Total unique words
# - Total words
# - Agar unique_words / total_words > 0.5 → "Rich vocabulary" warna "Repetitive"
# answer:


# Q92. [Write a Program] Complete student management system:
# User se 3 students ka data lo:
# - naam, roll, 5 marks, skills
# Data structure banao: {
#     roll1: {"name": ..., "marks": [...], "skills": set(...), "avg": ..., "grade": ...}
# }
# Print karo:
# - Sabhi students ka data
# - Highest avg wala student
# - Saare unique skills (union of all)
# - Saare common skills (intersection of all)
# answer:


# Q93. [Write a Program] E-commerce cart:
# products = ["laptop", "phone", "tablet"]
# prices = [50000, 20000, 30000]
# cart_items = ["laptop", "phone", "laptop", "tablet"]
# # cart_items mein jo bhi products hain unka:
# - unique items ki set banao
# - har item ka count nikaalo (list.count() se)
# - har item ka total (price × count)
# - grand total
# - Final dict: {item: {"price": ..., "qty": ..., "total": ...}, "grand_total": ...}
# answer:


# Q94. [Write a Program] Student grades analyzer:
# students = {
#     "sohail": [85, 92, 78, 88, 95],
#     "rahul": [78, 88, 82, 90, 85],
#     "priya": [95, 90, 88, 92, 96],
#     "vikas": [70, 75, 68, 72, 65]
# }
# Har student ka avg nikaalo. Grade assign karo (>=90 A+, >=80 A, >=70 B, warna C).
# Final dict: {name: {"avg": ..., "grade": ...}}
# Topper print karo. Unique grades ki set print karo.
# answer:


# Q95. [Write a Program] Text to frequency map:
# User se ek paragraph le.
# Dict banao jisme:
# - Har character ka count
# - Har word ka count
# - Total unique chars
# - Total unique words
# - Sabse zyada common char
# - Sabse zyada common word
# - Agar common char zyada hai → "Char heavy", warna "Word heavy"
# answer:


# Q96. [Write a Program] Library + members:
# books = {"Python": 5, "ML": 3, "AI": 2}  # available copies
# members = {"sohail", "rahul", "priya", "vikas"}
# issued = {
#     "sohail": ["Python", "ML"],
#     "rahul": ["AI"],
#     "priya": ["Python", "AI"]
# }
# Print karo:
# - Kaunsa book sabse zyada issued hai
# - Kaunsa member sabse zyada books le chuka hai
# - Kaunse members ne kuch issue nahi kiya (set difference)
# - Har book ki available copies ab kya hain
# answer:


# Q97. [Write a Program] Multi-class inventory:
# data = {
#     "electronics": ["phone", "laptop", "tv"],
#     "furniture": ["chair", "table"],
#     "clothing": ["shirt", "pant", "shirt"]
# }
# Print karo:
# - Har category ke unique items
# - Total unique items across all categories
# - Categories jisme duplicate items hain
# - Sabse zyada items wali category
# - Ek final dict: {category: {"unique": ..., "total": ...}}
# answer:


# Q98. [Write a Program] Employee salary analysis:
# employees = {
#     "sohail": {"dept": "IT", "salary": 50000},
#     "rahul": {"dept": "HR", "salary": 45000},
#     "priya": {"dept": "IT", "salary": 75000},
#     "vikas": {"dept": "HR", "salary": 55000}
# }
# Print karo:
# - Unique departments (set)
# - Har department ka average salary
# - Highest paid employee
# - Har department ke employees ki list
# - Final dict: {dept: {"employees": [...], "avg_salary": ...}}
# answer:


# Q99. [Write a Program] Word frequency + sentiment:
# User se ek paragraph le.
# positive_words = {"good", "great", "excellent", "amazing", "best"}
# negative_words = {"bad", "worst", "poor", "terrible", "hate"}
# Dict banao:
# - Har word ka count
# - Positive words count (set intersection se)
# - Negative words count
# - Sentiment: positive > negative → "Positive", negative > positive → "Negative", warna "Neutral"
# - Final output print karo
# answer:


# Q100. [FINAL ULTIMATE - All Days] Complete mini database:
# User se 3 students ka data le:
# - naam, roll_no, 5 marks, skills (comma separated)
#
# Build karo:
# students = {
#     roll: {
#         "name": ..., "marks": [...], "skills": set(...),
#         "total": ..., "avg": ..., "grade": ..., "rank": ...
#     }
# }
#
# Print karo:
# - Sabhi students sorted by avg (highest first)
# - Har student ka rank (1, 2, 3)
# - Saare unique skills (union)
# - Saare common skills (intersection)
# - Class average
# - Topper ka naam
# - Lowest scorer ka naam
# - Grade distribution (kitne A+, kitne A, etc.) — dict use karo
# - Ek final summary dict print karo
# answer:



# ############################################################
#  LEARNING NOTEBOOK
# ############################################################

# LEARNING 1:Q20 dict ki immutable honi chahiye kyunki python hash value mai store karta hai or agar change hoti to hash vlaue change hote and difficulty hoti search karne mai isiliye
# LEARNING 2:Q21 d.get("key") error nahi deta and d["key"] agar key nahi hai dict mai so ye keyerror de dega
# LEARNING 3:Q27 max(d,key=d.get) ye max value returen karta hai max function adn key = iska kaam hota hai ki kis basis pe compare karna hai 
# LEARNING 4:Q30 a.symmetric_difference(b) new method so ye symmetric diffrence ke liye hai

# LEARNING 5:Q42 Set unordered hota hai matlab uske elements ka order fix nahi hota. Isiliye set pe indexing kaam nahi karti, kyunki hum uske elements ko index number se access nahi kar sakte. Real-world example: Agar mujhe students ke unique names store karne hain aur duplicate names nahi chahiye, toh list ki jagah set use kar sakte hain, kyunki set automatically duplicate values hata deta hai.
# LEARNING 6:Q44 Set ke elements hashable hone chahiye. List mutable hoti hai aur hashable nahi hoti, isliye use set mein nahi daal sakte. Tuple immutable hota hai, isliye use daal sakte hain agar uske saare elements hashable hon.
# LEARNING 7:Q46 discard() ye bhi set se remove karta hai but agar value set mai nahi hai to error nahi deta 
# LEARNING 8:Q47 word: len(word) for word in words = dictionary comprehension

# LEARNING 9:Q51 "longest": max(lst, key=len) if lst else ""

# ############################################################
#  MISTAKE NOTEBOOK
# ############################################################

# Mistake 1:
# Mistake 2:
# Mistake 3:
# Mistake 4:
# Mistake 5: