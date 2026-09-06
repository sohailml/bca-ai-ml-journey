f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt","r")
data = f.read(5)
print(data)
print(type(data))
f.close()

f = open("demo.txt","r")
data = f.readline()  #one line at a time 
print(data)
print(type(data))
f.close()

f = open("demo.txt","w")
f.write("i want to be a ai/ml engineer")
f.close()

f = open("demo.txt","a")
f.write("then i'll learn numpy")
f.write("\nafter that pandas")
f.close()

f = open("sample.txt","w") #make new file
f.close()

f = open("sample.txt","r+")  #starting postition se overwrite ke liye r+
f.write("abcs")
print(f.read())
f.close()

f =open("sample.txt","w+")   # writing reading
f.write("so w+ mode se likhenge and ye purana data truncat kar dega yani ki delete ")
f.close()

f =open("sample.txt","a+")   # writing reading
f.write("so a+ mode se likhenge so ye purana data truncat nahi karega and overwrite kar dega")
print(f.read()) #give blank line beacuse of pointer
f.close()

# with  syantax
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("sample.txt","w") as f:
    f.write("with ke sath wirite")

#deleting a file
import os
os.remove("deletingfile")
