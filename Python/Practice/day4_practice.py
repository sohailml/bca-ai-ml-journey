"""Question 1: Store following word meanings in a python dictionary : table : “a piece of furniture”
,“list of facts & figures” cat : “a small animal”"""
# dict = {"table": ["a piece of furniture","a list of facts and figure"],"cat": "a small animal"}
# print(dict)


"""Question 2: You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students 
python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C” """
# subject = {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(subject)
# print("Number of classroom: ",len(subject))


"""Question 3: WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value."""
# sub1 = int(input("enter you phy marks: "))
# sub2 = int(input("enter you chem marks: "))
# sub3 = int(input("enter you maths marks: "))
# marks_of_student = {

# }
# marks_of_student.update({"phy":sub1})
# marks_of_student.update({"chem":sub1})
# marks_of_student.update({"math":sub1})
# print(marks_of_student)


"""Question 4: Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)"""
# value = {9,9.0,'9.0'}
# print(value)
# val = {("float",9.0),("int",9)}
# print(val)

#basic test-python
"""Q1. The Forbidden Swap (Nested Dict Keys) 🧨
Ek dictionary di gayi hai:
d = {
    "level1": {"key": "A", "value": 100},
    "level2": {"key": "B", "value": 200}
}
Bina kisi temporary variable (temp) ke, aur bina kisi if condition ke, level1 ki "key" aur level2 ki "key" ko swap kar do.
(Hint: Simultaneous assignment ka use hai, par nesting ka dhyan rakhna). Print karo d ko.
"""
# d = {
#     "level1": {"key": "A", "value": 100},
#     "level2": {"key": "B", "value": 200}
# }
# d["level1"]["key"],d["level2"]["key"] = d["level2"]["key"],d["level1"]["key"]
# print(d)


"""Q2. The Unique String Verifier (Set + String Slicing) 🔍
User se ek string input lo (maan lo word = "programming").
Task: Bina kisi loop ke, ek hi line me check karo ki is string me kitne unique characters hain. 
Agar total length (len) aur unique characters ki count ka difference 3 hai, toh "Special String" print karo,
warna "Normal String" print karo.
(Isko solve karne ke liye tujhe set(), len(), aur arithmetic operator ka use karna padega)"""
# n = input("enter a word: ")
# s = set(n)
# print("you have",len(s),"unique characters")
# if (len(n)-len(s) == 3):
#     print(n,"is special string")
# else:
#     print("normal string")


"""Q3. The Two-Faced Set 🎭
Ek set hai: s = {1, 2, 3, 4, 5}
Tujhe is set ke pehle 3 elements (jo bhi randomly aayein) ko ek tuple me convert karna hai, 
aur baaki ke 2 elements ko ek alag tuple me convert karna hai. Bina loop ke, sirf list(), set(), tuple slicing,
aur methods ka use karke yeh kaam karo."""
# s = {1, 2, 3, 4, 5}
# s_lst = list(s)
# tup = tuple(s_lst[0:3])
# print(tup)
# tup2 = tuple(s_lst[3:])
# print(tup2)


"""Q4. The Dictionary Value Extractor (Nested .get() Challenge) 📦
user = {
    "profile": {
        "personal": {
            "name": "Sohail"
        }
    }
}
Task: Bina if statement use kiye, user dictionary se "city" ki value nikaal kar print karo. 
Agar "city" nahi milti, toh "Unknown City" print karo. Agar "profile" hi nahi mila, toh "No Profile" print karo."""
# user = {
#     "profile": {
#         "personal": {
#             "name": "Sohail"
#         }
#     }
# }
# city = user.get("profile",{}).get("personal",{}).get("city","unkown city")
# print(city)

"""Q5. The Immutable vs Mutable (Output Prediction) 🤯
Bina code run kiye, neeche diye code ka exact output batao, aur ek line mein reason likho:
a = {1, 2, 3}
b = a.copy()
c = a
a.add(4)
b.add(5)
print(a)
print(b)
print(c)"""
# a = {1, 2, 3}
# b = a.copy()
# c = a
# a.add(4)
# b.add(5)
# print(a)  # iska output {1,2,3,4} randomly
# print(b)  # iska output {1,2,3,5}
# print(c)  # iska output {1,2,3,4}


"""Q6. The Ultimate Brain Fryer (Symmetric Difference Without ^) 🔥
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
Task: Bina ^ operator aur bina symmetric_difference() method ke, 
inn sets ka symmetric difference (wo elements jo dono me nahi aate, i.e., {10,20,50,60}) nikaal kar print karo. 
Tum sirf union(), intersection(), aur difference() methods use kar sakte ho."""
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
# set3 = set1.union(set2)
# set4 = set1.intersection(set2)
# print(set3 - set4)
