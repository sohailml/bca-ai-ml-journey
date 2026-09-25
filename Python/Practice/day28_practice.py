# 🐍 Practice Set (75 Questions) for Python Basics — Day 2

"""
🟢 Category 1: Warm-Up — Q1-Q6
Q1. String ke andar apostrophe (') use karna ho toh kaunsa quote use karein? Example do.

Q2. \n aur \t ka kya kaam hai? Dono ka ek-ek example likho.

Q3. len() kya return karta hai? len("soh ail") ka output kya hoga?

Q4. Positive index aur negative index mein kya farak hai? Example se samjhao.

Q5. Slicing mein last index include hota hai ya nahi? str[0:3] mein kitne characters aayenge?

Q6. find() aur count() mein kya farak hai? Dono kab use hote hain?

🔵 Category 2: Output Predict — Q7-Q22
Q7.
str1 = "Sohail"
str2 = "Ansari"
print(str1 + str2)
print(str1 + " " + str2)

Q8.
print("Hello\nWorld")
print("Hello\tWorld")

Q9.
s = "sohail"
print(len(s))
print(s[2])
print(s[-4])

Q10.
s = "sohail"
print(s[0:3])
print(s[:3])
print(s[1:])
print(s[:])

Q11.
s = "sohail"
print(s[-6:-3])
print(s[-3:])
print(s[:-3])

Q12.
s = "sohail"
print(s.endswith("l"))
print(s.endswith("z"))
print(s.endswith("ail"))

Q13.
s = "sohail"
print(s.capitalize())
print(s)
Kya s ki original value change hoti hai?

Q14.
s = "i am learning html"
print(s.replace("html", "python"))
print(s)

Q15.
s = "sohail is learning"
print(s.find("l"))
print(s.find("learning"))
print(s.find("xyz"))

Q16.
s = "arbaaz"
print(s.count("a"))
print(s.count("z"))
print(s.count("ar"))

Q17.
age = 24
if age >= 18:
    print("can vote")
elif age == 17:
    print("can not vote but apply for pan card")
else:
    print("can not vote")

Q18.
age = 17
if age >= 18:
    print("can vote")
elif age == 17:
    print("can not vote but apply for pan card")
else:
    print("can not vote")

Q19.
age = 15
if age >= 18:
    print("can vote")
elif age == 17:
    print("can not vote but apply for pan card")
else:
    print("can not vote")

Q20.
a = 20
if a > 0:
    if a % 2 == 0:
        print("a is positive and even")
    else:
        print("a is positive and odd")
elif a == 0:
    print("a is 0")
else:
    print("a is negative")

Q21.
a = -7
if a > 0:
    if a % 2 == 0:
        print("a is positive and even")
    else:
        print("a is positive and odd")
elif a == 0:
    print("a is 0")
else:
    print("a is negative")

Q22.
a = 0
if a > 0:
    if a % 2 == 0:
        print("a is positive and even")
    else:
        print("a is positive and odd")
elif a == 0:
    print("a is 0")
else:
    print("a is negative")

🟡 Category 3: Logic Building — Q23-Q34
Q23. s = "programming". Iska last 3 characters nikalo slicing se.

Q24. s = "programming". Iska pehla aur aakhri character print karo.

Q25. s = "python". Slicing se "tho" print karo.

Q26. s = "hello world". Slicing se "world" print karo.

Q27. s = "abcdefgh". Slicing se "bdfh" kaise nikaaloge? (Hint: step slicing — s[start:end:step] — ye tune padha nahi but try karo, agar na aaye skip karo)

Q28. s = "Sohail". Isko reverse karo slicing se. (Hint: s[::-1])

Q29. s = "python". s[1:100] ka output kya hoga? Error aayega ya nahi?

Q30. Ek string s = "madam" hai. Bina reverse built-in use kiye, sirf slicing aur comparison se check karo ki ye palindrome hai ya nahi — output True/False print karo.

Q31. name = "sohail". Agar main name.capitalize() call karu aur result kisi variable mein store na karu, toh kya original name change hoga? Reason batao.

Q32. Ek string s = "i love python". Isme "python" ko "java" se replace karo aur naya string print karo.

Q33. User se ek naam input lo. Agar naam ki length 5 se zyada hai toh "Long name" print karo, warna "Short name" print karo. (if-else allowed)

Q34. User se ek character input lo. Check karo wo vowel hai ya nahi — sirf if-elif-else se (5 vowels ke liye 5 elif ya in operator — in tune padha nahi, toh if-elif-else use karo).

🟠 Category 4: Tricky / Edge Case — Q35-Q46
Q35. s = "sohail". s[10] chalega? Kya error aayega?

Q36. s = "sohail". s[2:10] chalega? Error aayega ya kuch return karega?

Q37. s = "sohail". s[-10] chalega? Kya hoga?

Q38.
s = "sohail"
print(s[3:1])
Kya output aayega?

Q39. s = "" (empty string). len(s) kya dega? s[0] chalega?

Q40. Ye code:

s = "sohail"
s.capitalize()
print(s)
Output kya aayega? "Sohail" ya "sohail"? Kyun?

Q41. Ye code:

s = "sohail"
s = s.capitalize()
print(s)
Ab output kya aayega?

Q42. print("Sohail" == "sohail") — True ya False? Kyun?

Q43. print("a" < "b") — True ya False? Aur print("Z" < "a") — True ya False? (Hint: ASCII values)

Q44. s = "hello". s.find("l") aur s.rfind("l") mein kya farak hoga? (rfind tune padha nahi, skip kar sakte ho — but try karo)

Q45. Ye code:

a = 5
if a > 0:
    print("positive")
elif a > 10:
    print("greater than 10")
else:
    print("other")
Output kya aayega? a = 5 hai toh a > 10 wala elif kabhi chalega kya? Reason batao.

Q46. Ek hi if mein and, or, not use karke check karo: age = 25, has_id = True. Agar age >= 18 and has_id toh "Allowed" print karo warna "Not allowed".

🔴 Category 5: Debugging — Q47-Q56
Q47.
str = "I'm Sohail"
print(str)
Kya error aayega? Fix karo (do tarike batao).

Q48.
s = "sohail"
print(s[6])
Bug kya hai?

Q49.
s = "sohail"
print(s.length())
Bug kya hai?

Q50.
s = "sohail"
print(len[s])
Bug kya hai?

Q51.
s = "i am learning html"
s.replace("html", "python")
print(s)
Output kya aayega — python wala ya html wala? Fix karo.

Q52.
age = 20
if age >= 18:
print("can vote")
Kya error aayega?

Q53.
age = 20
if (age >= 18)
    print("can vote")
Kya error aayega?

Q54.
a = 10
if a > 5:
    print("A")
elif a > 7:
    print("B")
else:
    print("C")
Output kya aayega? Kya "B" print hoga? Reason batao.

Q55.
name = "sohail"
if name = "sohail":
    print("match")
Bug kya hai?

Q56.
s = "sohail"
print(s[2:])
print(s[:2])
print(s[2:2])
Teeno ka output batao. Teesre ka kya aayega?

🟣 Category 6: Challenge — Q57-Q66
Q57. s = "programming". Slicing se "gram" aur "ming" dono alag-alag print karo.

Q58. s = "abcdef". Slicing se "ace" aur "bdf" nikaalo. (Hint: step slicing)

Q59. Ek string s = "12345". Iska reverse print karo bina koi loop use kiye.

Q60. s = "hello". s.capitalize() ke baad len() same rahega ya change hoga? Reason batao.

Q61. Ek string s = "sohail". Iska first character aur last character compare karo (True/False print karo).

Q62. Ek string s = "i love python programming". Isme kitne spaces hain count karo (sirf count() use karo).

Q63. s = "banana". s.count("an") aur s.count("a") — dono ka output batao. Farak samjhao.

Q64. Ek string input lo. Agar uski length even hai toh "Even length", warna "Odd length" print karo.

Q65. User se ek number (string form mein) input lo. Bina int() use kiye, sirf len() aur slicing se batao wo 3-digit hai, 4-digit, ya other — if-elif-else se.

Q66. Ek string s = "racecar". Check karo palindrome hai ya nahi — slicing + comparison se. Phir s = "hello" pe bhi try karo.

🟩 Category 7: Write a Program — Q67-Q75
Q67. Program likho jo apna full name print kare — first_name aur last_name ko concatenate karke, beech mein space daal ke.

Q68. Program likho jo ek string s = "Hello World" ki length print kare, aur uska first 5 characters aur last 5 characters alag-alag print kare.

Q69. Program likho jo user se ek word input le aur uska reverse print kare (slicing se).

Q70. Program likho jo user se ek sentence input le aur usme "a" kitni baar aaya hai count karke print kare.

Q71. Program likho jo user se age input le (int mein convert karke):

Agar age >= 18 → "Adult"

Agar age >= 13 aur < 18 → "Teenager"

Warna → "Child"

Q72. Program likho jo user se do numbers input le aur batao dono mein bada kaunsa hai (if-elif-else se). Agar dono equal ho toh "Equal" print karo.

Q73. Program likho jo user se ek character input le aur check karo:

Vowel (a, e, i, o, u) → "Vowel"

Warna → "Consonant"

Q74. Program likho jo user se username aur password input le:

Agar username "admin" aur password "1234" → "Login successful"

Warna → "Invalid credentials"

Q75. Program likho jo user se ek string input le aur:

Agar string palindrome hai → "Palindrome"

Warna → "Not palindrome"
"""

#ANSWER


# 1 - apostrophe use karne ke liye ham double quate ka use karenge ex:
# var = "that's my pen"
# print(var)

# 2 - \n iska kaam hota hai character ko new line mai print karna and \t charater ko same line print karna but tab jitna space ke bad 4 space ex:
# print("this is my pen\ncoulor is blue")
# print("the brand is\tbutterfly")

# 3 - len() lenght provide karta hai len("soh ail") iska output 7 aayega
# print(len("soh ail"))

# 4 - positive index start se start hota hai and negative end se ex:
# var = "sohail"
# print(var[2]) #output - h
# print(var[-3]) #output - a

# 5 - slicing mai last index count nai hota 1 subtract ho jata hai jaise str[0:3] so ye 0 se 2 tak ka print karega
# name = "sohail"
# print(name[0:3]) #output - soh

# 6 - find() us value ka index dundh ke deta hai jab vo pehli bar appear hui hogi tab ka and count() us value ko count karta hai kitne bar aayi hai find ka use tab karenge jab hame pata karna ho ki first time vo kon se index pe hai and count tab use karenge jab hame pata karna ho ki kitne bar hamne vo chiz apne string mai likhi hai

# 7 - pehle output aayega SohailAnsari kyunki isme space concatinate nahi kiye hai and second Sohail Ansari kyunki alag se " " space add kiye hai

# 8 - pehla output Hello new line mai World and second output Hello    World

# 9 - pehla ka output 6 length 6 hai isiliye and second output h and third output h

# 10 - first soh second soh third ohail fourth sohail

# 11 - first soh last index mai -1 ho jata hai so -3-1 = -4  second ail third soh

# 12 - first True second False third True

# 13 - ye first letter capital kar dega so output Sohail and original value change nahi hoti so second output sohail

# 14 - first i am learning python and second i am learnig html change nahi hoti original value

# 15 - fisrt 5 second 10 third -1

# 16 - first 3 second 1 third 1

# 17 - output = can vote

# 18 - iska output can not vote but apply for pan card

# 19 - output can not vote

# 20 - iska output a is positive and even

# 21 - a is negative

# 22 - a is 0 

# 23 - 
# s = "programming"
# print(s[-3::1])

# 24 -
# s = "programming"
# print(s[0])
# print(s[-1])

# 25 -
# s = "python"
# print(s[2:5])

# 26 - 
# s = "hello world"
# print(s[6:])

# 27 -
# s = "abcdefgh"
# print(s[1::2])

# 28 -
# s = "Sohail"
# print(s[-1::-1])

# 29 - error nahi aayega kyunki bhale hi end index bada ho but python jitne available hai utne print kar deta hai pehle mujhe laga error aayega but nahi
# s = "python"
# print(s[1:100])

