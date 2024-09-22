# # Function

# def my_function():
#   print("Hello")

# my_function()

# # Function with inputs

# def my_function(name, number):
#   print(name)
#   print(number)

# my_function("Monty", 20)


# # Function with outputs

# def my_function():
#   return 3*2

# output = my_function()
# print(output)

#------------------------------------------------------------------------------

# Return function 

# def format_name(f_name, l_name):
#   # print(f_name.title())
#   # print(l_name.title())
#   formated_f_name = f_name.title() # same result of above print functions
#   formated_l_name = l_name.title()
#   # print(f"{formated_f_name} {formated_l_name}")
#   return(f"{formated_f_name} {formated_l_name}")

# # format_name("monty","MONTY")
# formated_string = format_name("monty","hindustani") # same reult of above line 
# print(formated_string) 


# --------Multiple return functions---------------


# def format_name(f_name, l_name):
 
#   formated_f_name = f_name.title() 
#   formated_l_name = l_name.title()
#   return(f"{formated_f_name} {formated_l_name}")

# # formated_string = format_name("monty","hindustani") 
# # print(formated_string)
# print(format_name(input("What is your first name? "),input("What is your last name? "))) # Passing values inside a function with inputs



# When you dont pass the values in function

def format_name(f_name, l_name):
 if f_name == "" or l_name == "":
   return "You did'nt provide any inputs" # If the user input an empty string thne the code return frome here and not executing the rest of the tha code


 formated_f_name = f_name.title() 
 formated_l_name = l_name.title()
 return(f"{formated_f_name} {formated_l_name}")

# formated_string = format_name("monty","hindustani") 
# print(formated_string)
print(format_name(input("What is your first name? "),input("What is your last name? "))) # Passing values inside a function with inputs