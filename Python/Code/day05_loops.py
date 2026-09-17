# day 5 of my jurney

# loops in python
# While loop
i = 1
while i<=5: #printing value while condition is true
    print("sohail")
    i += 1
print("ended")

j = 1
while j<=10:
    print(j)
    j += 1
print("ended")

k = 5
while k>=1:
    print(k)
    k -= 1
print("ended")

# Break and Continue
i = 1
while i<=5:
    print(i)
    if (i == 3):
        break                  #it break loop and when condition will true and not run next code
    i += 1
print("end of loop")

i = 0
while i<=5:
    if (i == 3):
        i += 1
        continue            #skip that and move to next code
    print(i)
    i += 1

j = 0
while j<=20:
    if (j%2 == 0):
        j += 1
        continue
    print(j)
    j += 1

# for loops
lst = [1,2,4,6,9,3,5,2]
for num in lst:
    print(num)

tup = ("patato","onion", "chicken", "mutton")
for val in tup:
    print(val)

stng = "sohail ansari"
for char in stng:
    print(char)

# for loops with else:
name = "sohail ansari"
for char in name:
    if (char == "a"):
        break
    print(char)
else:
    print("end")

# range(start,stop,step) function return sequence of number.
for i in range(11):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(2,100,2): #even number
    print(i)

for i in range(1,100,2): #odd number
    print(i)

# pass statement or null statement , placeholder for future work
# for i in range(6):
#     #we want empty
# print("end")  #it give error because after for loop code can not be empty thats why we use pass
for i in range(6):
    pass
if i > 5:
    pass
print("end")
