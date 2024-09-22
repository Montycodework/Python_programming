print(8/3) # You get 2.66666666666665
print(int(8/3)) # You get 2 
print(round(8/3)) # You get 3 (Round off value)
print(round(8/3,2)) # Number of digits you want to make round off value

# instead of doing the above things use // you get the integer value and you dont need to use the type conversion for this  calculation
print(8//3)
print(type(8//3)) # This print the int class
print(type(8/3)) # This print the float class

#------------------------------------------------------------

score = 0


# User scores a point
score = score+1 # Take the previous value of score and add 1 in it
score += 1 # Same function but with short version
score -= 1
score *= 1
score /= 1
print(score)


# F string

# print("Your score is "+ score) # You will get an error because you can't concatinate string with numbers
print("Your score is "+ str(score)) # Error resolved

# Now F string comes in action

print(f"Your score is {score}") # shortest version to print str with int.

# _______________________________________________________
# Highlights of this session

# type casting
# round off function
# Operators
# F-string