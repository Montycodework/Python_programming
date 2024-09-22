height = input("What is your height in m: ")
weight = input("What is your weight in kg: ")

# BMI  = weight/height**2 # Type error because input comes from weight and height is string and 2 is int and you can't use string data with integer 

# First technique
BMI  = int(weight)/float(height)**2
BMI_as_int = int(BMI) # To cut off the digit comes after the decimal
# print(BMI_as_int)

# Second technique
h = float(height) # Height as float
w = int(weight) # Weight as integer
BMI = int(w/h**2) # BMI as integer
print(BMI)


# _________________________________________________
# Highlights of this session

# project (BMI calculatos)
# Input function
# Operators
