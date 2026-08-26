# # Question 1: WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
first=input("Enter your first favourite movie: ")
second=input("Enter your second favourite movie: ")
third=input("Enter your third favourite movie: ")

list_of_your_favourite_movie =[first,second,third]
print(list_of_your_favourite_movie)

# #second solution
Movies=[]
mov1=input("Enter your first favourite movie: ")
mov2=input("Enter your first favourite movie: ")
mov3=input("Enter your first favourite movie: ")
Movies.insert(0,mov1)
Movies.insert(1,mov2)
Movies.insert(2,mov3)
print(Movies)

#Question 2: WAP to check if a list contains a palindrome(1,2,3,2,1) of elements. (Hint: use copy( ) method)
list = [1,2,3,4,1]
list2 =list.copy()
list2.reverse()
if (list==list2):
    print("this list is palindrome")
else:
    print("this list is not palindrome")

# Question 3: WAP to count the number of students with the “A” grade in the following tuple.
Grade = ("C", "D", "A","A", "B", "B", "A")
print(Grade.count("A"))

#Question 4: Store the above values in a list & sort them from “A” to “D”
Grade1 = ["C", "D", "A","A", "B", "B", "A"]
Grade1.sort()
print(Grade1)
