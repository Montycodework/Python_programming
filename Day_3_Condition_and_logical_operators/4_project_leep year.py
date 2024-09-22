# my program

# print("Leep year founder")
# year = int(input("Enter the year: "))

# if year%4==0 or year%100==0 or year%400==0:
#   print(f"{year} is a leep year")
# else:
#   print(f"{year} is not a leep year")  





# teacher version

# print("Leep year founder")
# year = int(input("Enter the year: "))

# if year%4==0:
#   if year%100==0:
#     if year%400==0:
#       print("A Leap year")
#     else:
#       print("Not a Leap year")  
#   else:
#     print("A Leap year")    
# else:
#   print("Not a Leap year")    


# Multiple if /else


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
  want_photo = input("Do you want photo of your ride ans. in Y or N\n")
  if want_photo == "Y":
    bill+=3
    print(f"Your bill is Rs.{bill}")  
else:
  print("You are not eligible for this ride")


  # _________________________________________________________________
  # Hightlights of this session

  # Nested if
  # input
  # project
  # Operators(Comparison),(Assigning)