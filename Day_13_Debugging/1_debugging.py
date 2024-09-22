############ DEBUGGING #####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # Change the range from 1 to 21 
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # List is having a limit of index 5 so change the randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: # add = after > in 1994 then u get the print whrn u entered 1994
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") # Convert the input into int for comparing with an integer in if statement
# if age > 18:
# print(f"You can drive at age {age}.") # Add f before first inverted quoma to make it a f string and use indentation after if statement

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # Do not use == use only = for a variable 
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # To make this line work use indent
#   print(b_list)

# mutate([1,2,3,5,8,13])