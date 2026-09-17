#day 4 of my jurney

# dictionary in python
info = {
    "key" : "value",
    "name" : "sohail",
    "age" : 18,
    "learning" : "python",
    "subject" : ["python ","java","c"], #can store lsit and tuple
    "topic" : ("dictionary", "set"),
    12 : "key can be number",
    "name" : "golden" #dict mai key unique hoti hai duplicate se purani value overwrite ho jati hai. value can be same
}

null_dict = { #null dictionary

}
print(type(null_dict))
print(info)
print(info["age"])
info["age"] = 19
print(info["age"]) #dictionary is mutable
# print(info[0]) # error dictionary is unorderd
print(info["name"])
info["surname"] = "ansari" # add in dict
print(info)

# nested dictinoray : dictonary ke andar dictnoray
student ={
    "name" : "sohail",
    "subject_marks" : {
        "phy" : 67,
        "chem" : 47,
        "maths" : 93
    },
    "is_pass" : True,
    "total" : 207
}

print(student)
print(student["subject_marks"])
print(student["subject_marks"]["maths"])


# dictionary methods
dict = {
    "name" : "sohail",
    "age" : 18,
    "learning" : "python",
    "subject" : ["python ","java","c"],
    "topic" : ("dictionary", "set"),
    12 : "key can be number",
}
print(len(dict)) #total number of keys
print(dict.keys()) #print all key
print(list(dict.keys())) # print all key in list (type casting)
print(len(list(dict.keys())))

print(dict.values()) #print all value
print(list(dict.values())) # print all value in list (type casting)

print(dict.items()) # return key value pair in tuple
pair =list(dict.items())
print(pair[0])

print(dict["name"])
print(dict.get("name"))
# print(dict["name2"]) #error
print(dict.get("name2")) # no error give none

dict.update({"class" : "college"}) #update old dict
print(dict)
new_dict= {"city": "delhi","salary":23000}
dict.update(new_dict)
print(dict)

# set in python
num = {1,3,8,4,5} #sets unorderd and each element must be uniqe and immutable
num2 = {1,3,3,2,9,7,6} #repeated element store only once
#num3 = {1,25.99,"sohail",(1,2),(1,2,"sohail"),{"key":"value"}} # error list and dict can not add because they are mutable
print(num)
print(num2)
print(type(num))

null_set = set()
print(type(null_set))

# set method
null_set.add(4) #add an elemnt set is mutable but not its element
null_set.add("sohail")
null_set.add(56)
print(null_set)
null_set.remove(4) #remove an element
print(null_set)
null_set.pop() # remove randome value give error if set empty
print(null_set)
null_set.clear() # clear entire set
print(null_set)
print(num.union(num2)) #combines both set and give new set
print(num.intersection(num2)) # combine only common value
