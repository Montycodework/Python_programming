len("Hello")  # len function easily work with a string
len(12345) # But len function can't work with integers and throw an error.


# type casting or conversion

new_char = len(input("What is your name: ")) # We will gwt thw integer value from this function
new_num_char = str(new_char) # In this we are converting the integer into string by using str type casting function

print("Your name has "+new_num_char+" characters.") # new_num_char has the converted data inside it and printing it when required


# how to check the type of a particular data you are UserWarning

# print(type(put the data here to check the data type))

print(type("Hello")) # A string <str>
print(type(1234)) # A integer <int>
print(type(123.345)) # A float <float>
print(type(True)) # A boolean <bool>

# converting the data type into another 

a = 1234 # This is an integer 
# str(1234) this is how you can convert a integer into string and when you print the type of this data it becomes string now
print(str(1234)) # This is looks like a integer but it is converted into string by using str before puting the data in brackets

print(int(1234)) # An integer type data
print(float(1234)) # An float type data
print(bool(1234)) # An boolean type data



# ____________________________________________
# Highlights of this session


# len function
# type casting
