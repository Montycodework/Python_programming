programming_dict = {
  "Bug": "An error in a program that prevents you to run the code",
  "Function": "A piece of code that you can easily call over and over again",
  "Loop": "The action of doing something over and over again",
}

print(programming_dict["Bug"]) # here you need to call the key with correct spelling for getting the value of that key.
# print(programming_dict[Bug]) # In this line you ll get the error because you have to call the key at its original
# datatype . in the dic "Bug" is a string but now you are calling it as a variable name.

# Adding a new key and Value

programming_dict["Python"] = "A easiest coding language "

print(programming_dict["Python"])
print(programming_dict)

# you can also start with an empty dictionary and then add the keys and value by this method

empty_dict = {}
empty_dict["Loop"] = "Repeatetive proces in coding language"
print(empty_dict) # now loop is shown when u print 


# You can also wipe the existing dictonary 
programming_dict = {}
print(programming_dict) # You ll get only curly braces after this {}
# Jese game start hone pe score vgera zero karne hote he to usme iska use kar skte he



# Edit an item in the dictionary

programming_dict["Bug"] = "the value is changed"
print(programming_dict) # Now the previous value of "Bug" is changed now


# How to loop through the dictionary (dictionary me loop kese lagye)

programming_dict = {
  "Bug": "An error in a program that prevents you to run the code",
  "Function": "A piece of code that you can easily call over and over again",
  "Loop": "The action of doing something over and over again",
}

for thing in programming_dict:
  print(thing) # Same hi tareeka he  loop lgane ka but isme aapko sirf key print hoke milegi value nhi.
  print(programming_dict[thing]) # isse aap programming_dict ki values bhi mil jyegi
 



