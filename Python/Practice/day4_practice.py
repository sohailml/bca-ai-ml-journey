"""Question 1: Store following word meanings in a python dictionary : table : “a piece of furniture”
,“list of facts & figures” cat : “a small animal”"""
dict = {"table": ["a piece of furniture","a list of facts and figure"],"cat": "a small animal"}
print(dict)


"""Question 2: You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students 
python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C” """
subject = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(subject)
print("Number of classroom: ",len(subject))


"""Question 3: WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value."""
sub1 = int(input("enter you phy marks: "))
sub2 = int(input("enter you chem marks: "))
sub3 = int(input("enter you maths marks: "))
marks_of_student = {

}
marks_of_student.update({"phy":sub1})
marks_of_student.update({"chem":sub1})
marks_of_student.update({"math":sub1})
print(marks_of_student)


"""Question 4: Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)"""
value = {9,9.0,'9.0'}
print(value)
val = {("float",9.0),("int",9)}
print(val)
