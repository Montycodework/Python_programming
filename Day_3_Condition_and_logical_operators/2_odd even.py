# remainder operator (modulus)
# % is used as modulus in python
# 7 % 2 it means 2 is divided in parts of itself untill it terminates the number which is used oppositeof 2
# 2+2+2+1 here 7 is divided by 2 in itself parts untill 7 terminates itself and there is 1 left that is the remainder
# 7 % 2 = 1


# Conditional statements

# num = int(input("Enter the number\n"))
# if num%2 == 0:
#   print(str(num)+" is a Even number")
# else:
#   print(str(num)+" is a odd number")  


# nested if else staements

# if condition:
#   if another condition:
#     do this
#   else:
#     do this  
# else:
#   do this

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
  age = int(input("What is your age in years? "))
  if age <= 18: 
    print("Your age is lesser than required")
  else:
    print("You are eligible for this ride.")
else:
  print("You are not eligible for this ride.")

  print("Enjoy the ride !!!!!")  

# If elif else statements

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height>=120:
  print("You are eligible")
  age = int(input("What is your age in years? "))
  if age<12:
    print("Please pay Rs.5")
  elif age<=18:
    print("please pay Rs.10")    
  elif age>18:
    print("Please pay Rs.20")
else:
  print("You are not eligible for this ride")


  # ________________________________________________________________________

  # Hightlights of this session

  # If and else
  # nested if
  # Operators (Comparison)
  # Input
