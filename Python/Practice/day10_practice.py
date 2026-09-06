"""Q1: Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I lik programming in Java"""
# f = open("practice.txt","w")
# f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")
# f.close()


"""Q2: WAF that replace all occurrences of “java” with “python” in above file."""
# def replac():
#     with open("practice.txt","r") as f:
#         data = f.read()

#     new_data = data.replace("Java","python")
#     print(new_data)

# replac()

# with open("practice.txt","w") as f:
#     f.write(new_data)


"""Q3: Search if the word “learning” exists in the file or not."""
# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")


"""Q4: WAF to find in which line of the file does the word “learning”occur first.
Print -1 if word not found."""
# def check_of_line():
#     word = "programming"
#     line_no = 1
#     data = True
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1

#     print(-1)
# check_of_line()


"""Q5: From a file containing numbers separated by comma, print the count of even numbers."""
# count = 0
# with open("number.txt","r") as f:
#     data = f.read()
#     nums = data.split(",")
#     for val in nums:
#         if (int(val) % 2 == 0):
#             count +=1
# print(count)
