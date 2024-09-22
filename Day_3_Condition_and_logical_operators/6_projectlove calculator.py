Boy = input("Enter your name boy:\n")
Girl = input("Enter your name girl:\n")

combined_name = Boy+Girl
lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t+r+u+e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score>=90:
  print("Best")
elif love_score<90 and love_score>=50:
  print("Nice")
else:
  print("Split it cant works")    


# ________________________________________________________________________________________
#  Hightlight of this session


# Project
# Input
# Type casting
# lower case method
# Count method
# if and else