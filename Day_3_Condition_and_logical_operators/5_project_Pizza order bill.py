# pizza bill 

# print("Welcome to !!!Pizza World!!!")
# size = input("What size pizza do you want S or M or L\n")
# cheese = input("Do you want extra cheese Y or N\n")
# add_paparoni = input("Do you wanted to add paperoni y or n\n")


# b = 0
# if size=="S":
#   b += 15
# elif size=="M":
#   b += 20
# else:
#   b += 25 
    
# if add_paparoni=="y":
#   if size=="S":
#     b += 2
#   else:
#     b += 3 

# if cheese=="Y":
#   b+=1
  
# print(f"Your total bill is {b}")


# Logical operator

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height>=120:
  print("You are eligible")
  age = int(input("What is your age in years? "))
  if age<12:
    bill = 5
    print("Child ticket Rs.5")
  elif age<=18:
    bill = 10
    print("Youth ticket Rs.10")    
  elif age>18:
    bill = 20
    print("Adult ticket Rs.20")
  want_photo = input("Do you want photo of your ride ans. in y or n\n")
  if want_photo == "y":
    if age>=40 and age<=60: #<---------------------------IMPORTANT
      print("Enjoy the free Ride")  
    else:
      bill += 5
      print("Enjoy the ride")
      print(f"Your bill is Rs.{bill}")  
else:
  print("You are not eligible for this ride")


# ____________________________________________________________

# Hightlights of this session

# Project
# Nested if
# Operators(Comparison),(Assignment)
# Input
