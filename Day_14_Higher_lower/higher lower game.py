from game_data import data
from art import logo
from art import vs
# from replit import clear
import random
print(logo)
# #############################################################################

# # Todo: 1- how to print the random choice from data
# compare = random.choice(data)
# against = random.choice(data)  

# ################################################################################

# # To put the dict values into list 
# value_listA = list(compare.values())
# compare_A = (f"Compare (A). A {value_listA[2]}, {value_listA[0]} in {value_listA[3]}")
# value_listB = list(against.values())
# against_B = (f"Against (B). A {value_listB[2]}, {value_listB[0]} in {value_listB[3]}")
# print(compare_A)
# # print(vs)
# print(against_B)

# ##################################################################################

# # User Choice
# user_choice = input("Which of these have more followers Type 'A' or 'B': ")
# if user_choice == "A":
#   user_answer = value_listA[1]
#   computer_answer = value_listB[1]
# elif user_choice == "B":
#   user_answer = value_listB[1]
#   computer_answer = value_listA[1]

# ############################################################
# # Comparison  
# if user_answer > computer_answer:
#   print("You win")
# else:
#   print("You loose")    

# # print(f"User answer{user_answer}, computer answer {computer_answer}")    

#------------------------------------------------------------------------------------------------------------------------------------------
# 1st step
compare = random.choice(data)
value_listA = list(compare.values())
compare_A = (f"A {value_listA[2]}, a {value_listA[0]} from {value_listA[3]}")

# 2nd step
against = random.choice(data)
value_listB = list(against.values())
against_B = (f"A {value_listB[2]}, a {value_listB[0]} from {value_listB[3]}")

# 3rd step
print(compare_A)
print(vs)
print(against_B)

# 4rth step
score = 0
is_game = True
while is_game:
  user_choice = input("Which of these have more followers Type 'A' or 'B': ")
  if user_choice == "A":
    UA = value_listA[1]
    CB = value_listB[1]
  elif user_choice == "B":
    UA = value_listB[1]
    CB = value_listA[1]

  # 5th step  
  if UA>CB:
    compare_A = against_B
    against = random.choice(data)
    value_listB = list(against.values())
    against_B = (f"A {value_listB[2]}, a {value_listB[0]} from {value_listB[3]}")
    # clear()
    print(logo)
    print(compare_A)
    print(vs)
    print(against_B)
    score += 1
    print(f"Current score is: {score}")
  elif UA<CB:
    print(f"Sorry that's wrong : Final score is {score} ")
    is_game = False