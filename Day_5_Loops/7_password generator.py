import random

letters  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","(",")","+"]

print("Welcome to the Py Password Generator!")
ur_letters = int(input("Enter how many alphabets u want in your password:\n"))
ur_numbers = int(input("Enter how many numbers u want in your password:\n"))
ur_symbols = int(input("Enter how many symbols u want in your password:\n"))


# Easy way to do this
# to make the series password like : letter comes first then number and then symbols
password = ""

for char in range(1, ur_letters  + 1):
  password += random.choice(letters)
  # password_list.append(random.choice(letters))    ye bhi same kam karega
for char in range(1, ur_numbers  + 1):
  password += random.choice(number)
for char in range(1, ur_symbols  + 1):
  password += random.choice(symbols) 

print(password)


# Hard way to do this
# lets make it absolute random 

password_list = [] # to yha hum password ko list banana pdega to hum usko uper vaps jake list bna dete he verna pehle hum usko ek blank string ki tra use kar rhe the password = "" ese.
# Ab password list ban chuka he to hum asani se uske under se random value print kar lenge
for char in range(1, ur_letters  + 1):
  password_list += random.choice(letters)
  # password_list.append(random.choice(letters))    ye bhi same kam karega
for char in range(1, ur_numbers  + 1):
  password_list += random.choice(number)
for char in range(1, ur_symbols  + 1):
  password_list += random.choice(symbols) 

print(password_list)     

random.shuffle(password_list) # to reorder the list
print(password_list)

password = ""
for char in password_list:
  password += char
print(f"Your Password is {password}")




# ___________________________________________________________________________
# Hiughlights of this session

# Khali string ko bna ke usme data bharna
# khali list bna ke usme content ko daalna
# random.shuffle()
# use of variable inside range brackets