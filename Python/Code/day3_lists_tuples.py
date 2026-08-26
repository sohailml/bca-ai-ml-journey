# day 3 of mu jurney

#list:
marks =[85,94.4,80,70.5,"sohail","arbaaz"] #mutable
print(marks,type(marks))
print(len(marks))
# list mutable
print(marks[3])
marks[3] = 70

 #strings imutable
str="hello"
print(str[0])
str[0]="y" #error

#indexing:
print(marks[0])
print(marks[-1])
print(marks[-4])
print(marks[6]) #error there is no 6 character in list

#list slicing
print(marks[0:3])
print(marks[0:])
print(marks[-5:-1])

# list method
list = [1,3,5,7,87,9,1,3]
list.append(4) #add one element at last in list
print(list)

list.sort() #convert list into ascending order
print(list)

list.sort(reverse=True) #convert list into descending order
print(list)

list.reverse() #print list from backside
print(list)

list.insert(2,"sohail") #insert value at specific index
print(list)

list.remove(1) # remove where it is occure at first time
print(list)

list.pop(4) #remove item at that index
print(list)

list.copy()
print(list)

#Tuple
tup = (1,3,2,7,4,9,3,5) #immutable
print(tup)
print(type(tup))
print(tup[1])

tup1 = () #Empty touple
print(type(tup1))

# Tuple slicing
print(tup[1:5])
print(tup[-5:-1])

# Tuple method
print(tup.index(4)) #return idex of first occurence 
print(tup.count(1)) #count total occurence
