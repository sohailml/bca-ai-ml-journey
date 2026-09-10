# random passsword generator
import random
import string

pswd_len = 8

charValue = string.ascii_letters + string.digits + string.punctuation

pswd = ""
for i in range(pswd_len):
    pswd += random.choice(charValue)
print("your random password is:",pswd)

#By list comprehension [funtion for i in range(n)]
res = [random.choice(charValue) for i in range(pswd_len)]   # this will give same output but in list
print(res)


# if we want in single string we use "".join()
rslt = "".join([random.choice(charValue) for i in range(pswd_len)])
print(rslt)
