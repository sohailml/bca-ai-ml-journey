# Practice Set (55 Questions) for 🐍 Python Basics — Day 1

"""
🟢 Category 1: Warm-Up (Basics Confirm) — Q1-Q6

Q1. print() function ka kaam kya hai? Ek line mein likho.

Q2. In sab mein se kaunsa valid variable name hai aur kaunsa nahi? Reason batao:
a) name
b) 2name
c) _name
d) my-name
e) Name
f) myName2
g) class
h) PRICE

Q3. name aur Name — ye same variable hain ya alag? Kyun?

Q4. In sab ka data type batao:
a) 5
b) 5.0
c) "5"
d) True
e) None
f) -3.14

Q5. True, False, None — inko capital letter se kyun likhte hain? Agar true (small) likhenge toh kya hoga?

Q6. Comment likhne ke kitne tarike hain Python mein? Shortcut kya hai VS Code mein?

🔵 Category 2: Output Predict (Bin Chala Ke Bata) — Q7-Q16

Q7.
print("Hello")
print('World')
print("Hello World")
Output?

Q8.
a = 10
b = 3
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
Char lines ka output?

Q9.
a, b = 1, 2.0
print(a + b)
print(type(a + b))

Q10.
print(type(5))
print(type(5.0))
print(type("5"))
print(type(True))
print(type(None))

Q11.
x = 5
x += 3
x *= 2
print(x)

Q12.
a = 10
b = 3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

Q13.
print(True + True)
print(True + False)
print(False + False)
print(True * 5)
Kya aayega? (Hint: bool int ka subclass hai)

Q14.
print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 - 4 / 2)
print(2 ** 3 ** 2)
BODMAS aur right-to-left associativity ka dhyan rakhna.

Q15.
a = 5
b = a
a = 10
print(b)
b ki value kya hogi — 5 ya 10?

Q16.
print("5" + "5")
print("5" * 3)
print(5 + 5)
Teeno lines ka output?

🟡 Category 3: Logic Building (Sochna Padhe) — Q17-Q28

Q17. Ek variable price = 99.99 hai. Ise integer mein convert karo aur print karo. Kya value aayegi — 99 ya 100?

Q18. User se do numbers input lo aur unka sum print karo. (Hint: input() string deta hai, cast karna padega)

Q19. User se naam aur age input lo, aur aise print karo:
Hello Sohail, your age is 22

Q20. Ek number n = 47 hai. Batao wo even hai ya odd — sirf % operator use karke. (if-else allowed hai)

Q21. Ek string "123" ko integer mein convert karo, usme 10 add karo, aur result print karo.

Q22. a = 5, b = 2. Bina third variable use kiye a aur b ki values swap karo. (Python trick use kar sakte ho)

Q23. Ek number num = 12345 hai. Iska last digit nikalo sirf operator se (string convert nahi karna).

Q24. User se ek float input lo (e.g., 45.67) aur usko int mein convert karke print karo. Kya decimal part hat jayega ya round hoga?

Q25. Ek variable x = 10. Ise string "10" mein convert karo aur dono ko add karke dekho — kya error aayega?

Q26. Ek variable hai result = 2 + 3 * 4 - 6 / 2. Bina chala ke batao output kya hoga (float ya int?).

Q27. User se 3 subjects ke marks input lo (int), average nikalo, aur print karo.

Q28. n = 5. Batao n ka square, cube, aur square root — bina math module use kiye cube aur square tak nikaalo.

🟠 Category 4: Tricky / Edge Case (Interview Traps) — Q29-Q38

Q29. Ye code kya print karega?
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
Kyun aisa hota hai?

Q30. int("5.5") — kya ye kaam karega? Agar nahi, toh 5.5 ko int kaise banayenge?

Q31. int("abc") chalega? Kya error aayega?

Q32. bool(""), bool("0"), bool(0), bool([]), bool("False") — in sab ka output batao. (Hint: falsy values)

Q33. None + 5 — kya hoga? Error ya value?

Q34. Ye code:
x = "10"
y = 20
print(x + y)
Kya print hoga? Reason?

Q35. print("A" > "B") — kya aayega True ya False? String comparison kaise hoti hai?

Q36.
a = 5
b = 5
print(a is b)

c = [1, 2]
d = [1, 2]
print(c == d)
print(c is d)
== aur is mein kya farak? Output batao.

Q37.
print(True == 1)
print(True == 2)
print(False == 0)
print("1" == 1)
Kya aayega?

Q38. Ye code error dega ya chalega?
5 = a
print(a)
Kyun?

🔴 Category 5: Debugging (Bug Dhundho) — Q39-Q45

Q39.
name = "Sohail
print(name)
Bug kya hai?

Q40.
2num = 10
print(2num)
Error kya aayega?

Q41.
num = input("Enter number: ")
result = num + 5
print(result)
Bug kya hai? Fix karo.

Q42.
Price = 100
print(price)
Kya error aayega aur kyun?

Q43.
x = 5
y = "10"
print(x + int(y))
print(x + y)
Kaunsi line error degi?

Q44.
a = 10
b = 0
print(a / b)
Kya error aayega?

Q45.
print("Result:", 5 + "5")
Error kyun aayega? Fix karo (do tarike batao).

🟣 Category 6: Challenge (High-IQ Level) — Q46-Q55

Q46. Bina int() ya float() use kiye, sirf arithmetic operators se "5" string ko number mein convert karo. (Hint: "5" * 1 kya karega?)

Q47. User se ek number input lo. Bina if-else use kiye batao wo even hai ya odd. (Hint: list indexing)

Q48. Ek 3-digit number n = 456 hai. Uske digits ka sum nikalo bina string convert kiye — sirf % aur // se.

Q49. Bina koi built-in function (jaise abs(), max()) use kiye, do numbers a = -15, b = 8 mein se bada number nikalo.

Q50. num = 12345. Ise reverse karo bina string mein convert kiye — pure math se.

Q51. Ek number input lo. Batao wo perfect square hai ya nahi — bina math.sqrt() ke. (Hint: ** 0.5 ya loop)

Q52. Bina third variable aur bina Python swap trick ke, a = 5, b = 10 ko swap karo — sirf + aur - se.

Q53. Ye code kya print karega aur kyun?
a = 256
b = 256
print(a is b)

x = 257
y = 257
print(x is y)
(Small integer caching ka concept)

Q54. Ek user se seconds input lo (e.g., 3665). Ise hours, minutes, seconds mein convert karke print karo. (e.g., 1h 1m 5s)

Q55. Bina type() function use kiye, kisi bhi variable ka type batao sirf ek trick se. (Hint: kuch aisa socho jo har type pe alag behave kare)

🟢 Category 7: Write a Program (Concept Solid Karne Ke Liye) — Q56-Q80

🟩 Level 1: Starter (Basic Practice) — Q56-Q63

Q56. Ek program likho jo apna naam, age, aur city print kare — har cheez alag line pe.

Q57. Ek program likho jo do numbers a = 25, b = 7 le aur unka sum, difference, product, quotient, remainder print kare.

Q58. Ek program likho jo ek number n = 45 ka square aur cube print kare.

Q59. Ek program likho jo rectangle ki length aur breadth le (variables mein store karo) aur uska area aur perimeter print kare.

Q60. Ek program likho jo temperature Celsius mein le aur Fahrenheit mein convert karke print kare. Formula: F = (C × 9/5) + 32

Q61. Ek program likho jo ek string variable banaye aur usko integer mein convert karke 100 add karke print kare.

Q62. Ek program likho jo do float numbers le aur unka average print kare.

Q63. Ek program likho jo check kare ki a = 10 aur b = 20 mein a chhota hai ya nahi (sirf comparison operator use karo, output True/False).

🟨 Level 2: User Input Based — Q64-Q71
Q64. Ek program likho jo user se uska naam aur age le aur aise print kare:
Hello [name], you are [age] years old.

Q65. Ek program likho jo user se do numbers le aur unka sum, difference, product, aur division print kare.

Q66. Ek program likho jo user se radius le aur circle ka area aur circumference print kare. Use pi = 3.14159.

Q67. Ek program likho jo user se principal, rate, time le aur simple interest nikaale. Formula: SI = (P × R × T) / 100

Q68. Ek program likho jo user se 3 subject ke marks le (int mein convert karke) aur unka total aur average print kare.

Q69. Ek program likho jo user se do numbers le aur check kare ki dono equal hain ya nahi (True/False print kare).

Q70. Ek program likho jo user se ek float le aur usko integer mein convert karke print kare. Saath mein original aur converted dono dikhao.

Q71. Ek program likho jo user se minutes le aur unhe hours aur minutes mein convert karke print kare. (e.g., 130 min → 2 hours 10 minutes) — sirf // aur % use karo.

🟧 Level 3: Logic + Concept Clear — Q72-Q77
Q72. Ek program likho jo user se do numbers le aur batao ki unka sum even hai ya odd (True/False print karo using %).

Q73. Ek program likho jo ek 4-digit number (jaise 5678) ka first digit aur last digit print kare — sirf // aur % use karke, string convert nahi karna.

Q74. Ek program likho jo user se ek number le aur uske saare digits ka sum nikaale — lekin sirf arithmetic operators se (string mein convert nahi karna). Hint: % 10 aur // 10.

Q75. Ek program likho jo user se ek 3-digit number le aur usko reverse karke print kare — bina string conversion ke, sirf math se.

Q76. Ek program likho jo user se seconds le aur usko hours, minutes, seconds mein convert karke aise print kare:
3665 seconds = 1 hour, 1 minute, 5 seconds

Q77. Ek program likho jo user se do numbers le aur bina third variable use kiye unko swap karke print kare. (Python trick use kar sakte ho, aur ek baar bina trick ke bhi try karo.)

🟥 Level 4: Challenge (Real Interview Level) — Q78-Q80
Q78. Ek program likho jo user se ek integer le aur batao ki wo positive, negative, ya zero hai — sirf comparison operators aur boolean logic se. (if-else allowed hai)

Q79. Ek program likho jo user se student ka naam, 3 subject marks le aur output aise de:
Student: Sohail
Total: 245
Average: 81.67
Percentage: 81.67%
Result: PASS   (agar average >= 33)
(Result ke liye if-else use kar sakte ho)

Q80. Ek program likho jo user se ek 5-digit number le aur uske saare digits ko alag-alag line pe print kare — bina string conversion ke. (Hint: // aur % ka combo — thoda sochna padega, 5 digit ke liye)

"""

# ANSWER

"""
1 - print() function ke andar jo bhi hota hai vo usse print karta hai

2 - option b and d variable nahi hai kyunki variable number se start nahi hota hai and special chracter nahi ho sakta

3 - name and Name alag alag variables hai kyunki pyhton case senstive hota hai

4 - a = int , b = float , c = string , d = bool , e = None , f = float

5 - True None False ye capital letter mai likhte hai ye keywords hai small mai likh ke variable bana sakte hai but jo kaam True False ka hota hai vo nahi hoga fir

6 - comment karne ka ek tarika hai aage # lagana or dusra multiline so triple comma mai likh sakte hai and vs code mai ctrl + / se bhi comment ho jata hai 

7 - iska output hoga Hello fir new line ke bad World and new line ke bad Hello World

8 - iska output hoga pehle 3.33 fir 3 fir 1 fir 1000

9 - iska output hoga 3.0 and type float

10 - iska output int fir  float fir string fir bool fir none

11 - iska output 16

12 - iska output False fir True fir True fir False

13 - True = 1 False = 0 so output 2 fir 1 fir 0 fir 5

14 - pehle 14 fir 20 fir 8.0 fir fir 512 , because 2 ** (3 ** 2) right-to-left associativity

15 - b ki value 5

16 - pehle 55 fir 555 fir 10

"""
# 17 - output 99
# price = 99.99
# print(int(price))

# 18 - 
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(num1+num2)

